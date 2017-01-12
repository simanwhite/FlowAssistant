import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.MainWindow import ui_MainWindow

from lib.GuiUtils import *


class MainForm(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__(parent=None)
        self.setupUi(self)
        self._action_group_dict = {}

    def add_tabular_plugin(self, plugin_object):
        # add tabular in main window
        tab = QWidget()
        icon = QIcon(plugin_object.icon)
        self.tabWidget.addTab(tab, icon, plugin_object.name)

        # add customized actions in menu -> Plugins
        plugin_menu = QMenu(self.menuPlugins)
        plugin_menu.setTitle(plugin_object.name)
        plugin_action_group = QActionGroup(self)
        try:
            for each_action_info in plugin_object.action_info_lst:
                plugin_action = action_generator(self, each_action_info)
                plugin_menu.addAction(plugin_action)
                self.menuPlugins.addAction(plugin_menu.menuAction())
                plugin_action_group.addAction(plugin_action)
            self._action_group_dict[plugin_object.name] = plugin_action_group
        except AttributeError:
            print 'No action to add for plugin: %s' % plugin_object.name

        # add customized gui
        try:
            attach_one_form_to_another(plugin_object.form, tab)
        except AttributeError:
            print 'No form to add for plugin: %s' % plugin_object.name

    def _on_current_tab_change(self):
        # take care of the action's disable/enable when current tabular changed.
        # First set all tabs' action_group disabled
        for tab_index in range(self.tabWidget.count()):
            tab_name = str(self.tabWidget.tabText(tab_index))
            self._action_group_dict[tab_name].setDisabled(True)
        # Set current tabular action_group enabled
        current_index = self.tabWidget.currentIndex()
        tab_name = str(self.tabWidget.tabText(current_index))
        self._action_group_dict[tab_name].setDisabled(False)

    def _connect_signals(self):
        self.connect(self.tabWidget, SIGNAL('currentChanged (int)'), self._on_current_tab_change)

    def initialize_main_form(self):
        self._on_current_tab_change()  # update tab change when GUI is created
        self._connect_signals()