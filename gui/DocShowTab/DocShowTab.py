import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_DocShowTab

from gui.WebView import WebView
from gui.TreeView import TreeView

from lib.GuiUtils import attach_one_form_to_another


class DocForm(QWidget, ui_DocShowTab.Ui_Dialog):
    def __init__(self, index_url, doc_root):
        super(DocForm, self).__init__(parent=None)
        self.setupUi(self)
        possible_url = os.path.join(doc_root, index_url)
        if os.path.exists(possible_url):
            index_url = possible_url
        web_view = WebView.WebViewForm(index_url)
        model = QDirModel()
        model.setNameFilters(['*.html'])
        model.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)
        doc_root = os.path.abspath(doc_root)
        tree_view = TreeView.TreeViewForm(model, model.index(doc_root))
        attach_one_form_to_another(tree_view, self.frame)
        attach_one_form_to_another(web_view, self.frame_2)
        for column_index in range(1, 4):  # Hide columns for size, data, etc.
            tree_view.treeView.setColumnHidden(column_index, True)

    def update_web_view(self):
        pass


def main():
    app = QApplication(sys.argv)
    form = DocForm('work projects.html', '../../res/doc_test')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
