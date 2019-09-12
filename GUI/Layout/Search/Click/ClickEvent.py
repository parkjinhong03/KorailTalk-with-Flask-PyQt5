from PyQt5.QtWidgets import *
from Layout.Search.Clear.Search_clear import search_clear
from Layout.Train.TrainWindow import TrainWindow

location_num = {
    '서울': 1,
    '광명': 2,
    '천안아산': 3,
    '오송': 4,
    '대전': 5,
    '김천구미': 6,
    '동대구': 7,
    '신경주': 8,
    '울산': 9,
    '부산': 10
}

radio_change_count = 0


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

    def change_radio(self):
        global radio_change_count

        if radio_change_count % 2 == 0:
            QMessageBox.about(self, 'Message', '어짜피 KTX 밖에 없음용..')
            radio_change_count += 1
            self.radio1.setChecked(True)

        else:
            radio_change_count += 1

    def search_button(self):
        import datetime
        now = datetime.datetime.now()

        if int(self.date_year.currentText()) == int(now.strftime('%Y')):
            if int(self.date_month.currentText()) < int(now.strftime('%m')):
                QMessageBox.about(self, 'Message', '시간을 다시 확인해 주세요!')
                return

            elif int(self.date_month.currentText()) == int(now.strftime('%m')):
                if int(self.date_day.currentText()) < int(now.strftime('%d')):
                    QMessageBox.about(self, 'Message', '시간을 다시 확인해 주세요!')
                    return

        if self.start_input_location.text() == '':
            QMessageBox.about(self, 'Message', '출발역을 선택해 주세요!')
            return
        elif self.end_input_location.text() == '':
            QMessageBox.about(self, 'Message', '도착역을 선택해 주세요!')
            return

        if location_num[self.start_input_location.text()] > location_num[self.end_input_location.text()]:
            QMessageBox.about(self, "Message", "아직 서울 -> 부산 방향밖에 예매가 안되요 ㅜㅜ")
            return

        elif location_num[self.start_input_location.text()] == location_num[self.end_input_location.text()]:
            QMessageBox.about(self, "Message", "서로 다른 기차역을 선택해 주세요.")
            return

        search_clear(self)
        TrainWindow(self)

    def click_information_button(self):
        self.information_window = InformationWindow()


class InformationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()
        self.show()

    def setupUI(self):
        self.setFixedSize(400, 600)
        self.setWindowTitle('Information')


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