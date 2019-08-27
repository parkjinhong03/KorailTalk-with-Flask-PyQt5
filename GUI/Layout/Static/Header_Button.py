from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Layout.Static.Button_Hover import PushButton


def Header_Button(self):
    self.header = QLabel('', self)
    self.header.resize(1300, 100)
    self.header.setStyleSheet("background-color: #083B82;")
    self.header.show()

    self.main = QLabel('', self)
    self.main.resize(1300, 1200)
    self.main.move(0, 100)
    self.main.setStyleSheet("background-color: white;")
    self.main.show()

    self.header_logo_background = QLabel('', self)
    self.header_logo_background.resize(500, 100)
    self.header_logo_background.setStyleSheet("background-color: #083B82;")

    self.logo = QLabel(self)
    self.logo.resize(400, 50)
    self.logo.move(500, 25)
    pixmap_logo = QPixmap("Img/Korail_logo.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(300)
    self.logo.setPixmap(QPixmap(pixmap_logo))
    self.logo.show()

    self.my_information_button = PushButton('승차권 확인', self)
    self.my_information_button.resize(140, 60)
    self.my_information_button.move(950, 20)
    self.my_information_button.set_defualt_style("border-radius: 5px; border: 1px solid white; background-color: rgb(255, 255, 255, 50); font: 20px; font-weight: bold; color: white;")
    self.my_information_button.set_hovering_style("border-radius: 5px; border: 1px solid white; background-color: rgba(0, 0, 0, 100); font: 20px; font-weight: bold; color: white;")
    self.my_information_button.initStyle()
    self.my_information_button.show()

    self.logout_button = PushButton('로그아웃', self)
    self.logout_button.resize(140, 60)
    self.logout_button.move(1110, 20)
    self.logout_button.set_defualt_style("border-radius: 5px; border: 1px solid white; background-color: rgb(255, 255, 255, 50); font: 20px; font-weight: bold; color: white;")
    self.logout_button.set_hovering_style("border-radius: 5px; border: 1px solid white; background-color: rgba(0, 0, 0, 100); font: 20px; font-weight: bold; color: white;")
    self.logout_button.initStyle()
    self.logout_button.show()