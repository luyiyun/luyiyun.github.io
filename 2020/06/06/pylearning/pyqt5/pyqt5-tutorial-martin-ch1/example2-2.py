import sys

from PyQt5.QtWidgets import QApplication, QWidget


try:
    app = QApplication(sys.argv)

    window = QWidget()
    window.show()  # important! 窗口默认是隐藏的

    sys.exit(app.exec_())

finally:
    pass
