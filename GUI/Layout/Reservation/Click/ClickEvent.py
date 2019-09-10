from PyQt5.QtWidgets import *
import requests
from Layout.Reservation.Clear.reservation_clear import resercation_clear
from Layout.Login import user_token


class ClickEvent:
    def seat_click(self, seat_num, seat_data, date, num, start, end, TrainWindow):
        if seat_data[seat_num] == '1':
            return

        reply = QMessageBox.question(self, "Message", f"{seat_num}번 좌석을 예매하시겠습니까?", QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)

        if reply == QMessageBox.No:
            return

        url = f"http://127.0.0.1:5000/train/{date}"
        acess_token = user_token.access_token

        headers = {
            'Authorization': f"Bearer {acess_token}"
        }

        data = {
            'train_num': num,
            "seat": seat_num,
            "start": start,
            "end": end
        }

        res = requests.post(url=url, data=data, headers=headers)

        QMessageBox.about(self, "Message", "테스트 기간 동안에는 돈을 받지 않아요")

        if res.status_code == 200:
            QMessageBox.about(self, "Message", "좌석 예매를 완료했습니다!")
            resercation_clear(self)
            TrainWindow(self)

        else:
            QMessageBox.about(self, "Message", "다시 시도해 보세요. 계속 안될 경우 관리자에게 문의해 주세요.")
            return

