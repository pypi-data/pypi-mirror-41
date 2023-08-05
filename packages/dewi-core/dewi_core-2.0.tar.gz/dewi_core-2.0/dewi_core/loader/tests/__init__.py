# Copyright 2015-2019 Laszlo Attila Toth
# Distributed under the terms of the GNU Lesser General Public License v3
import dewi_core.testcase

from dewi_core.loader.loader import PluginLoader, PluginLoaderError


class TestLoadable(dewi_core.testcase.TestCase):

    def assert_loadable(self, plugin_name: str):
        try:
            loader = PluginLoader()
            loader.load({plugin_name})
        except PluginLoaderError as exc:
            raise AssertionError("Unable to load plugin '{}'; reason='{}'".format(plugin_name, str(exc)))
