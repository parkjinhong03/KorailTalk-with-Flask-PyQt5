from PyQt5.QtWidgets import *


class ClickEvent:
    def start_location(self):
        self.Location_Window = LocationWindow()

    def end_location(self):
        self.asdfasdf = QLabel('sfd', self)
        self.asdfasdf.show()


class LocationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle('Choose')

        self.btn1 = QPushButton('서울', self)
        self.btn1.resize(90, 90)
        self.btn1.move(0, 0)
        self.btn1.setStyleSheet("font: 20px;")
        self.btn1.show()

        self.btn2 = QPushButton('광명', self)
        self.btn2.resize(90, 90)
        self.btn2.move(100, 0)
        self.btn2.setStyleSheet("font: 20px;")
        self.btn2.show()

        self.btn3 = QPushButton('천안아산', self)
        self.btn3.resize(90, 90)
        self.btn3.move(200, 0)
        self.btn3.setStyleSheet("font: 20px;")
        self.btn3.show()

        self.btn4 = QPushButton('오송', self)
        self.btn4.resize(90, 90)
        self.btn4.move(0, 100)
        self.btn4.setStyleSheet("font: 20px;")
        self.btn4.show()

        self.btn5 = QPushButton('대전', self)
        self.btn5.resize(90, 90)
        self.btn5.move(100, 100)
        self.btn5.setStyleSheet("font: 20px;")
        self.btn5.show()

        self.btn6 = QPushButton('김천구미', self)
        self.btn6.resize(90, 90)
        self.btn6.move(200, 100)
        self.btn6.setStyleSheet("font: 20px;")
        self.btn6.show()

        self.btn7 = QPushButton('동대구', self)
        self.btn7.resize(90, 90)
        self.btn7.move(0, 200)
        self.btn7.setStyleSheet("font: 20px;")
        self.btn7.show()

        self.btn8 = QPushButton('신경주', self)
        self.btn8.resize(90, 90)
        self.btn8.move(100, 200)
        self.btn8.setStyleSheet("font: 20px;")
        self.btn8.show()

        self.btn9 = QPushButton('울산', self)
        self.btn9.resize(90, 90)
        self.btn9.move(200, 200)
        self.btn9.setStyleSheet("font: 20px;")
        self.btn9.show()

        self.btn10 = QPushButton('부산', self)
        self.btn10.resize(90, 90)
        self.btn10.move(100, 300)
        self.btn10.setStyleSheet("font: 20px;")
        self.btn10.show()
