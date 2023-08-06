"""

Example of using a YAML document to provision solace

"""

import logging

import yaml

import libsolace
from libsolace.plugin import Plugin

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


@libsolace.plugin_registry.register
class YAMLClient(Plugin):
    # the name used to call the plugin
    plugin_name = "YAMLClient"

    def __init__(self, settings=None, **kwargs):
        """
        Example:
        from libsolace.settingsloader import settings
        import libsolace
        clazz = libsolace.plugin_registry('YAMLClient', settings=settings)
        yaml_client = clazz(settings=settings)
        yaml_client.get_vpns_by_owner("SolaceTest", environment="au")

        :param settings:
        :param kwargs:
        :return:
        """
        logger.debug("Configuring with settings: %s" % settings)
        self.settings = settings  # type: dict
        self.file = settings["CMDB_FILE"]
        stream = open(self.file, 'r')
        self.data = yaml.load(stream)

    def get_vpns_by_owner(self, *args, **kwargs):
        """
        return a LIST of vpns groups by some "owner", each VPN contains final config,
        so all environment overrides and that should be taken care of here!
        :param environment: the name of the environment
        """

        owner_name = args[0]  # type: str
        vpns = self.data.get("VPNS").get(owner_name)

        return vpns

    def get_users_of_vpn(self, *args, **kwargs):
        """
        Just return a list of users for a VPN
        """

        vpn_name = args[0]  # type: str
        users = self.data.get("USERS").get(vpn_name)

        # iterate over users copying environment overrides where applicable
        if users is not None:
            for user in users:
                if user.has_key('environment'):
                    e = user.get("environment").get(kwargs.get("environment"))
                    if e is not None:
                        for k, v in e.items():
                            user[k] = v

        return users

    def get_queues_of_vpn(self, *args, **kwargs):
        """
        As with VPN, all configs should be finalized before returned.
        """

        vpn_name = args[0]  # type: str

        queues = self.data.get("QUEUES").get(vpn_name)

        if queues is not None:
            for queue in queues:
                if queue.has_key('environment'):
                    e = queue.get("environment").get(kwargs.get("environment"))
                    logger.info("qoverride: %s" % e)
                    if e is not None:
                        for k, v in e.items():
                            queue['queue_config'][k] = v

        return queues
