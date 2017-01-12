from PyQt4.QtGui import *
from PyQt4.QtCore import *


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


def action_generator(parent, action_info):
    """
    This function take action_info dict, and return a QAction instance.
    :param action_info: is a dictionary that describes an action.
    :return: QAction
    """
    action = QAction(parent)
    for each_key in action_info:
        each_val = action_info[each_key]
        if each_key == 'description':
            action.setText(each_val)
        elif each_key == 'function_handle':
            parent.connect(action, SIGNAL('triggered()'), each_val)
        elif each_key == 'icon':
            action.setIcon(QIcon(each_val))
        elif each_key == 'shortcut':  # shortcut val should be of QKeySequence type.
            action.setShortcut(each_val)
    return action
