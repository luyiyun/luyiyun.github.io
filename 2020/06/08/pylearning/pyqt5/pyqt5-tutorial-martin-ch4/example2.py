import sys
import random
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


COLORS = [
    # 17 undertones https://lospec.com/palette-list/17undertones
    '#000000', '#141923', '#414168', '#3a7fa7', '#35e3e3', '#8fd970',
    '#5ebb49', '#458352', '#dcd37b', '#fffee5', '#ffd035', '#cc9245',
    '#a15c3e', '#a42f3b', '#f45b7a', '#c24998', '#81588d', '#bcb0c2',
    '#ffffff',
]


class QPaletteButton(QtWidgets.QPushButton):
    """
    一个自定义按钮，背景颜色代表其储存的颜色类别，
    """
    def __init__(self, color):
        super().__init__()
        self.setFixedSize(QtCore.QSize(24, 24))
        self.color = color
        self.setStyleSheet("background-color: %s" % color)
        # self.setCheckable(True)  # 有按下的效果


class Canvas(QtWidgets.QLabel):
    """
    自定义画布，实际上就是一个带有pixmap的label。
    可以侦测鼠标的移动从而进行绘制
    储存有当前画笔的颜色，改变当前画笔的颜色使用set_pen_color方法
    """
    def __init__(self):
        super().__init__()
        pixmap = QtGui.QPixmap(600, 300)
        pixmap.fill()
        self.setPixmap(pixmap)

        self.last_x, self.last_y = None, None
        self.pen_color = QtGui.QColor("#000000")
        self.pen_type = 'pen'

    def set_pen_color(self, c):
        self.pen_color = QtGui.QColor(c)

    def mouseMoveEvent(self, e):
        painter = QtGui.QPainter(self.pixmap())
        p = painter.pen()
        p.setColor(self.pen_color)
        if self.pen_type == "pen":
            if self.last_x is None:  # First event.
                # 当我们按下鼠标的一刻，会触发该方法，此时last_x和last_y都是None
                #   所以先记录一下当前的鼠标位置
                self.last_x = e.x()
                self.last_y = e.y()
                return  # Ignore the first time.

            # 当我们继续移动鼠标，技术触发该方法，此时，会执行下面的内容绘制线条并
            #   更新last_x和last_y
            p.setWidth(4)
            painter.setPen(p)
            # 这里使用line，因为如果是point的话，绘制的速度会跟不上鼠标移动的速度，
            #   从而出现断开的状态。如果是line的话就没有这个问题，但线条会比较毛糙。
            painter.drawLine(self.last_x, self.last_y, e.x(), e.y())
            painter.end()
            # 绘制图像的过程发生在show之后，所以如果想要把绘制的内容打印到屏幕上，
            #   需要使用update方法
            self.update()

            # Update the origin for next time.
            self.last_x = e.x()
            self.last_y = e.y()
        elif self.pen_type == "spray":
            p.setWidth(1)
            painter.setPen(p)
            for n in range(100):
                xo = random.gauss(0, 10)
                yo = random.gauss(0, 10)
                painter.drawPoint(e.x() + xo, e.y() + yo)

            self.update()

    def mouseReleaseEvent(self, e):
        # 当我们松开鼠标的时候，将last_x和last_y抹除
        self.last_x = None
        self.last_y = None


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()

        self.canvas = Canvas()

        w = QtWidgets.QWidget()
        l = QtWidgets.QVBoxLayout()
        w.setLayout(l)
        l.addWidget(self.canvas)

        palette = QtWidgets.QHBoxLayout()
        self.add_palette_buttons(palette)
        l.addLayout(palette)

        self.setCentralWidget(w)

    def add_palette_buttons(self, layout):
        # 为每个颜色创建一个按钮，并设置当按下按钮的时候，更改画布中的画笔颜色
        #   然后把所有的按钮防止到布局中
        for c in COLORS:
            b = QPaletteButton(c)
            b.pressed.connect(lambda c=c: self.canvas.set_pen_color(c))
            layout.addWidget(b)


app = QtWidgets.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
