# Show flow docs in a Qt Creator like GUI.
import os
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from plugins.Categories import *
from gui.DocShowTab import DocShowTab


class DocShowPlugin(TabularPlugin):
    name = 'Documents'

    def __init__(self):
        super(DocShowPlugin, self).__init__()
        doc_root = os.path.abspath('../res/doc_test')
        print doc_root
        self.form = DocShowTab.DocForm('work projects.html', doc_root)

        # actions in action dictionary will be added in Plugins menu bar
        # of the MainWindow
        self.action_info_lst = [
            # (description, function_handle, icon, key-shortcut),
            {
                'description': 'Go back',
                'function_handle': self.form.web_view.webView.back,
                'icon': '../res/tb_back.gif',
                'shortcut': QKeySequence.Back,
            },
            {
                'description': 'Go forward',
                'function_handle': self.form.web_view.webView.forward,
                'icon': '../res/tb_forward.gif',
                'shortcut': QKeySequence.Forward,
            }
        ]

