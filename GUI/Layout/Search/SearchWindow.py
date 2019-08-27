from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Layout.Static.Button_Hover import PushButton
from Layout.Static import Header_Button
from Layout.Search.Click.ClickEvent import ClickEvent


def SearchWindow(self):
    Header_Button.Header_Button(self)

    self.start_box = QLabel('', self)
    self.start_box.resize(800, 200)
    self.start_box.move(250, 150)
    self.start_box.setStyleSheet("background-color: white; border: 2px solid black;")
    self.start_box.show()

    self.end_box = QLabel('', self)
    self.end_box.resize(800, 200)
    self.end_box.move(250, 400)
    self.end_box.setStyleSheet("background-color: #ECF1F4; border: 5px solid #0095CD;")
    self.end_box.show()

    self.Next_Icon1 = QLabel(self)
    self.Next_Icon1.resize(400, 50)
    self.Next_Icon1.move(300, 440)
    self.Next_Icon2 = QLabel(self)
    self.Next_Icon2.resize(400, 50)
    self.Next_Icon2.move(300, 510)

    pixmap_logo = QPixmap("Img/Next_Icon.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(20)

    self.Next_Icon1.setPixmap(QPixmap(pixmap_logo))
    self.Next_Icon1.show()
    self.Next_Icon2.setPixmap(QPixmap(pixmap_logo))
    self.Next_Icon2.show()

    # Text 설정
    self.start_label_start = QLabel('출발역', self)
    self.start_label_start.move(330, 240)
    self.start_label_start.resize(200, 450)
    self.start_label_start.setStyleSheet("font: 20px; font-weight: bold; color: blue;")
    self.start_label_start.show()

    self.end_label_start = QLabel('도착역', self)
    self.end_label_start.move(330, 308)
    self.end_label_start.resize(200, 450)
    self.end_label_start.setStyleSheet("font: 20px; font-weight: bold; color: blue;")
    self.end_label_start.show()

    self.start_input_location = QLineEdit(self)
    self.start_input_location.resize(200, 33)
    self.start_input_location.move(410, 450)
    self.start_input_location.setStyleSheet("font: 20px; font-weight: bold;")
    self.start_input_location.setReadOnly(True)
    self.start_input_location.show()

    self.end_input_location = QLineEdit(self)
    self.end_input_location.resize(200, 33)
    self.end_input_location.move(410, 515)
    self.end_input_location.setStyleSheet("font: 20px; font-weight: bold;")
    self.end_input_location.setReadOnly(True)
    self.end_input_location.show()

    self.start_btn_location = PushButton('조회', self)
    self.start_btn_location.resize(70, 35)
    self.start_btn_location.move(620, 449)
    self.start_btn_location.set_defualt_style('background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.start_btn_location.set_hovering_style('background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.start_btn_location.initStyle()
    self.start_btn_location.show()
    self.start_btn_location.clicked.connect(lambda x: ClickEvent.start_location(self))

    self.end_btn_location = PushButton('조회', self)
    self.end_btn_location.resize(70, 35)
    self.end_btn_location.move(620, 514)
    self.end_btn_location.set_defualt_style('background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.end_btn_location.set_hovering_style('background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.end_btn_location.initStyle()
    self.end_btn_location.show()
    self.end_btn_location.clicked.connect(lambda x: ClickEvent.end_location(self))