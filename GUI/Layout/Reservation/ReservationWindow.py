from PyQt5.QtWidgets import *
import requests


def ReservationWindow(self, date, num, start, end):
    self.reservation_to_train.raise_()
    self.reservation_to_train.show()
    print(date, num, start, end)

    url = f'http://127.0.0.1:5000/train/{date}'
    data = {
        'train_num': num,
        'start': start,
        'end': end,
        'seat': 10
    }

    res = requests.post(url=url, data=data)
    print(res.text)