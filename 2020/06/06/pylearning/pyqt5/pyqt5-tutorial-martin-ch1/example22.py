import sys

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Color(QWidget):
    """
    一个自定义的类，用于展示布局
    """
    def __init__(self, color, *args, **kwargs):
        super(Color, self).__init__(*args, **kwargs)
        # 开启后，其自动使用window color来填充背景
        self.setAutoFillBackground(True)
        # 得到调色板，默认是global desktop palette。调色板中记录了
        #   widgets的各种元素的颜色，可以看做是widgets颜色设置的一组
        #   集合
        palette = self.palette()
        # 将调色板中窗口颜色改变，需要使用QColor类
        palette.setColor(QPalette.Window, QColor(color))
        # 将这组设置更新到当前的widgets中
        self.setPalette(palette)


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        layout = QGridLayout()

        layout.addWidget(Color("red"), 0, 0)
        layout.addWidget(Color("green"), 1, 0)
        layout.addWidget(Color("blue"), 1, 1)
        layout.addWidget(Color("purple"), 2, 1)

        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
