import sys

import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg


class CustomDialog(qtw.QDialog):

    def __init__(self, *args, **kwargs):
        super(CustomDialog, self).__init__(*args, **kwargs)

        self.setWindowTitle("HELLO!")

        QBtn = qtw.QDialogButtonBox.Ok | qtw.QDialogButtonBox.Cancel

        self.buttonBox = qtw.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = qtw.QVBoxLayout()
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


# 这里使用面向对象的方法
class MainWindow(qtw.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")
        label = qtw.QLabel("This is a PyQt5 window!")
        label.setAlignment(qtc.Qt.AlignCenter)
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
        button_action.setShortcut(qtg.QKeySequence("Ctrl+p"))
        toolbar.addAction(button_action)
        toolbar.addSeparator()
        button_action2 = qtw.QAction(
            qtg.QIcon("bug.png"), "You button2", self
        )
        button_action2.triggered.connect(self.onMyToolBarButtonClick)
        button_action.setCheckable(True)
        toolbar.addAction(button_action)
        toolbar.addWidget(qtw.QLabel("Hello"))
        toolbar.addWidget(qtw.QCheckBox())
        menu = self.menuBar()
        self.setStatusBar(qtw.QStatusBar(self))
        file_menu = menu.addMenu("&File")  # &使得此Menu可以有alt来控制
        file_menu.addAction(button_action)  # 为file menu添加一个按钮
        file_menu.addSeparator()  # 添加一个分割线
        file_menu.addAction(button_action2)  # 添加第二个按钮
        file_submenu = file_menu.addMenu("Submenu")
        file_submenu.addAction(button_action2)

    def onMyToolBarButtonClick(self, s):
        print("click", s)

        # 主要改动在这里
        dlg = CustomDialog(self)
        if dlg.exec_():
            print("Success!")
        else:
            print("Cancel!")


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
