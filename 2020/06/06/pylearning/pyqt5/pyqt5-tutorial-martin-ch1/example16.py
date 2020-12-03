import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget = QComboBox()
        # 增加可选元素
        widget.addItems(["one", "two", "Three"])

        # 这个signal默认传给slot的是index
        widget.currentIndexChanged.connect(self.index_changed)
        # 可以通过此操作，使signal传递给slot的是上面的text
        widget.currentIndexChanged[str].connect(self.text_changed)
        # 此操作使得combo box可以输入文本
        widget.setEditable(True)
        # 这些输入的文本怎么处理
        # 当我们输入文本并按enter后，下面的设置会使这个文本选项称为新的Items
        #   并插入到Item列表的最后
        widget.setInsertPolicy(QComboBox.InsertAtBottom)
        # Items最多有5个
        widget.setMaxCount(5)

        self.setCentralWidget(widget)

    def index_changed(self, i):
        print(i)

    def text_changed(self, s):
        print(s)

app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
