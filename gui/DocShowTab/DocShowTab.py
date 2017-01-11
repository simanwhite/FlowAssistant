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
        doc_root = os.path.abspath(doc_root)
        possible_url = os.path.join(doc_root, index_url)
        if os.path.exists(possible_url):
            index_url = possible_url
        print index_url
        self.web_view = WebView.WebViewForm(index_url)
        self.model = QDirModel()
        self.model.setNameFilters(['*.html'])  # Here set the supported file format for webview.
        self.model.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)
        doc_root = os.path.abspath(doc_root)
        self.tree_view = TreeView.TreeViewForm(self.model, self.model.index(doc_root))
        attach_one_form_to_another(self.tree_view, self.frame)
        attach_one_form_to_another(self.web_view, self.frame_2)
        for column_index in range(1, 4):  # Hide columns for size, data, etc.
            self.tree_view.treeView.setColumnHidden(column_index, True)
        self.connect(self.tree_view.treeView, SIGNAL('clicked(const QModelIndex&)'), self.update_web_view)

    def update_web_view(self):
        selected_index = self.tree_view.treeView.selectedIndexes()[0]
        file_path = unicode(self.model.filePath(selected_index))
        if os.path.isfile(file_path):
            self.web_view.set_url(file_path)


def main():
    app = QApplication(sys.argv)
    form = DocForm('work projects.html', '../../res/doc_test')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
