import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QLineEdit()
        # 设置可以输入的最大字符数量
        widget.setMaxLength(10)
        # 设置预先填入的提示字符
        widget.setPlaceholderText("Enter your text")

        # 此signal在按下enter时触发
        widget.returnPressed.connect(self.return_pressed)
        # 此signal在选中的文本发生变化的时候触发
        widget.selectionChanged.connect(self.selection_changed)
        # 此signal在text发生变化时触发，并返回改变的文本
        widget.textChanged.connect(self.text_changed)
        # 此signal在进行编辑的时候触发，基本上和textChanged同时触发
        widget.textEdited.connect(self.text_edited)

        self.setCentralWidget(widget)

    def return_pressed(self):
        print("Return preseed!")
        self.centralWidget().setText("BOOM!")

    def selection_changed(self):
        print("Selection changed")
        print(self.centralWidget().selectedText())

    def text_changed(self, s):
        print("Text changed...")
        print(s)

    def text_edited(self, s):
        print("Text edited...")
        print(s)


app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
