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

        button_action = qtw.QAction("Your button", self)
        button_action.setStatusTip("This is you button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)  # 只增加这一行
        toolbar.addAction(button_action)

        self.setStatusBar(qtw.QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
