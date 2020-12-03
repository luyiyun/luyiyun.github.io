# 来源：https://blog.csdn.net/zhulove86/article/details/52563131
# author：Tony Zhu
import sys
from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import (
    QWidget, QApplication, QGroupBox, QPushButton, QLabel,
    QCheckBox, QSpinBox, QHBoxLayout, QComboBox, QGridLayout
)


class SignalEmit(QWidget):

    helpSignal = pyqtSignal(str)  # str表示这个signal发送的信息将是str
    printSignal = pyqtSignal(list)
    # 这里是复合信号，第一个会带有两个值，第二个将带有1个值，可以使用Signal[int, str]和Signal[str]
    #   得到每个部分
    previewSignal = pyqtSignal([int, str], [str])

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.creatControls("打印控制：")
        self.creatResult("操作结果：")

        layout = QHBoxLayout()
        layout.addWidget(self.controlsGroup)
        layout.addWidget(self.resultGroup)
        self.setLayout(layout)

        # 设置自定义Signals的slots
        self.helpSignal.connect(self.showHelpMesage)
        self.printSignal.connect(self.printPaper)
        self.previewSignal[str].connect(self.previewPaper)
        self.previewSignal[int, str].connect(self.previewPaperWithArgs)
        # 这里将自定义signals的发送信息作为slots链接到存在的signals上
        self.printButton.clicked.connect(self.emitPrintSignal)
        self.previewButton.clicked.connect(self.emitPreviewSignal)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle("defined signal")
        self.show()

    def creatControls(self, title):
        # 一个带有标题的盒子，用来作为容器承载更多的widgets，主要用来划分区域
        self.controlsGroup = QGroupBox(title)
        self.printButton = QPushButton("打印")
        self.previewButton = QPushButton("预览")
        numberLabel = QLabel("打印份数：")
        paperLabel = QLabel("纸张类型：")
        # 原来checkBox可以直接给文本来当做label。。
        self.previewStatus = QCheckBox("全屏预览")
        # spin box就是一个数字轮盘
        self.numberSpinBox = QSpinBox()
        self.numberSpinBox.setRange(1, 100)
        self.styleCombo = QComboBox(self)
        self.styleCombo.addItem("A4")
        self.styleCombo.addItem("A5")

        controlsLayout = QGridLayout()
        controlsLayout.addWidget(numberLabel, 0, 0)
        controlsLayout.addWidget(self.numberSpinBox, 0, 1)
        controlsLayout.addWidget(paperLabel, 0, 2)
        controlsLayout.addWidget(self.styleCombo, 0, 3)
        controlsLayout.addWidget(self.printButton, 0, 4)
        controlsLayout.addWidget(self.previewStatus, 3, 0)
        controlsLayout.addWidget(self.previewButton, 3, 1)
        self.controlsGroup.setLayout(controlsLayout)

    def creatResult(self, title):
        self.resultGroup = QGroupBox(title)
        self.resultLabel = QLabel("")
        layout = QHBoxLayout()
        layout.addWidget(self.resultLabel)
        self.resultGroup.setLayout(layout)

    def emitPreviewSignal(self):
        if self.previewStatus.isChecked() is True:
            self.previewSignal[int, str].emit(1080, "Full Screen")
        elif self.previewStatus.isChecked() is False:
            self.previewSignal[str].emit("Preview")

    def emitPrintSignal(self):
        pList = []
        pList.append(self.numberSpinBox.value())
        pList.append(self.styleCombo.currentText())
        self.printSignal.emit(pList)

    def printPaper(self, list):
        self.resultLabel.setText(
            "Print: " + "份数：" + str(list[0]) +
            "纸张：" + str(list[1])
        )

    def previewPaperWithArgs(self, style, text):
        self.resultLabel.setText(str(style) + text)

    def previewPaper(self, text):
        self.resultLabel.setText(text)

    def keyPressEvent(self, event):
        # QWidget自带的方法（event handler），用于在继承时进行改写，
        #   接受的event是关于键盘的事件
        # 在event loop中被时刻监听
        if event.key() == Qt.Key_F1:
            # 如果按下了F1，则helpsignal信号将发送，其发送的消息是字符串
            self.helpSignal.emit("Help Message")

    def showHelpMesage(self, message):
        # 是helpSignal信号的slot，接受的是上面方法中的Help Message字符串，
        #   其行为是将此字符串打印到resultLabel上
        self.resultLabel.setText(message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    dispatch = SignalEmit()
    sys.exit(app.exec_())
