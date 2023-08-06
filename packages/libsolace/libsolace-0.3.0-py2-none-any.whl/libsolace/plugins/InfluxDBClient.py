"""
a plugin for sending metrics to InfluxDB
"""

import logging
import sys
from time import strftime, gmtime

try:
    from influxdb import InfluxDBClient as InfluxDBClientConnector
except ImportError, e:
    print("You need to install influxdb")
    sys.exit(1)

import libsolace
from libsolace.plugin import Plugin

__doc__ = """
Simple influxdb client that can send metrics to influx.

.. code-block:: none

    PLUGINS:
        ...
        - libsolace.plugins.InfluxDBClient
        ...

    INFLUXDB_HOST: localhost
    INFLUXDB_PORT: 8086
    INFLUXDB_USER: user
    INFLUXDB_PASS: pass
    INFLUXDB_DB: solace

"""

logger = logging.getLogger(__name__)
logger.addHandler(logging.NullHandler())


def get_time():
    """ consistent time formatting

    :return: time
    """
    return strftime("%Y-%m-%dT%H:%M:%SZ", gmtime())


def flatten_json(y):
    """
    flattens a json object combining key names to be {parent-child-leaf: value}

    :param y:
    :return:
    """
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        else:
            try:
                out[str(name[:-1])] = long(x)
            except Exception, e:
                pass

    flatten(y)
    return out


@libsolace.plugin_registry.register
class InfluxDBClient(Plugin):
    """
    Simple influxdb client plugin for libsolace

    Example:

    .. doctest::
        :options: +SKIP

        >>> from libsolace.settingsloader import settings
        >>> import libsolace
        >>> metrics_class = libsolace.plugin_registry('InfluxDBClient', settings=settings)
        >>> metrics = metrics_class(settings=settings)

    """
    plugin_name = "InfluxDBClient"

    def __init__(self, settings=None, **kwargs):
        logger.debug("Configuring with settings: %s" % settings)
        self.settings = settings  # type: dict
        self.influxdb_host = settings.get("INFLUXDB_HOST", "defiant")
        self.influxdb_port = settings.get("INFLUXDB_PORT", 8086)
        self.influxdb_user = settings.get("INFLUXDB_USER", "root")
        self.influxdb_pass = settings.get("INFLUXDB_PASS", "root")
        self.influxdb_db = settings.get("INFLUXDB_DB", "solace")

        # connect
        self.client = InfluxDBClientConnector(self.influxdb_host,
                                              self.influxdb_port,
                                              self.influxdb_user,
                                              self.influxdb_pass,
                                              self.influxdb_db)

    def send(self, measurement, data, **tags):
        """
        Sends the metrics to influxdb.

        Examples:

        .. doctest::
            :options: +SKIP

            >>> from libsolace.settingsloader import settings
            >>> import libsolace
            >>> metrics_class = libsolace.plugin_registry('InfluxDBClient', settings=settings)
            >>> metrics = metrics_class(settings=settings)
            >>> metrics.send('http-metrics', {"key": 10, "key2": 12}, environment='prod', host='foo')
            >>> metrics.send("test", {"key": 2}, host="test")

        :param data: a json object of keys and values. will be flattened!
        :param measurement:
        """

        json_body = [{
            "measurement": measurement,
            "tags": {},
            "time": get_time(),
            "fields": flatten_json(data)
        }]

        for tag in tags:
            json_body[0]['tags'][tag] = tags[tag]

        try:
            self.client.write_points(json_body)
        except Exception, e:
            logger.error(e.message)
            logger.error("Unable to write to influxdb")
