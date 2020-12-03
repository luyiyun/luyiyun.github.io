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

        pagelayout = QVBoxLayout()
        button_layout = QHBoxLayout()
        layout = QStackedLayout()

        pagelayout.addLayout(button_layout)
        pagelayout.addLayout(layout)

        cs = ["red", "green", "blue", "yellow"]
        for n, color in enumerate(cs):
            btn = QPushButton(color)
            btn.pressed.connect(lambda n=n: layout.setCurrentIndex(n))
            # 这里使用了python的一个技巧。这里将index设为lambda参数的默认值，则其会被缓存，
            #   不然，所有的这四个lambda里的n都只会是黄色
            button_layout.addWidget(btn)
            layout.addWidget(Color(color))

        widget = QWidget()
        widget.setLayout(pagelayout)
        self.setCentralWidget(widget)


app = QApplication(sys.argv)
win = MainWindow()
win.show()

app.exec_()
