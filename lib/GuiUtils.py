from PyQt4.QtGui import *
# from PyQt4.QtCore import *


def attach_one_form_to_another(one_form, another_form):
    """
    This function is made static. It will set one form to the child of
    another one, and show it as vertical layout in that parent form.
    :param one_form: the child
    :param another_form: the parent
    :return:
    """
    one_form.setParent(another_form)
    if isinstance(another_form.layout(), type(None)):
        layout = QVBoxLayout(another_form)
        layout.setMargin(0)
    else:
        layout = another_form.layout()
        layout.setMargin(0)
        for index in range(layout.count()):
            layout_item = layout.itemAt(index)
            layout.removeItem(layout_item)
            layout_widget = layout_item.widget()
            if not isinstance(layout_widget, type(None)):
                layout_widget.setShown(False)
    layout.addWidget(one_form)
    one_form.setShown(True)
