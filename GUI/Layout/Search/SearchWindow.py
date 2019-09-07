from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Layout.Static.Button_Hover import PushButton
from Layout.Static import Header_Button
from Layout.Search.Click.ClickEvent import ClickEvent

month_day_dict = {
    '1': 31,
    '2': 28,
    '3': 31,
    '4': 30,
    '5': 31,
    '6': 30,
    '7': 31,
    '8': 31,
    '9': 30,
    '10': 31,
    '11': 30,
    '12': 31
}


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


    self.change_btn_location = PushButton('변경', self)
    self.change_btn_location.resize(80, 100)
    self.change_btn_location.move(805, 448)
    self.change_btn_location.set_defualt_style("background-color: #EAEAEA; font:25px; border: 1px solid #939798; color: black;")
    self.change_btn_location.set_hovering_style("background-color: #d1d1d1; font:25px; border: 1px solid #939798; color: black;")
    self.change_btn_location.initStyle()
    self.change_btn_location.clicked.connect(lambda x:ClickEvent.change_location(self))
    self.change_btn_location.show()

    self.Next_Icon1 = QLabel(self)
    self.Next_Icon1.resize(400, 50)
    self.Next_Icon1.move(400, 440)
    self.Next_Icon2 = QLabel(self)
    self.Next_Icon2.resize(400, 50)
    self.Next_Icon2.move(400, 510)

    pixmap_logo = QPixmap("Img/Next_Icon.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(20)

    self.Next_Icon1.setPixmap(QPixmap(pixmap_logo))
    self.Next_Icon1.show()
    self.Next_Icon2.setPixmap(QPixmap(pixmap_logo))
    self.Next_Icon2.show()

    # self.Change_Icon = QLabel(self)
    # self.Change_Icon.resize(400, 50)
    # self.Change_Icon.move(725, 475)
    #
    # pixmap_logo1 = QPixmap("Img/Change_Icon.PNG")
    # pixmap_logo1 = pixmap_logo1.scaledToWidth(40)
    # self.Change_Icon.setPixmap(QPixmap(pixmap_logo1))
    # self.Change_Icon.show()

    # Text 설정
    self.start_label_start = QLabel('출발역', self)
    self.start_label_start.move(430, 240)
    self.start_label_start.resize(200, 450)
    self.start_label_start.setStyleSheet("font: 20px; font-weight: bold; color: #0095CD;")
    self.start_label_start.show()

    self.end_label_start = QLabel('도착역', self)
    self.end_label_start.move(430, 308)
    self.end_label_start.resize(200, 450)
    self.end_label_start.setStyleSheet("font: 20px; font-weight: bold; color: #0095CD;")
    self.end_label_start.show()

    self.start_input_location = QLineEdit(self)
    self.start_input_location.resize(200, 33)
    self.start_input_location.move(510, 450)
    self.start_input_location.setStyleSheet("font: 20px; font-weight: bold;")
    self.start_input_location.setReadOnly(True)
    self.start_input_location.show()

    self.end_input_location = QLineEdit(self)
    self.end_input_location.resize(200, 33)
    self.end_input_location.move(510, 515)
    self.end_input_location.setStyleSheet("font: 20px; font-weight: bold;")
    self.end_input_location.setReadOnly(True)
    self.end_input_location.show()

    self.start_btn_location = PushButton('조회', self)
    self.start_btn_location.resize(70, 35)
    self.start_btn_location.move(720, 449)
    self.start_btn_location.set_defualt_style('background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.start_btn_location.set_hovering_style('background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.start_btn_location.initStyle()
    self.start_btn_location.show()
    self.start_btn_location.clicked.connect(lambda x: ClickEvent.start_location(self))

    self.end_btn_location = PushButton('조회', self)
    self.end_btn_location.resize(70, 35)
    self.end_btn_location.move(720, 514)
    self.end_btn_location.set_defualt_style('background-color: #357BE3; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.end_btn_location.set_hovering_style('background-color: #1C5DAE; font: 17px; color: white; font-weight: bold; border: 0px;')
    self.end_btn_location.initStyle()
    self.end_btn_location.show()
    self.end_btn_location.clicked.connect(lambda x: ClickEvent.end_location(self))

    self.group_box1 = QGroupBox("기차", self)
    self.group_box1.resize(700, 100)
    self.group_box1.move(295, 170)
    self.group_box1.show()

    self.radio1 = QRadioButton('전체', self)
    self.radio1.move(350, 190)
    self.radio1.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio1.setChecked(True)
    self.radio1.show()

    self.radio2 = QRadioButton('KTX/KTX-산천/SRT', self)
    self.radio2.resize(200, 30)
    self.radio2.move(440, 190)
    self.radio2.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio2.show()
    self.radio2.toggled.connect(lambda X: ClickEvent.change_radio(self))

    self.radio3 = QRadioButton('ITX-청춘', self)
    self.radio3.resize(200, 30)
    self.radio3.move(440, 230)
    self.radio3.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio3.show()
    self.radio3.toggled.connect(lambda X: ClickEvent.change_radio(self))

    self.radio4 = QRadioButton('새마을호/ITX-새마을', self)
    self.radio4.resize(200, 30)
    self.radio4.move(630, 190)
    self.radio4.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio4.show()
    self.radio4.toggled.connect(lambda X: ClickEvent.change_radio(self))

    self.radio5 = QRadioButton('무궁화호/누리로', self)
    self.radio5.resize(200, 30)
    self.radio5.move(630, 230)
    self.radio5.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio5.show()
    self.radio5.toggled.connect(lambda X: ClickEvent.change_radio(self))

    self.radio6 = QRadioButton('통큰열차', self)
    self.radio6.resize(200, 30)
    self.radio6.move(830, 190)
    self.radio6.setStyleSheet("color: #0095CD;font-weight: bold;")
    self.radio6.show()
    self.radio6.toggled.connect(lambda X: ClickEvent.change_radio(self))

    self.Next_Icon_black = QLabel(self)
    self.Next_Icon_black.resize(400, 50)
    self.Next_Icon_black.move(400, 280)

    pixmap_logo = QPixmap("Img/Next_Icon_black.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(25)

    self.Next_Icon_black.setPixmap(QPixmap(pixmap_logo))
    self.Next_Icon_black.show()

    from datetime  import datetime
    now = datetime.now()

    self.start_label_date = QLabel('출발일', self)
    self.start_label_date.move(435, 280)
    self.start_label_date.resize(100, 50)
    self.start_label_date.setStyleSheet("font: 20px; font-weight: bold; color: #0095CD;")
    self.start_label_date.show()

    self.date_year = QComboBox(self)
    self.date_year.addItem(str(int(now.year)))
    self.date_year.addItem(str(int(now.year) + 1))
    self.date_year.addItem(str(int(now.year) + 2))
    self.date_year.resize(70, 30)
    self.date_year.move(520, 290)
    self.date_year.setStyleSheet("background-color: white; border: 1px solid #a8a8a8;")
    self.date_year.show()

    self.label_year = QLabel('년', self)
    self.label_year.move(595, 290)
    self.label_year.setStyleSheet("font: 20px;")
    self.label_year.show()

    self.date_month = QComboBox(self)

    for i in range(12):
        self.date_month.addItem(str(i + 1))
    self.date_month.setCurrentIndex(now.month - 1)

    self.date_month.resize(70, 30)
    self.date_month.move(640, 290)
    self.date_month.setStyleSheet("background-color: white; border: 1px solid #a8a8a8;")
    self.date_month.currentIndexChanged.connect(lambda x:Set_Combo_Item(self, str(self.date_month.currentIndex()+1)))
    self.date_month.show()

    self.label_month = QLabel('월', self)
    self.label_month.move(715, 290)
    self.label_month.setStyleSheet("font: 20px;")
    self.label_month.show()

    self.date_day = QComboBox(self)
    Set_Combo_Item(self, str(self.date_month.currentIndex()+1))
    self.date_day.setCurrentIndex(now.day-1)
    self.date_day.resize(70, 30)
    self.date_day.move(760, 290)
    self.date_day.setStyleSheet("background-color: white; border: 1px solid #a8a8a8;")
    self.date_day.show()

    self.label_day = QLabel('일', self)
    self.label_day.move(835, 290)
    self.label_day.setStyleSheet("font: 20px;")
    self.label_day.show()

    self.search_btn_submit = PushButton('조회하기', self)
    self.search_btn_submit.resize(220, 55)
    self.search_btn_submit.move(820, 615)
    self.search_btn_submit.set_defualt_style('background-color: #357BE3; font: 20px; color: white; font-weight: bold; border: 0px;')
    self.search_btn_submit.set_hovering_style('background-color: #1C5DAE; font: 20px; color: white; font-weight: bold; border: 0px;')
    self.search_btn_submit.initStyle()
    self.search_btn_submit.clicked.connect(lambda X: ClickEvent.search_button(self))
    self.search_btn_submit.show()


def Set_Combo_Item(self, month):
    self.date_day.clear()
    for i in range(month_day_dict[month]):
        self.date_day.addItem(str(i+1))