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

        button_action = qtw.QAction(
            qtg.QIcon("bug.png"), "Your button", self
        )
        button_action.setStatusTip("This is you button")
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        # 为了此action添加快捷键
        button_action.setShortcut(qtg.QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)

        # 添加分割线
        toolbar.addSeparator()

        # 添加第二个button
        button_action2 = qtw.QAction(
            qtg.QIcon("bug.png"), "You button2", self
        )
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)

        # toolbar也可以加入其他的widgets
        toolbar.addWidget(qtw.QLabel("Hello"))
        toolbar.addWidget(qtw.QCheckBox())

        # 本来QMainWindow就已经有menu bar了，只是menu bar里是空的
        menu = self.menuBar()

        self.setStatusBar(qtw.QStatusBar(self))

        # 添加一个menu
        file_menu = menu.addMenu("&File")  # &使得此Menu可以有alt来控制
        file_menu.addAction(button_action)  # 为file menu添加一个按钮
        file_menu.addSeparator()  # 添加一个分割线
        file_menu.addAction(button_action2)  # 添加第二个按钮

        # 可以我menu继续添加子menu
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
