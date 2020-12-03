import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QListWidget()
        # 增加可选元素
        widget.addItems(["one", "two", "Three"])

        widget.currentItemChanged.connect(self.index_changed)
        widget.currentTextChanged.connect(self.text_changed)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        # 这里传入的不是index，而是一个QListItem对象
        print(i.text())

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
