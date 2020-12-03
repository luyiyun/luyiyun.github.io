import sys

import PyQt5.QtWidgets as qtw
from PyQt5.QtCore import Qt


# 这里使用面向对象的方法
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = qtw.QLabel("This is a PyQt5 window!")

        # Qt namespace中有大量的特征用于自定义widget的行为，类似常量
        label.setAlignment(Qt.AlignCenter)

        # 将widget放入window的中央，默认widget将填满整个window
        self.setCentralWidget(label)

        toolbar = qtw.QToolBar("My Main toolbar")
        self.addToolBar(toolbar)

        # 创建一个QAction实例
        button_action = qtw.QAction("Your button", self)
        # 这个信息会显示在statusbar中，如果有的话
        button_action.setStatusTip("This is you button")
        # 将action的signal triggered链接到一个slot上
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # 将action加入的toolbar上
        toolbar.addAction(button_action)

    def onMyToolBarButtonClick(self, s):
        # 接受action传送的signal
        print("click", s)


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
