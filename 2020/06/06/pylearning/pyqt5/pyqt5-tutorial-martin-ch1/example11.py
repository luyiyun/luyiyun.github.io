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

        # 创建一个toolbar，并将toolbar加入到main window中
        toolbar = qtw.QToolBar("My Main toolbar")
        # 告诉toolbar，我们使用的icon 图片的大小，这样icon可以填充整个按钮
        toolbar.setIconSize(qtc.QSize(16, 16))
        self.addToolBar(toolbar)

        # 创建一个按钮（这里使用的是action，这是一个更加通用的抽象的按钮类）
        #   action相对于button的好处在于，button只是一个按钮，所以其唯一接受的交互形式是
        #   press。但action可以作为任何形式的交互出现，即其既可以是按钮，又可以出现在菜单栏，
        #   也可以通过键盘快捷键触发。这在toolbar和menubar的实现中是非常必要的，因为一般来说
        #   有很多内容在toolbar和menu中是共享的，如果没有action，我们需要为menu中和toolbar
        #   中都有的一样的功能实现两次。。
        # action接受的是一个QIcon对象作为其icon、string作为其介绍，还有最后的参数是其parent，
        #   这里其signal会传递非其父元素，所以这里设定为main window
        button_action = qtw.QAction(
            qtg.QIcon("bug.png"), "Your button", self
        )
        # hover到action上，会在status上打印下面的信息
        button_action.setStatusTip("This is you button")
        # 为action的triggeredsignal绑定slot
        button_action.triggered.connect(self.onMyToolBarButtonClick)
        # 该设置使action 按钮有按下的效果
        button_action.setCheckable(True)
        # 将action加入到toolbar中
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

        self.setStatusBar(qtw.QStatusBar(self))

    def onMyToolBarButtonClick(self, s):
        # 这里可以知道，传入的信息是个boolean
        print("click", s)


app = qtw.QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
