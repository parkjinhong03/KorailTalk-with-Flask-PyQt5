from PyQt5.QtWidgets import *
import requests


class ClickEvent:
    def seat_click(self, seat_num, seat_data, date, num, start, end):
        if seat_data[seat_num] == '1':
            return

        url = f"http://127.0.0.1:5000/train/{date}"

        data = {
            'train_num': num,
            "seat": seat_num,
            "start": start,
            "end": end
        }

        res = requests.post(url=url, data=data)

        if res.status_code == 200:
            QMessageBox.about(self, "Message", "예매를 완료하였습니다!")

        else:
            QMessageBox.about(self, "Message", "다시 시도해 보세요. 계속 안될 경우 관리자에게 문의해 주세요.")