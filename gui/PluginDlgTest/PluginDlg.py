import sys
from PyQt4.QtGui import *
import ui_PluginDlg


class PluginForm(QDialog, ui_PluginDlg.Ui_Dialog):
    def __init__(self, text_to_show=None):
        super(PluginForm, self).__init__(parent=None)
        self.setupUi(self)
        if text_to_show:
            self.label.setText(text_to_show)


def main():
    app = QApplication(sys.argv)
    form = PluginForm('This is for test.')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
