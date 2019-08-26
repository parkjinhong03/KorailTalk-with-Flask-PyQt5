import sys
from PyQt5.QtWidgets import *
from test_UI import testUI


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        testUI(self)

    def setupUI(self):
        self.setFixedSize(1300, 800)
        self.setWindowTitle('Korail Talk')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())