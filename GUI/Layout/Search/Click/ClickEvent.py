from PyQt5.QtWidgets import *


class ClickEvent:
    def start_location(self):
        self.Location_Window = LocationWindow('start', self)

    def end_location(self):
        self.Location_Window = LocationWindow('end', self)

    def select_location(self, location, MainWindow):
        if self.status == 'start':
            MainWindow.start_input_location.setText(location)
        elif self.status == 'end':
            MainWindow.end_input_location.setText(location)
        self.close()

    def change_location(self):
        start = self.start_input_location.text()
        end = self.end_input_location.text()

        self.end_input_location.setText(start)
        self.start_input_location.setText(end)


class LocationWindow(QMainWindow):
    def __init__(self, status, MainWindow):
        super().__init__()
        self.status = status
        self.MainWIndow_colne = MainWindow
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setFixedSize(300, 390)
        self.setWindowTitle('Choose')

        self.btn1 = QPushButton('서울', self)
        self.btn1.resize(90, 90)
        self.btn1.move(0, 0)
        self.btn1.setStyleSheet("font: 20px;")
        self.btn1.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn1.text(), self.MainWIndow_colne))
        self.btn1.show()

        self.btn2 = QPushButton('광명', self)
        self.btn2.resize(90, 90)
        self.btn2.move(100, 0)
        self.btn2.setStyleSheet("font: 20px;")
        self.btn2.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn2.text(), self.MainWIndow_colne))
        self.btn2.show()

        self.btn3 = QPushButton('천안아산', self)
        self.btn3.resize(90, 90)
        self.btn3.move(200, 0)
        self.btn3.setStyleSheet("font: 20px;")
        self.btn3.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn3.text(), self.MainWIndow_colne))
        self.btn3.show()

        self.btn4 = QPushButton('오송', self)
        self.btn4.resize(90, 90)
        self.btn4.move(0, 100)
        self.btn4.setStyleSheet("font: 20px;")
        self.btn4.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn4.text(), self.MainWIndow_colne))
        self.btn4.show()

        self.btn5 = QPushButton('대전', self)
        self.btn5.resize(90, 90)
        self.btn5.move(100, 100)
        self.btn5.setStyleSheet("font: 20px;")
        self.btn5.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn5.text(), self.MainWIndow_colne))
        self.btn5.show()

        self.btn6 = QPushButton('김천구미', self)
        self.btn6.resize(90, 90)
        self.btn6.move(200, 100)
        self.btn6.setStyleSheet("font: 20px;")
        self.btn6.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn6.text(), self.MainWIndow_colne))
        self.btn6.show()

        self.btn7 = QPushButton('동대구', self)
        self.btn7.resize(90, 90)
        self.btn7.move(0, 200)
        self.btn7.setStyleSheet("font: 20px;")
        self.btn7.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn7.text(), self.MainWIndow_colne))
        self.btn7.show()

        self.btn8 = QPushButton('신경주', self)
        self.btn8.resize(90, 90)
        self.btn8.move(100, 200)
        self.btn8.setStyleSheet("font: 20px;")
        self.btn8.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn8.text(), self.MainWIndow_colne))
        self.btn8.show()

        self.btn9 = QPushButton('울산', self)
        self.btn9.resize(90, 90)
        self.btn9.move(200, 200)
        self.btn9.setStyleSheet("font: 20px;")
        self.btn9.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn9.text(), self.MainWIndow_colne))
        self.btn9.show()

        self.btn10 = QPushButton('부산', self)
        self.btn10.resize(90, 90)
        self.btn10.move(100, 300)
        self.btn10.setStyleSheet("font: 20px;")
        self.btn10.clicked.connect(lambda x: ClickEvent.select_location(self, self.btn10.text(), self.MainWIndow_colne))
        self.btn10.show()
