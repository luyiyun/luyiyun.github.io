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

        tabs = QTabWidget()
        tabs.setDocumentMode(True)
        tabs.setTabPosition(QTabWidget.East)  # 控制标签所在的位置，右侧
        tabs.setMovable(True)

        cs = ["red", "green", "blue", "yellow"]
        for n, color in enumerate(cs):
            tabs.addTab(Color(color), color)

        self.setCentralWidget(tabs)


app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
