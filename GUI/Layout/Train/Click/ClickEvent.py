from PyQt5.QtWidgets import *
from Layout.Train.Clear import train_clear
from Layout.Reservation.ReservationWindow import ReservationWindow
from Layout.Login import user_token
import requests
import json

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


class ClickEvent:
    def reservation_click(self, date, num, start, end, start_time, TrainWindow):
        if len(start_time) == 5:
            hour = start_time[:2]
            minute = start_time[3:5]
        elif len(start_time) == 4:
            hour = start_time[:1]
            minute = start_time[2:4]

        url = "http://127.0.0.1:5000/user"

        acess_token = user_token.access_token
        headers = {
            'Authorization': f"Bearer {acess_token}"
        }

        res = requests.get(url=url, headers=headers)
        reservation_data = json.loads(res.text)

        for i in reservation_data:
            specific_data = reservation_data[i]

            if date == specific_data['date']:
                if str(num) == specific_data['train_num']:
                    QMessageBox.about(self, "Message", "해당 열치는 이미 예매 하셨습니다.")
                    return

        train_clear.clear_table(self)
        ReservationWindow(self, date, num, start, end, TrainWindow)

    def back_button(self):
        train_clear.clear_table(self)

    def handle_button(self, page, total_page):
        if page >= total_page + 1:
            QMessageBox.about(self, 'Message', '더 이상 이후 정보가 없습니다.')
            return 1
        elif page <= 0:
            QMessageBox.about(self, 'Message', '더 이상 이전 정보가 없습니다.')
            return 2
