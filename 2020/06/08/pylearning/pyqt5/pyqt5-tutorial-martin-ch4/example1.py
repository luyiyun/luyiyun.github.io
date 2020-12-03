import sys
from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        # 创建一个label，并将其放到整个窗口中
        self.label = QtWidgets.QLabel()
        self.setCentralWidget(self.label)
        # 创建一个画布，并将这个画布放到label上
        canvas = QtGui.QPixmap(400, 300)
        # 原教程中没有介绍，新创建的Pixmap对象是null的，需要先给底色，可以使用fill(QColor(.))来完成，其默认是白色
        canvas.fill()
        self.label.setPixmap(canvas)
        # 在画布上画一些东西
        self.draw_something()

    def draw_something(self):
        # 对一个QPixmap对象操作，需要使用QPainter
        painter = QtGui.QPainter(self.label.pixmap())
        painter.drawLine(10, 10, 300, 200)
        painter.end()


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
