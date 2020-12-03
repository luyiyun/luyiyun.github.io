from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget1 = QLabel("Hello")  # 可以直接传入文字
        widget1.setText("Hello world")  # 通过此方法改变文字的内容
        # 以下是改变文字样式的方法
        font = widget1.font()
        font.setPointSize(30)
        widget1.setFont(font)
        # 改变文字的对齐位置
        widget1.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        widget2 = QLabel("")
        widget2.setPixmap(QPixmap("space.jpg"))
        widget2.setScaledContents(True)

        layout = QVBoxLayout()
        layout.addWidget(widget1)
        layout.addWidget(widget2)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
