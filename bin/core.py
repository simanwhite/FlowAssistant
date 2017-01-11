import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from gui.MainWindow import ui_MainWindow

from lib.GuiUtils import attach_one_form_to_another


class MainForm(QMainWindow, ui_MainWindow.Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__(parent=None)
        self.setupUi(self)

    def add_tabular_plugin(self, plugin):
        # add tabular in main window
        tab = QWidget()
        icon = QIcon(plugin.icon)
        self.tabWidget.addTab(tab, icon, plugin.name)

        # add customized actions in menu -> Plugins
        plugin_menu = QMenu(self.menuPlugins)
        plugin_menu.setTitle(plugin.name)
        for each_action in plugin.action_lst:
            # each_action is tuple like (Description, function handle, action icon)
            action_description = each_action[0]
            action_function = each_action[1]
            action_icon = QIcon(each_action[2])
            plugin_action = QAction(action_icon, action_description, self)
            self.connect(plugin_action, SIGNAL('triggered()'), action_function)
            # plugin_action.setText(each_action)
            plugin_menu.addAction(plugin_action)
            self.menuPlugins.addAction(plugin_menu.menuAction())

        # add customized gui
        try:
            attach_one_form_to_another(plugin.form, tab)
        except AttributeError:
            print 'ignore this err'


