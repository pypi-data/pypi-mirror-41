__author__ = 'Kegan Holtzhausen <Kegan.Holtzhausen@unibet.com>'

"""
The plugin system
"""

import functools
import logging
from collections import OrderedDict

from libsolace.util import get_calling_module

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


class PluginClass(type):
    """This is a metaclass for construction only, see Plugin rather"""

    def __new__(cls, clsname, bases, dct):
        new_object = super(PluginClass, cls).__new__(cls, clsname, bases, dct)
        return new_object


class Plugin(object):
    """This is the plugin core object where all plugins should extend from and register too.

    Plugin Example:

    .. doctest::
        :options: +SKIP

        >>> import pprint
        >>> import libsolace
        >>> from libsolace.plugin import Plugin
        >>> @libsolace.plugin_registry.register
        >>> class Bar(Plugin):
        >>>     plugin_name = "BarPlugin"
        >>>     def __init__(self):
        >>>         pass
        >>>     # Instance methods work!
        >>>     def hello(self, name):
        >>>         print("Hello %s from %s" % (name, self))
        >>>     # Static methods work too!
        >>>     @staticmethod
        >>>     def gbye():
        >>>         print("Cheers!")
        >>> libsolace.plugin_registry('BarPlugin').hello("dude")
        >>> libsolace.plugin_registry('BarPlugin').gbye()
        >>> pprint.pprint(dir(libsolace.plugin_registry('BarPlugin')))

    Plugin Instantiation:

    >>> from libsolace.settingsloader import settings
    >>> from libsolace.SolaceAPI import SolaceAPI
    >>> api = SolaceAPI("dev")
    >>> my_plugin = api.manage("NullPlugin")
    >>> type(my_plugin)
    <class 'libsolace.items.NullPlugin.NullPlugin'>

    Direct Instantiation:

    >>> from libsolace.settingsloader import settings
    >>> import libsolace
    >>> my_clazz = libsolace.plugin_registry("NullPlugin", settings=settings)
    >>> my_instance = my_clazz(settings=settings)

    """
    __metaclass__ = PluginClass
    plugins = []
    plugins_dict = OrderedDict()
    plugin_name = "Plugin"
    """ the plugin's name, override this in the derived class!"""
    exists = False

    def __init__(self, *args, **kwargs):
        logger.debug("Plugin Init: %s, %s" % (args, kwargs))

    def register(self, object_class, *args, **kwargs):
        """
        Registers a object with the plugin registry, typically used as a decorator.

        :param object_class: the class to register as a plugin

        Example:
            .. doctest::
                :options: +SKIP

                >>> @libsolace.plugin_registry.register
                >>> class Foo(Plugin)
                >>> ...

        """
        logger.info("Registering Plugin id: %s from class: %s " % (object_class.plugin_name, object_class))
        o = object_class
        self.plugins.append(o)
        self.plugins_dict[object_class.plugin_name] = o

        def _d(fn):
            logger.info("CALL CALL CALL CALL CALL CALL")
            return functools.update_wrapper(object_class(fn), fn)

        functools.update_wrapper(_d, object_class)
        return _d

    def __call__(self, *args, **kwargs):
        """
        When you call the registry with the name of a plugin eg: 'NullPlugin', as the first arg, this returns the class
        from the plugin_registry. You can then instantiate the class in any way you need to.

        Example
        >>> import libsolace
        >>> from libsolace.plugin import Plugin
        >>> a = libsolace.plugin_registry("NullPlugin")
        >>> type(a)
        ""


        :param args: name of Plugin to return
        :param kwargs:
        :return: class
        """

        try:
            module = get_calling_module(point=2)
        except:
            module = "Unknown"

        try:
            module_parent = get_calling_module(point=3)
        except:
            module_parent = "Unknown"

        logger.debug(self.plugins_dict)
        logger.info("Module %s->%s->%s" % (module_parent, module, args[0]))

        logger.debug("Plugin Request: args: %s, kwargs: %s" % (args, kwargs))
        try:
            logger.debug("Class: %s" % self.plugins_dict[args[0]])
            return self.plugins_dict[args[0]]
        except:
            logger.warn("No plugin named: %s found, available plugins are: %s" % (args[0], self.plugins_dict))
            logger.warn(
                "Please check the plugin is listed in the yaml config and that you have @libsolace.plugin_registry.register in the class")
            raise

    def set_exists(self, state):
        """set_exists is used as caching in order to cut down on SEMP queries to validate existence of items. For example,
        if you create a new VPN in "batch" mode, After the "create-vpn" XML is generated, set_exists is set to True so
        subsequent requests decorated with the `only_if_exists` will function correctly since set_exists states that the
        object will exist.

        :param state: the existence state of the object
        :type state: bool
        :return:
        """
        module = get_calling_module(point=3)
        logger.info("Calling module: %s, Setting Exists bit: %s" % (module, state))
        self.exists = state


class PluginResponse(object):
    """
    Encapsulating class for holding SEMP requests and their accompanying kwargs.

    Example:

    >>> request = PluginResponse('<rpc semp-version="soltr/7_1_1"><show><memory/></show></rpc>', primaryOnly=True)
    >>> request.xml
    '<rpc semp-version="soltr/7_1_1"><show><memory/></show></rpc>'

    """

    def __init__(self, xml, **kwargs):
        self.xml = xml
        """ the XML """
        self.kwargs = kwargs
        """ the kwargs """
