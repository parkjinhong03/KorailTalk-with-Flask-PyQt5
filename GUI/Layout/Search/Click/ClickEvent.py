from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from Layout.Search.Clear.Search_clear import search_clear
from Layout.Train.TrainWindow import TrainWindow
from Layout.Login import user_token
from Layout.Static.Button_Hover import PushButton
import requests
import json
import datetime

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
        result = self.setupUI()
        self.show()

        if result == 1:
            QMessageBox.about(self, "Message", "예매하신 열차 정보가 없습니다.")
            self.close()

    def setupUI(self):
        self.setFixedSize(400, 660)
        self.setWindowTitle('Information')
        self.background_label = QLabel('', self)
        self.background_label.resize(400, 660)
        self.background_label.setStyleSheet('background-color: #edf4ff;')
        self.background_label.show()

        reservation_data = self.get_data()

        if 1 not in reservation_data:
            return 1

        count = 0

        for i in reservation_data:
            if type(i) == int:
                count += 1

        self.CreatePage(reservation_data, 1, count // 2 + count % 2)
        return 0

    def CreateButton(self, page, reservation_data, total_page):
        self.before_button = PushButton('before', self)
        self.before_button.resize(100, 30)
        self.before_button.move(95, 615)
        self.before_button.set_defualt_style(
            'background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
        self.before_button.set_hovering_style(
            'background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
        self.before_button.initStyle()
        self.before_button.clicked.connect(self.ClearPage)
        self.before_button.clicked.connect(lambda x: self.CreatePage(reservation_data, page-1, total_page))
        self.before_button.show()

        self.next_button = PushButton('next', self)
        self.next_button.resize(100, 30)
        self.next_button.move(215, 615)
        self.next_button.set_defualt_style(
            'background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
        self.next_button.set_hovering_style(
            'background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
        self.next_button.initStyle()
        self.next_button.clicked.connect(self.ClearPage)
        self.next_button.clicked.connect(lambda x: self.CreatePage(reservation_data, page+1, total_page))
        self.next_button.show()

    def ClearPage(self):
        self.clear_label = QLabel('', self)
        self.clear_label.resize(400, 660)
        self.clear_label.setStyleSheet('background-color: #edf4ff;')
        self.clear_label.show()

    def CreatePage(self, reservation_data, page, total_page):
        if page < 1:
            QMessageBox.about(self, "Message", "더 이상 정보가 없습니다.")
            InformationWindow.CreatePage(self, reservation_data, 1, total_page)
            return

        elif page > total_page:
            QMessageBox.about(self, "Message", "더 이상 정보가 없습니다.")
            InformationWindow.CreatePage(self, reservation_data, total_page, total_page)
            return

        try:
            self.CreateTicket(reservation_data[page*2-1], 0)
            self.CreateTicket(reservation_data[page*2], 1)
        except:
            pass

        self.CreateButton(page, reservation_data, total_page)

    def CreateTicket(self, specific_data, sequence):
        date = int(specific_data['date'])
        train_num = specific_data['train_num']
        seat = specific_data['seat']
        start = InformationWindow.train_korean_name[specific_data['start']]
        start_time = specific_data['start_time']
        end = InformationWindow.train_korean_name[specific_data['end']]
        end_time = specific_data['end_time']
        train_type = specific_data['train_type']

        d = datetime.date(date // 10000, date % 10000 // 100, date % 100)

        self.label_border = QLabel('', self)
        self.label_border.setStyleSheet('border: 1px solid black; background-color: white;')
        self.label_border.resize(360, 280)
        self.label_border.move(20, 20 + sequence * 300)
        self.label_border.show()

        self.label_date = QLabel(f'{date // 10000}년 {date % 10000 //100}월 {date % 100}일 ({InformationWindow.korean_date[d.strftime("%A")]})', self)
        self.label_date.resize(300, 50)
        self.label_date.move(35, 25 + sequence * 300)
        self.label_date.setStyleSheet('font: 22px 맑은 고딕;')
        self.label_date.show()

        self.start_station = QLabel(start + '', self)
        self.start_station.resize(100, 100)
        self.start_station.move(75, 50 + sequence * 300)
        self.start_station.setStyleSheet('font: 26px 맑은 고딕; font-weight: bold;')
        self.start_station.setAlignment(Qt.AlignCenter)
        self.start_station.show()

        self.end_station = QLabel(end + '', self)
        self.end_station.resize(100, 100)
        self.end_station.move(220, 50 + sequence * 300)
        self.end_station.setStyleSheet('font: 26px 맑은 고딕; font-weight: bold;')
        self.end_station.setAlignment(Qt.AlignCenter)
        self.end_station.show()

        self.start_time = QLabel(start_time, self)
        self.start_time.resize(150, 70)
        self.start_time.move(50, 120 + sequence * 300)
        self.start_time.setAlignment(Qt.AlignCenter)
        self.start_time.setStyleSheet('font: 40px;')
        self.start_time.show()

        self.end_time = QLabel(end_time, self)
        self.end_time.resize(150, 70)
        self.end_time.move(200, 120 + sequence * 300)
        self.end_time.setAlignment(Qt.AlignCenter)
        self.end_time.setStyleSheet('font: 40px;')
        self.end_time.show()

        self.arrow = QLabel('→', self)
        self.arrow.move(185, 87 + sequence * 300)
        self.arrow.setStyleSheet('font: 25px; font-weight: bold;')
        self.arrow.show()

        self.table_label_1 = QLabel('', self)
        self.table_label_1.setStyleSheet('background-color: #E7E6E6; border: 1px solid black;')
        self.table_label_1.move(50, 200 + sequence * 300)
        self.table_label_1.resize(100, 30)
        self.table_label_1.show()

        self.table_label_2 = QLabel('', self)
        self.table_label_2.setStyleSheet('background-color: #E7E6E6; border-top: 1px solid black; border-bottom: 1px solid black;')
        self.table_label_2.move(150, 200 + sequence * 300)
        self.table_label_2.resize(100, 30)
        self.table_label_2.show()

        self.table_label_3 = QLabel('', self)
        self.table_label_3.setStyleSheet('background-color: #E7E6E6; border: 1px solid black;')
        self.table_label_3.move(250, 200 + sequence * 300)
        self.table_label_3.resize(100, 30)
        self.table_label_3.show()

        self.table_label_4 = QLabel('', self)
        self.table_label_4.setStyleSheet('background-color: white; border: 1px solid black; border-top: 0px;')
        self.table_label_4.move(50, 230 + sequence * 300)
        self.table_label_4.resize(100, 55)
        self.table_label_4.show()

        self.table_label_5 = QLabel('', self)
        self.table_label_5.setStyleSheet('background-color: white; border-bottom: 1px solid black;')
        self.table_label_5.move(150, 230 + sequence * 300)
        self.table_label_5.resize(100, 55)
        self.table_label_5.show()

        self.table_label_6 = QLabel('', self)
        self.table_label_6.setStyleSheet('background-color: white; border: 1px solid black; border-top: 0px;')
        self.table_label_6.move(250, 230 + sequence * 300)
        self.table_label_6.resize(100, 55)
        self.table_label_6.show()

        self.text_label_1 = QLabel('열차 종류', self)
        self.text_label_1.setStyleSheet('font: 17px 맑은 고딕; font-weight: bold;')
        self.text_label_1.move(63, 197 + sequence * 300)
        self.text_label_1.show()

        self.text_label_2 = QLabel('열차 번호', self)
        self.text_label_2.setStyleSheet('font: 17px 맑은 고딕; font-weight: bold;')
        self.text_label_2.move(163, 197 + sequence * 300)
        self.text_label_2.show()

        self.text_label_3 = QLabel('좌석 번호', self)
        self.text_label_3.setStyleSheet('font: 17px 맑은 고딕; font-weight: bold;')
        self.text_label_3.move(263, 197 + sequence * 300)
        self.text_label_3.show()

        self.train_type_label = QLabel(train_type, self)

        if len(self.train_type_label.text()) <= 4:
           self.train_type_label.setStyleSheet('font: 25px 맑은 고딕;')
        else:
            self.train_type_label.setStyleSheet('font: 20px 맑은 고딕;')

        self.train_type_label.move(51, 239 + sequence * 300)
        self.train_type_label.setAlignment(Qt.AlignCenter)
        self.train_type_label.show()

        self.train_num_label = QLabel(train_num, self)
        self.train_num_label.setStyleSheet('font: 30px 맑은 고딕;')
        self.train_num_label.move(174, 239 + sequence * 300)
        self.train_num_label.show()

        self.seat_label = QLabel(seat, self)
        self.seat_label.setStyleSheet('font: 30px 맑은 고딕;')
        self.seat_label.move(283, 239 + sequence * 300)
        self.seat_label.show()

    def get_data(self):
        url = "http://127.0.0.1:5000/user"
        count = 0
        return_dict = {}

        access_token = user_token.access_token

        headers = {
            'Authorization': f'Bearer {access_token}'
        }

        res = requests.get(url=url, headers=headers)
        reservation_data = json.loads(res.text)

        now = datetime.datetime.now()

        for i in reservation_data:
            specific_data = reservation_data[i]
            if int(specific_data['date']) < int(now.strftime('%Y%m%d')):
                continue
            count += 1

            url = 'http://127.0.0.1:5000/train'
            params = {
                'start': specific_data['start'],
                'end': specific_data['end'],
                'date': specific_data['date']
            }
            res = requests.get(url=url, params=params)
            time_table = json.loads(res.text)

            for j in time_table:
                specific_time_table = time_table[j]
                try:
                    if int(specific_time_table['train_num']) == int(specific_data['train_num']):
                        specific_data['start_time'] = specific_time_table['start_time']
                        specific_data['end_time'] = specific_time_table['end_time']
                        specific_data['train_type'] = specific_time_table['train_name']
                        break
                except:
                    continue

            return_dict[count] = specific_data

        return return_dict

    korean_date = {
        'Monday': '월',
        'Tuesday': '화',
        'Wednesday': '수',
        'Thursday': '목',
        'Friday': '금',
        'Saturday': '토',
        'Sunday': '일'
    }

    train_korean_name = {
        'Seoul': '서울',
        'Gwangmyeong': '광명',
        'Cheonan_Asan': '천안아산',
        'Osong': '오송',
        'Daejeon': '대전',
        'Gimcheon_Gumi': '김천구미',
        'Dongdaegu': '동대구',
        'Singyeongju': '신경주',
        'Ulsan': '울산',
        'Busan': '부산'
    }


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