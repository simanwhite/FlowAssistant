# ComboFrame is a window that takes multiple dialogs or frames into its
# combo box, and shows the one that selected.

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_ComboFrame

from lib.GuiUtils import attach_one_form_to_another


class ComboFrame(QFrame, ui_ComboFrame.Ui_Frame):
    def __init__(self, form_list=None):
        super(ComboFrame, self).__init__(parent=None)
        self._current_form = None  # to store the form instance which is showing now
        self._form_map = {}  # to store {form_title: form}
        self.setupUi(self)
        self.connect(self.comboBox, SIGNAL('currentIndexChanged(int)'), self.combobox_change_slot)
        if form_list:
            self.load_form_list(form_list)

    def load_form_list(self, form_list):
        """
        Load the dialogs or frames to combo box.
        :param form_list: a list of Qt widgets or windows instances
        :return:
        """
        if not form_list:
            print 'No form to load in combo frame'
            return
        for each_form in form_list:
            title = str(each_form.windowTitle())
            if title not in self._form_map:
                self._form_map[title] = each_form
                self.comboBox.addItem(title)
        self.set_current_form(str(self.comboBox.currentText()))

    def set_current_form(self, title):
        form_to_show = self._form_map[title]
        attach_one_form_to_another(form_to_show, self.frame)

    def combobox_change_slot(self):
        new_text = str(self.comboBox.currentText())
        self.set_current_form(new_text)


def main():
    from gui.PluginDlgTest.PluginDlg import PluginForm
    app = QApplication(sys.argv)
    f1 = PluginForm('Test form 1')
    f1.setWindowTitle('Form1')
    f2 = PluginForm('Test form 2')
    f2.setWindowTitle('Form2')
    f3 = PluginForm('Test form 3')
    f3.setWindowTitle('Form3')
    form = ComboFrame(form_list=[f1, f2, f3])
    # form.load_form_list([f1, f2, f3])
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
