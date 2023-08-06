import logging
import traceback
from collections import OrderedDict

import libsolace
from libsolace.settingsloader import settings
from libsolace import xml2dict
from libsolace.Exceptions import LoginException
from libsolace.SolaceCommandQueue import SolaceCommandQueue
from libsolace.SolaceXMLBuilder import SolaceXMLBuilder
from libsolace.plugin import PluginResponse

try:
    import simplejson
except ImportError:
    from json import simplejson

from libsolace.util import httpRequest, generateRequestHeaders, generateBasicAuthHeader

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class SolaceAPI:
    """
    Connects to a Solace cluster's *primary* and *backup* appliance(s)

    a SolaceAPI instance contains a SolaceXMLBuilder and a SolaceCommandQueue
    in order to facilitate the generation of SEMP XML requests, enqueuing the XML
    requests, and sending them to the appliance(s) through the rpc(str) method.

    SolaceAPI connects to **both** appliances in a redundant pair setup and gets
    the the *primary* and *backup* node states. Typically you issue the same SEMP
    command to both appliances. Commands can also be issued to either the primary
    or the backup appliance utilizing the `primaryOnly` and `backupOnly` kwargs.
    see: :func:`~libsolace.SolaceAPI.SolaceAPI.rpc`

    The version of the SolOS-TR OS is detected on automatically, and this behaviour
    can be overridden with the `version` kwarg. If using the VMR you will want to
    pass in both detect_status=False and version="soltr/7_1_1".

    :keyword environment: the environemnt
    :type environment: str
    :keyword detect_status: detection of node primary/backup status, pass True
        here for the VMR or single appliances.
    :type detect_status: bool
    :keyword version: override appliance version detection. Some versions of SolOS-TR
        require you to set the language level a bit higher like the VMR for example.
    :type version: str
    :keyword testmode: Tells the api to connect using the READ_ONLY_USER as defined
        in the libsolace.yaml file.
    :type testmode: bool
    :keyword setting_overrides: dictionary containing overrides for the settings in
        `libsolace.yaml`. Any key configured in this parameter will take precedence
        over keys specified in `libsolace.yaml`.
    :type setting_overrides: dict
    :rtype: SolaceAPI.SolaceAPI
    :returns: instance


    Examples:
        >>> from libsolace.SolaceXMLBuilder import SolaceXMLBuilder
        >>> api = SolaceAPI("dev")
        >>> api.x = SolaceXMLBuilder("LOG: Showing the Message Spool in %s" % api.environment, version=api.version)
        >>> api.x.show.message_spool.detail
        OrderedDict()
        >>> response = api.rpc(api.x)

        Setting the API version if detection fails

        >>> from libsolace.SolaceXMLBuilder import SolaceXMLBuilder
        >>> api = SolaceAPI("dev", version="soltr/7_1_1")
        >>> api.x = SolaceXMLBuilder("My description of what im doing", version=api.version)
        >>> api.x.show.message_spool
        OrderedDict()
        >>> response = api.rpc(api.x, primaryOnly=True)
        >>> response[0]['rpc-reply']['rpc']['show']['message-spool']['message-spool-info']['config-status']
        u'Enabled (Primary)'

        Query the backup appliance only

        >>> from libsolace.SolaceXMLBuilder import SolaceXMLBuilder
        >>> api = SolaceAPI("dev", detect_status=False)
        >>> api.x = SolaceXMLBuilder("My Something something", version=api.version)
        >>> api.x.show.version
        OrderedDict()
        >>> r = api.rpc(api.x, backupOnly=True)
        >>> # check the response was the "configured" backup
        >>> r[0]['HOST'] == settings["SOLACE_CONF"]["dev"]['MGMT'][1]
        True

        Get a instance of some plugin from the plugin manager

        >>> api = SolaceAPI("dev")
        >>> type(api.manage("NullPlugin"))
        <class 'libsolace.items.NullPlugin.NullPlugin'>

        """

    def __init__(self, environment, version=None, detect_status=True, testmode=False,
                 setting_overrides=None, **kwargs):
        try:
            logger.info("Solace Client SEMP version: %s", version)
            self.version = version

            self.settings = settings
            setting_overrides = [] if setting_overrides is None else setting_overrides
            self.settings.update(setting_overrides)

            self.config = self.settings["SOLACE_CONF"][environment]
            self.environment = environment

            logger.info("Connecting to appliances %s in %s",
                        self.config['MGMT'], environment)

            logger.debug("Loaded Config: %s", self.config)

            # testmode sets the user to the RO user
            self.testmode = testmode
            if self.testmode:
                self.config['USER'] = self.settings["READ_ONLY_USER"]
                self.config['PASS'] = self.settings["READ_ONLY_PASS"]
                logger.info('READONLY mode')

            # for SSL / TLS
            if 'VERIFY_SSL' not in self.config:
                self.config['VERIFY_SSL'] = True

            # detect primary / backup node instance states or assume
            # 1st node is primary and second is backup
            self.detect_status = detect_status
            if self.detect_status:
                logger.info("Detecting primary and backup node states")
                self.status = self.get_message_spool(**kwargs)
                self.primaryRouter = None
                self.backupRouter = None

                for node in self.status:
                    result = self.__detect_state(node)
                    if result == 'Primary':
                        self.primaryRouter = node['HOST']
                    elif result == 'Backup':
                        self.backupRouter = node['HOST']
                if self.primaryRouter is None:
                    raise Exception("Failed to detect primary router")
                if self.backupRouter is None:
                    raise Exception("Failed to detect backup router")
                if self.primaryRouter == self.backupRouter:
                    # impossible to test, but possible to happen...
                    raise Exception("Error, detected router %s to be both primary and backup", self.primaryRouter)
                logger.info("Detected primary Router: %s", self.primaryRouter)
                logger.info("Detected backup Router: %s", self.backupRouter)

            else:
                logger.info("Not detecting statuses, using config")
                try:
                    self.primaryRouter = self.config['MGMT'][0]
                except Exception, e:
                    logger.error("No routers")
                    raise
                try:
                    self.backupRouter = self.config['MGMT'][1]
                except IndexError, e:
                    logger.warn("No second router in config")
                    kwargs["primaryOnly"] = True
                    kwargs["backupOnly"] = False
                    pass

            # if the version is NOT specified, query appliance versions
            # assumes that backup and primary are SAME firmware version.s
            if version == None:
                logger.debug("Detecting Version")
                self.xmlbuilder = SolaceXMLBuilder("Detecting SolOS-TR Version", version="soltr/5_0")
                self.xmlbuilder.show.version
                result = self.rpc(str(self.xmlbuilder), **kwargs)
                self.version = result[0]['rpc-reply']['@semp-version']
            else:
                logger.info("Override SolOS-TR Version: %s", version)
                self.version = version
            logger.info("SolOS-TR Version: %s", self.version)

            # backwards compatibility
            # self.xmlbuilder = SolaceXMLBuilder(version=self.version)

            # shortcut / new methods
            self.x = SolaceXMLBuilder("XML Buider", version=self.version)
            self.cq = SolaceCommandQueue(version=self.version)

        except Exception, e:
            logger.warn("Solace Error %s" % e)
            raise

    def __restcall(self, request, primaryOnly=False, backupOnly=False, **kwargs):
        logger.info("%s user requesting: %s kwargs:%s primaryOnly:%s backupOnly:%s"
                    % (self.config['USER'], request, kwargs, primaryOnly, backupOnly))
        self.kwargs = kwargs

        # appliances in the query
        # appliances = self.config['MGMT']

        # appliances in order, fallback to unordered if this is the early calls to determine order
        try:
            appliances = [self.primaryRouter, self.backupRouter]
        except AttributeError, e:
            appliances = self.config['MGMT']

        # change appliances based on boolean conditions
        if len(appliances) > 1:
            if primaryOnly and backupOnly:
                appliances = [self.primaryRouter, self.backupRouter]
                logger.info("Forced Both: %s, request: %s" % (appliances, request))
            elif primaryOnly and not backupOnly:
                appliances = [self.primaryRouter]
                logger.info("Primary: %s, request: %s" % (appliances, request))
            elif backupOnly and not primaryOnly:
                appliances = [self.backupRouter]
                logger.info("Backup: %s, request: %s" % (appliances, request))
            else:
                logger.info("Both: %s, request: %s" % (appliances, request))
        else:
            logger.info("Only one appliance in configuration, running in non-HA mode")
            appliances = [self.primaryRouter]

        try:
            data = OrderedDict()
            codes = OrderedDict()
            for host in appliances:
                logger.debug("Querying host: %s" % host)
                url = host
                request_headers = generateRequestHeaders(
                    default_headers={
                        'Content-type': 'text/xml',
                        'Accept': 'text/xml'
                    },
                    auth_headers=generateBasicAuthHeader(self.config['USER'], self.config['PASS'])
                )
                logger.debug("request_headers: %s" % request_headers)
                (response, response_headers, code) = httpRequest(url, method='POST', headers=request_headers,
                                                                 fields=request, timeout=5000,
                                                                 verifySsl=self.config['VERIFY_SSL'])
                logger.debug("response: %s" % response)
                data[host] = response
                logger.debug("code: %s" % code)
                codes[host] = code
            logger.debug(data)

            for k in data:
                thisreply = None
                try:
                    thisreply = xml2dict.parse(data[k])
                    if thisreply['rpc-reply'].has_key('execute-result'):
                        if thisreply['rpc-reply']['execute-result']['@code'] != 'ok':
                            logger.warn("Device: %s: %s %s" % (k, thisreply['rpc-reply']['execute-result']['@code'],
                                                               "Request that failed: %s" % request))
                            logger.warn("Device: %s: %s: %s" % (k, thisreply['rpc-reply']['execute-result']['@code'],
                                                                "Reply from appliance: %s" %
                                                                thisreply['rpc-reply']['execute-result']['@reason']))
                        else:
                            logger.debug("Device: %s: %s" % (k, thisreply['rpc-reply']['execute-result']['@code']))
                        logger.debug("Device: %s: %s" % (k, thisreply))
                    else:
                        logger.debug("no execute-result in response. Device: %s" % k)
                except Exception, e:
                    logger.error("Error decoding response from appliance")
                    logger.error("Response Codes: %s" % codes)
                    logger.error("Data Object: key: %s, data: %s " % (k, data))
                    logger.error(codes.items()[0][1])
                    if codes.items()[0][1] == 401:
                        raise LoginException("Username / Password failure")
                    raise  # (Exception("Appliance Communication Failure"))
            logger.debug("Returning Data from rest_call")
            return data, codes

        except Exception, e:
            traceback.print_exc()
            logger.warn("Solace Error %s" % e)
            raise

    def get_redundancy(self):
        """
        Return redundancy status

        Example:
            >>> api = SolaceAPI("dev")
            >>> api.get_redundancy()[0]['rpc-reply']['rpc']['show']['redundancy']['config-status']
            u'Enabled'

        """
        request = SolaceXMLBuilder(version=self.version)
        request.show.redundancy
        return self.rpc(str(request))

    def get_memory(self):
        """ Returns the Memory Usage

        Example of request XML
        <rpc semp-version="soltr/6_0">
            <show>
                <memory></memory>
            </show>
        </rpc>
        """
        request = SolaceXMLBuilder(version=self.version)
        request.show.memory
        return self.rpc(str(request))

    def get_message_spool(self, **kwargs):
        """ show message spool
        :param version:
        """
        request = SolaceXMLBuilder("Getting message spool status", version=self.version)
        request.show.message_spool
        return self.rpc(str(request), **kwargs)

    def __detect_state(self, response):
        """ TODO: is this sufficient to detect cluster state? """
        message_spool = response['rpc-reply']['rpc']['show']['message-spool']['message-spool-info']
        if message_spool['operational-status'] == 'AD-Active':
            return 'Primary'
        elif message_spool['operational-status'] == 'AD-Standby':
            return 'Backup'
        else:
            raise Exception("Unknown message-spool operational-status '%s'" % message_spool['operational-status'])

    def rpc(self, xml, allowfail=False, primaryOnly=False, backupOnly=False, xml_response=False, **kwargs):
        """
        Execute a SEMP command on the appliance(s), call with a string representation
        of a SolaceXMLBuilder instance.

        Args:
            xml(str): string representation of a SolaceXMLBuilder instance.
            allowFail(Optional(bool)): tollerate some types of errors from the
                appliance.
            primaryOnly(Optional(bool)): only execute on primary appliance.
            backupOnly(Optional(bool)): only execute on backup appliance.

        Returns:
            data response list as from appliances. Json-like data

        Example:
            >>> from libsolace.SolaceXMLBuilder import SolaceXMLBuilder
            >>> conn = SolaceAPI("dev")
            >>> conn.x = SolaceXMLBuilder(version = conn.version)
            >>> conn.x.show.version
            OrderedDict()
            >>> type(conn.rpc(str(conn.x)))
            <type 'list'>

        """

        logger.debug(type(xml))

        if type(xml) == type(None):
            logger.warn("Ignoring empty request")
            return

        elif isinstance(xml, PluginResponse):
            logger.info("Plugin Response")
            kwargs = xml.kwargs
            xml = xml.xml

        elif type(xml) == type(()):
            kwargs = xml[1]
            xml = xml[0]

        elif isinstance(xml, str):
            pass

        elif isinstance(xml, SolaceXMLBuilder):
            xml = str(xml)

        else:
            logger.warn("I dont recognize this type of rpc: %s type: %s" % (xml, type(xml)))
            raise Exception("Not a valid RPC argument")

        responses = None
        mywargs = kwargs
        logger.debug("Kwargs: %s" % mywargs)
        logger.info("Request SEMP: %s" % xml)
        logger.debug("primaryOnly: %s" % primaryOnly)
        logger.debug("backupOnly: %s" % backupOnly)

        if "primaryOnly" in mywargs:
            primaryOnly = mywargs.pop("primaryOnly")

        if "backupOnly" in mywargs:
            backupOnly = mywargs.pop("backupOnly")

        try:
            data = []
            responses, codes = self.__restcall(xml, primaryOnly=primaryOnly, backupOnly=backupOnly, **mywargs)
            if xml_response:
                return responses
            for k in responses:
                response = xml2dict.parse(responses[k])
                logger.debug("Response: %s" % response)
                response['HOST'] = k
                if not allowfail:
                    if 'parse-error' in response['rpc-reply']:
                        raise Exception(str(response))
                    elif 'permission-error' in response['rpc-reply']:
                        if self.testmode:
                            logger.debug('tolerable permission error in test mode')
                        else:
                            logger.critical("Error occured, request was: %s" % xml)
                            raise Exception(str(response))
                    else:
                        data.append(response)
                else:
                    data.append(response)
            if len(data) is 1:
                data.append(None)
            return data
        except:
            logger.error("responses: %s" % responses)
            raise

    def manage(self, plugin_name, **kwargs):
        """
        Gets a plugin, configures it, then allows direct communication with it.

        Plugins are passed the kwargs directly if any are specified.

        Example:
            >>> api = SolaceAPI("dev")
            >>> p1 = api.manage("NullPlugin")
            >>> p1.some_method("foo", bar="baz")
            (('foo',), {'bar': 'baz'})
            >>> p2 = api.manage("NullPlugin", a="a")
            >>> p2.kwargs['a']
            'a'
        """

        plugin = libsolace.plugin_registry(plugin_name, **kwargs)
        logger.debug("Setting up the plugin instance with api and kwargs")
        return plugin(api=self, **kwargs)
