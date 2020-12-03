import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


# 这里使用面向对象的方法
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        # 使用connect方法会将signal连接到对应的slot（func）上去，一旦signal
        #   触发（window title改变），则会使用这些funcs
        # 我们可以一次连接多个这样的func，当signal触发时，这些func都会运行
        self.windowTitleChanged.connect(self.onWindowTitleChange)
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))
        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))

        # 在这里设置title的时候会触发上面的func一次
        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # Qt namespace中有大量的特征用于自定义widget的行为，类似常量
        label.setAlignment(Qt.AlignCenter)

        # 将widget放入window的中央，默认widget将填满整个window
        self.setCentralWidget(label)

    def onWindowTitleChange(self, x):
        # 这个x是signal触发是排出的内容，具体要查看文档
        print(x)

    def my_custom_fn(self, a="Hello", b=5):
        print(a, b)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
