#! /tool/pandora64/bin/python2.7.3
import os
import sys
from yapsy.PluginManager import PluginManager
from PyQt4.QtGui import *
from core import MainForm
from plugins.Categories import TabularPlugin

import logging
ch = logging.StreamHandler()
log = logging.getLogger('yapsy')
log.addHandler(ch)


def main():
    app = QApplication(sys.argv)
    form = MainForm()

    # load plugins
    manager = PluginManager(categories_filter={'TabularPlugins': TabularPlugin})
    manager.setPluginPlaces(['../plugins'])

    manager.collectPlugins()
    print manager.getPluginsOfCategory('TabularPlugins')
    for plugin in manager.getPluginsOfCategory('TabularPlugins'):
        plugin.plugin_object.print_name()
        print type(plugin)
        form.add_tabular_plugin(plugin=plugin.plugin_object)

    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
