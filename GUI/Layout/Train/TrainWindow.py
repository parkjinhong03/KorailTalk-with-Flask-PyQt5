from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from Layout.Static.Header_Button import Header_Button
import requests
import datetime
import json


def TrainWindow(self):
    Header_Button(self)
    layout_module.DataTitle(self)

    train_data = my_request.Request_Train(self)

    for i in range(7):
        specific_train_data = train_data[str(i+1)]
        layout_module.CreateTuple(self, i+1, specific_train_data['train_num'], specific_train_data['train_name'], specific_train_data['start_time'],
                                  specific_train_data['end_time'], train_data['fare']['general'], specific_train_data['operating_time'])


class layout_module:
    font_color = {
        1: 'rgb(255, 0, 0)',
        2: 'rgb(255, 50, 0)',
        3: 'rgb(255, 255, 0)',
        4: 'rgb(0, 255, 0)',
        5: 'rgb(0, 0, 255)',
        6: 'rgb(0, 5, 255)',
        7: 'rgb(100, 0, 255)'
    }

    def CreateTuple(self, locate, train_num, train_name, start_time, end_time, fare, operating_time):
        default_x = 185
        default_y = 210
        a = 'background-color: white; font: 22px; font-weight: bold; border-bottom: 1px solid black; border-right: 1px solid black;'

        self.label_TrainNum_data = QLabel(str(train_num), self)
        self.label_TrainNum_data.setStyleSheet(
            a + f'font: 25px; font-weight: bold; color: {layout_module.font_color[locate]};')
        self.label_TrainNum_data.resize(110, 70)
        self.label_TrainNum_data.setAlignment(Qt.AlignCenter)
        self.label_TrainNum_data.move(default_x, default_y + (locate-1) * 70)
        self.label_TrainNum_data.show()

        self.label_TrainName_data = QLabel(train_name, self)
        if len(train_name) > 5:
            self.label_TrainName_data.setStyleSheet( a + f'font: 20px; font-weight: bold;')
        else:
            self.label_TrainName_data.setStyleSheet( a + f'font: 24px; font-weight: bold;')
        self.label_TrainName_data.resize(110, 70)
        self.label_TrainName_data.setAlignment(Qt.AlignCenter)
        self.label_TrainName_data.move(default_x + 110, default_y + (locate - 1) * 70)
        self.label_TrainName_data.show()

        self.label_StartTime_data = QLabel(start_time, self)
        self.label_StartTime_data.setStyleSheet(
            a + f'font: 25px; font-weight: bold;')
        self.label_StartTime_data.resize(110, 70)
        self.label_StartTime_data.setAlignment(Qt.AlignCenter)
        self.label_StartTime_data.move(default_x + 220, default_y + (locate - 1) * 70)
        self.label_StartTime_data.show()

        self.label_EndTime_data = QLabel(end_time, self)
        self.label_EndTime_data.setStyleSheet(
            a + f'font: 25px; font-weight: bold;')
        self.label_EndTime_data.resize(110, 70)
        self.label_EndTime_data.setAlignment(Qt.AlignCenter)
        self.label_EndTime_data.move(default_x + 330, default_y + (locate - 1) * 70)
        self.label_EndTime_data.show()

        self.Reservation_box1 = QLabel('', self)
        self.Reservation_box1.setStyleSheet(
            a + f'font: 25px; font-weight: bold;')
        self.Reservation_box1.resize(120, 70)
        self.Reservation_box1.setAlignment(Qt.AlignCenter)
        self.Reservation_box1.move(default_x + 440, default_y + (locate - 1) * 70)
        self.Reservation_box1.show()

        self.Reservation_box2 = QLabel('', self)
        self.Reservation_box2.setStyleSheet(
            a + f'font: 25px; font-weight: bold;')
        self.Reservation_box2.resize(110, 70)
        self.Reservation_box2.setAlignment(Qt.AlignCenter)
        self.Reservation_box2.move(default_x + 560, default_y + (locate - 1) * 70)
        self.Reservation_box2.show()

        self.label_Fare_data = QLabel(str(fare), self)
        self.label_Fare_data.setStyleSheet(
            a + f'font: 24px; font-weight: bold;')
        self.label_Fare_data.resize(150, 70)
        self.label_Fare_data.setAlignment(Qt.AlignCenter)
        self.label_Fare_data.move(default_x + 670, default_y + (locate - 1) * 70)
        self.label_Fare_data.show()

        self.label_OperatingTime_data = QLabel(operating_time, self)
        self.label_OperatingTime_data.setStyleSheet(
            a + f'font: 24px; font-weight: bold; border-right: 0px;')
        self.label_OperatingTime_data.resize(110, 70)
        self.label_OperatingTime_data.setAlignment(Qt.AlignCenter)
        self.label_OperatingTime_data.move(default_x + 820, default_y + (locate - 1) * 70)
        self.label_OperatingTime_data.show()


    def DataTitle(self):
        default_x = 185
        default_y = 150
        a = 'background-color: #F8F8F8; font: 22px HY헤드라인M; border-top: 4px solid black; border-bottom: 1px solid black; border-right: 1px solid black;'

        self.label_TrainNum = QLabel('열차\n번호', self)
        self.label_TrainNum.setStyleSheet(a + 'font: 18px HY헤드라인M;')
        self.label_TrainNum.resize(110, 60)
        self.label_TrainNum.setAlignment(Qt.AlignCenter)
        self.label_TrainNum.move(default_x, default_y)
        self.label_TrainNum.show()

        self.label_TrainName = QLabel('열차', self)
        self.label_TrainName.setStyleSheet(a)
        self.label_TrainName.resize(110, 60)
        self.label_TrainName.setAlignment(Qt.AlignCenter)
        self.label_TrainName.move(default_x + 110, default_y)
        self.label_TrainName.show()

        self.label_Start= QLabel('출발', self)
        self.label_Start.setStyleSheet(a)
        self.label_Start.resize(110, 60)
        self.label_Start.setAlignment(Qt.AlignCenter)
        self.label_Start.move(default_x + 220, default_y)
        self.label_Start.show()

        self.label_End = QLabel('도착', self)
        self.label_End.setStyleSheet(a)
        self.label_End.resize(110, 60)
        self.label_End.setAlignment(Qt.AlignCenter)
        self.label_End.move(default_x + 330, default_y)
        self.label_End.show()

        self.label_GeneralRoom = QLabel('일반실', self)
        self.label_GeneralRoom.setStyleSheet(a)
        self.label_GeneralRoom.resize(120, 60)
        self.label_GeneralRoom.setAlignment(Qt.AlignCenter)
        self.label_GeneralRoom.move(default_x + 440, default_y)
        self.label_GeneralRoom.show()

        self.label_End = QLabel('특실', self)
        self.label_End.setStyleSheet(a)
        self.label_End.resize(110, 60)
        self.label_End.setAlignment(Qt.AlignCenter)
        self.label_End.move(default_x + 560, default_y)
        self.label_End.show()

        self.label_End = QLabel('가격', self)
        self.label_End.setStyleSheet(a)
        self.label_End.resize(150, 60)
        self.label_End.setAlignment(Qt.AlignCenter)
        self.label_End.move(default_x + 670, default_y)
        self.label_End.show()

        self.label_TrainTime = QLabel('소요\n시간', self)
        self.label_TrainTime.setStyleSheet(a + 'font: 18px HY헤드라인M; border-right: 0px;')
        self.label_TrainTime.resize(110, 60)
        self.label_TrainTime.setAlignment(Qt.AlignCenter)
        self.label_TrainTime.move(default_x+820, default_y)
        self.label_TrainTime.show()


