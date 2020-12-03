import sys

from PyQt5.QtWidgets import QApplication

# 每个app都需要且只需要一个QApplication实例，可以将命令行参数传入其中。
# 如果确定不需要命令行参数，则传入[]即可
app = QApplication(sys.argv)
# 开启主事件循环
app.exec_()

# application不会运行到这个地方，直到你退出，并且主事件循环结束
