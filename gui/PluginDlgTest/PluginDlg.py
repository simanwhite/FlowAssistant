import sys
from PyQt4.QtGui import *
import ui_PluginDlg


class PluginForm(QDialog, ui_PluginDlg.Ui_Dialog):
    def __init__(self):
        super(PluginForm, self).__init__(parent=None)
        self.setupUi(self)


def main():
    app = QApplication(sys.argv)
    form = PluginForm()
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
