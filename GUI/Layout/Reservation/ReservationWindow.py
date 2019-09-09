from PyQt5.QtWidgets import *
from Layout.Static.Button_Hover import PushButton
import requests
import json


def ReservationWindow(self, date, num, start, end):
    self.reservation_to_train.raise_()
    self.reservation_to_train.show()
    print(date, num, start, end)

    url = f'http://127.0.0.1:5000/train/{date}'
    params = {
        'train_num': num,
        'start': start,
        'end': end
    }

    res = requests.get(url=url, params=params)
    seat_data = json.loads(res.text)

    CreateSeat(self, seat_data, date, num, start, end)


def CreateSeat(self, seat_data, date, num, start, end):
    self.seat_btn1 = PushButton('1', self)
    self.seat_btn2 = PushButton('2', self)
    self.seat_btn3 = PushButton('3', self)
    self.seat_btn4 = PushButton('4', self)
    self.seat_btn5 = PushButton('5', self)
    self.seat_btn6 = PushButton('6', self)
    self.seat_btn7 = PushButton('7', self)
    self.seat_btn8 = PushButton('8', self)
    self.seat_btn9 = PushButton('9', self)
    self.seat_btn10 = PushButton('10', self)
    self.seat_btn11 = PushButton('11', self)
    self.seat_btn12 = PushButton('12', self)
    self.seat_btn13 = PushButton('13', self)
    self.seat_btn14 = PushButton('14', self)
    self.seat_btn15 = PushButton('15', self)
    self.seat_btn16 = PushButton('16', self)
    self.seat_btn17 = PushButton('17', self)
    self.seat_btn18 = PushButton('18', self)
    self.seat_btn19 = PushButton('19', self)
    self.seat_btn20 = PushButton('20', self)
    self.seat_btn21 = PushButton('21', self)
    self.seat_btn22 = PushButton('22', self)
    self.seat_btn23 = PushButton('23', self)
    self.seat_btn24 = PushButton('24', self)
    self.seat_btn25 = PushButton('25', self)
    self.seat_btn26 = PushButton('26', self)
    self.seat_btn27 = PushButton('27', self)
    self.seat_btn28 = PushButton('28', self)
    self.seat_btn29 = PushButton('29', self)
    self.seat_btn30 = PushButton('30', self)
    self.seat_btn31 = PushButton('31', self)
    self.seat_btn32 = PushButton('32', self)
    self.seat_btn33 = PushButton('33', self)
    self.seat_btn34 = PushButton('34', self)
    self.seat_btn35 = PushButton('35', self)
    self.seat_btn36 = PushButton('36', self)
    self.seat_btn37 = PushButton('37', self)
    self.seat_btn38 = PushButton('38', self)
    self.seat_btn39 = PushButton('39', self)
    self.seat_btn40 = PushButton('40', self)

    self.seat_btn_list = [self.seat_btn1, self.seat_btn2, self.seat_btn3, self.seat_btn4, self.seat_btn5, self.seat_btn6, self.seat_btn7, self.seat_btn8, self.seat_btn9, self.seat_btn10,
                          self.seat_btn11, self.seat_btn12, self.seat_btn13, self.seat_btn14, self.seat_btn15, self.seat_btn16, self.seat_btn17, self.seat_btn18, self.seat_btn19, self.seat_btn20,
                          self.seat_btn21, self.seat_btn22, self.seat_btn23, self.seat_btn24, self.seat_btn25, self.seat_btn26, self.seat_btn27, self.seat_btn28, self.seat_btn29, self.seat_btn30,
                          self.seat_btn31, self.seat_btn32, self.seat_btn33, self.seat_btn34, self.seat_btn35, self.seat_btn36, self.seat_btn37, self.seat_btn38, self.seat_btn39, self.seat_btn40]

    default_x = 150
    default_y = 220

    for i in range(40):
        self.seat_btn_list[i].resize(70, 70)
        if i % 4 >= 2:
            self.seat_btn_list[i].move(default_x + (i // 4) * 100, default_y + (i % 4) * 90 + 80)
        else:
            self.seat_btn_list[i].move(default_x + (i // 4) * 100, default_y + (i % 4) * 90)
        print(seat_data)
        if seat_data[str(i+1)] == '1':
            self.seat_btn_list[i].set_defualt_style('background-color: #b8b8b8; border: 1px solid black; font: 20px;')
            self.seat_btn_list[i].set_hovering_style('background-color: #b8b8b8; border: 1px solid black; font: 20px;')
            self.seat_btn_list[i].initStyle()
            self.seat_btn_list[i].show()
        else:
            self.seat_btn_list[i].set_defualt_style('background-color: white; border: 1px solid black; font: 20px;')
            self.seat_btn_list[i].set_hovering_style('background-color: white; border: 1px solid black; font: 20px;')
            self.seat_btn_list[i].initStyle()
            self.seat_btn_list[i].show()

