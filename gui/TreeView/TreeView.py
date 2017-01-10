import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_TreeView


class TreeViewForm(QTreeView, ui_TreeView.Ui_Frame):
    def __init__(self, model, root_index=None):
        super(TreeViewForm, self).__init__(parent=None)
        self.setupUi(self)
        self.treeView.setModel(model)
        if isinstance(root_index, type(QModelIndex())):
            self.treeView.setRootIndex(root_index)


def main():
    app = QApplication(sys.argv)
    model = QDirModel()
    form = TreeView(model, model.index('C:\\'))
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()



