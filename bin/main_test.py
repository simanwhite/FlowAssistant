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
    for plugin in manager.getPluginsOfCategory('TabularPlugins'):
        print 'Adding plugin: %s' % plugin.plugin_object.name
        form.add_tabular_plugin(plugin_object=plugin.plugin_object)

    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
