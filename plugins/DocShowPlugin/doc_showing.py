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

    def print_name(self):
        print 'This is plugin: #%s#' % self.name
