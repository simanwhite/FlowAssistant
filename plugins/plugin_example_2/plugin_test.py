import os
from plugins.Categories import *
from gui.WebView import WebView


class PluginOne(TabularPlugin):
    name = 'Tabular Plugin 2'
    _this_directory = os.path.dirname(__file__)
    icon = '%s/res/bottom-top.gif' % _this_directory
    form = WebView.WebViewForm('http://twiki.amd.com/twiki/bin/view/DesignCAD/CVSRDCTaskDFP')

    def __init__(self):
        super(PluginOne, self).__init__()
        print 'init of tabular plugin 1'

        # actions in action dictionary will be added in Plugins menu bar
        self.action_lst = [
            # (Description, function handle, action icon),
            (
                'Print Plugin Name',
                self.print_name,
                '%s/res/bottom-top.gif' % self._this_directory
            ),
            (
                'Go back',
                self.form.webView.back,
                '../res/tb_back.gif'
            ),
            (
                'Go forward',
                self.form.webView.forward,
                '../res/tb_forward.gif'
            )
        ]

    @staticmethod
    def print_name():
        print 'This is Tabular Plugin 2!'
