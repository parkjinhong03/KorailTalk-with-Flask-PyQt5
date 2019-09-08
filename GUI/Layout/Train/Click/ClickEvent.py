from PyQt5.QtWidgets import *
from Layout.Train.Clear import train_clear

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
    def reservation_click(self, date, num, start, end, start_time):
        if len(start_time) == 5:
            hour = start_time[:2]
            minute = start_time[3:5]
        elif len(start_time) == 4:
            hour = start_time[:1]
            minute = start_time[2:4]

        reply = QMessageBox.question(self, "Message", f'{date[:4]}년 {date[4:6]}월 {date[6:8]}일 {hour}시 {minute}분에 {train_korean_name[start]}역에서 {train_korean_name[end]}역으로\n출발하는 {num}번 열차를 예매하시겠습니까?',
                             QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
        if reply == QMessageBox.No:
            return

        train_clear.clear_table(self)

    def handle_button(self, page, total_page):
        if page >= total_page + 1:
            QMessageBox.about(self, 'Message', '더 이상 이후 정보가 없습니다.')
            return 1
        elif page <= 0:
            QMessageBox.about(self, 'Message', '더 이상 이전 정보가 없습니다.')
            return 2
