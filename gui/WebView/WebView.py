import sys
import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
import ui_WebView


class WebViewForm(QFrame, ui_WebView.Ui_Frame):
    def __init__(self, url):
        super(WebViewForm, self).__init__(parent=None)
        self.setupUi(self)
        self.webView.setHtml('<h3>Loading...</h3>')
        self.url = QUrl(url)
        # noinspection PyTypeChecker,PyCallByClass
        self.set_url(url)

    def load_url(self):
        self.webView.load(self.url)

    def set_url(self, url):
        self.webView.setHtml('<h3>Loading...</h3>')
        if os.path.isfile(url):
            url = 'file:///' + url
        url = url.replace(os.path.sep, '/')
        self.url = QUrl(url)
        # noinspection PyTypeChecker,PyCallByClass
        QTimer.singleShot(0, self.load_url)


def main():
    app = QApplication(sys.argv)
    form = WebViewForm(r'D:/working/PlayGround/FlowAssistant/res/doc_test/work projects.html')
    form.show()
    app.exec_()


if __name__ == '__main__':
    main()