class my_request:
    def Request_Train(self):
        start_train, end_train = my_request.KoreanToEnglish(self, '서울', '부산')  # -> SearchWindow 없이 바로 실행 시 인자 값으로 준 역의 영어 이름이 반환됨
        date = my_request.Get_Date(self, '20190908')  # -> SearchWindow 없이 바로 실행 시 인자 값으로 준 날짜가 반환됨

        url = "http://127.0.0.1:5000/train"
        params = {
            'start': start_train,
            'end': end_train,
            'date': date
        }
        res = requests.get(url=url, params=params)

        return json.loads(res.text)

    def Get_Date(self, my_date=None):
        try:
            date = self.date_year.currentText()

            if len(self.date_month.currentText()) == 2:
                date = date + self.date_month.currentText()
            else:
                date = date + '0' + self.date_month.currentText()

            if len(self.date_day.currentText()) == 2:
                date = date + self.date_day.currentText()
            else:
                date = date + '0' + self.date_day.currentText()

        except:
            now = datetime.datetime.now()
            if my_date==None:
                date = now.strftime("%Y%m%d")
            else:
                date = my_date

        return date

    def KoreanToEnglish(self, start=None, end=None):
        train_english_name = {
            '서울': 'Seoul',
            '광명': 'Gwangmyeong',
            '천안아산': 'Cheonan_Asan',
            '오송': 'Osong',
            '대전': 'Daejeon',
            '김천구미': 'Gimcheon_Gumi',
            '동대구': 'Dongdaegu',
            '신경주': 'Singyeongju',
            '울산': 'Ulsan',
            '부산': 'Busan'
        }

        try:
            return train_english_name[self.start_input_location.text()], train_english_name[self.end_input_location.text()]

        except:
            return train_english_name[start], train_english_name[end]