import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.MainWindow import ui_MainWindow

from lib.GuiUtils import *


class MainForm(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__(parent=None)
        self.setupUi(self)

    def add_tabular_plugin(self, plugin_object):
        # add tabular in main window
        tab = QWidget()
        icon = QIcon(plugin_object.icon)
        self.tabWidget.addTab(tab, icon, plugin_object.name)

        # add customized actions in menu -> Plugins
        plugin_menu = QMenu(self.menuPlugins)
        plugin_menu.setTitle(plugin_object.name)
        try:
            for each_action_info in plugin_object.action_info_lst:
                plugin_action = action_generator(self, each_action_info)
                plugin_menu.addAction(plugin_action)
                self.menuPlugins.addAction(plugin_menu.menuAction())
        except AttributeError:
            print 'No action to add for plugin: %s' % plugin_object.name

        # add customized gui
        try:
            attach_one_form_to_another(plugin_object.form, tab)
        except AttributeError:
            print 'No form to add for plugin: %s' % plugin_object.name


