import sys

from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt


# 这里使用面向对象的方法
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # Qt namespace中有大量的特征用于自定义widget的行为，类似常量
        label.setAlignment(Qt.AlignCenter)

        # 将widget放入window的中央，默认widget将填满整个window
        self.setCentralWidget(label)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
