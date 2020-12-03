import sys

import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg


# 这里使用面向对象的方法
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = qtw.QLabel("This is a PyQt5 window!")

        # Qt namespace中有大量的特征用于自定义widget的行为，类似常量
        label.setAlignment(qtc.Qt.AlignCenter)

        # 将widget放入window的中央，默认widget将填满整个window
        self.setCentralWidget(label)

        toolbar = qtw.QToolBar("My Main toolbar")
        toolbar.setIconSize(qtc.QSize(16, 16))
        self.addToolBar(toolbar)

        # 第一个参数是送入的图片，使用QIcon对象
        button_action = qtw.QAction(
            qtg.QIcon("bug.png"), "Your button", self
        )
        button_action.setStatusTip("This is you button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        self.setStatusBar(qtw.QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
