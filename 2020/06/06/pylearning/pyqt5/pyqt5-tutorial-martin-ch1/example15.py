from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        widget1 = QCheckBox()
        # 这个使用boolean来设置是否选中
        # widget1.setCheckted(True)
        # 这个使用flag来设置状态，有3种
        widget1.setCheckState(Qt.Checked)  # 设置状态是checked
        # 可以使用此方法来选择第三种状态
        # widget1.setTristate(True)

        # 将state改变的flag连接到slot，传递给slot的实际上就是flag
        widget1.stateChanged.connect(self.show_state)

        self.setCentralWidget(widget1)

    def show_state(self, s):
        # 打印一下flag
        print(s == Qt.Checked)
        print(s)

app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
