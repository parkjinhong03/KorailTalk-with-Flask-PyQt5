from PyQt5.QtWidgets import *
import requests


def ReservationWindow(self, date, num, start, end):
    self.reservation_to_train.raise_()
    self.reservation_to_train.show()
    print(date, num, start, end)

    url = f'http://127.0.0.1:5000/train/{date}'
    params = {
        'train_num': num,
        'start': start,
        'end': end,
        'seat': 10
    }

    res = requests.get(url=url, params=params)
    print(res.text)