import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from plugins.Categories import *
from gui.WebView import WebView


class PluginOne(TabularPlugin):
    name = 'Tabular Plugin 1'
    _this_directory = os.path.dirname(__file__)
    icon = '%s/res/bottom-top.gif' % _this_directory
    form = WebView.WebViewForm('http://twiki.amd.com/twiki/bin/view/DesignCAD/CVSRDCTaskDFP')

    def __init__(self):
        super(PluginOne, self).__init__()
        print 'init of tabular plugin 1'

        # actions in action dictionary will be added in Plugins menu bar
        self.action_info_lst = [
            # (description, function_handle, icon, key-shortcut),
            {
                'description': 'Print Name',
                'function_handle': self.print_name,
                'icon': '../res/tb_back.gif',
                'shortcut': QKeySequence.Print,
            },
        ]

    @staticmethod
    def print_name():
        print 'This is Tabular Plugin 1!'
