from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Layout.Static import static_layout
from Button_Hover import PushButton

status = "Login"


def LoginWindow(self):
    # 배경화면 설정
    self.background = QLabel(self)
    self.background.resize(1300, 800)
    pixmap_background = QPixmap("img/login_bakcgrond1.PNG")
    pixmap_background.scaledToHeight(800)
    self.background.setPixmap(QPixmap(pixmap_background))

    # 기본 틀 설정
    static_layout.static(self)

    # 로고 사진
    self.logo = QLabel(self)
    self.logo.resize(400, 50)
    self.logo.move(500, 25)
    pixmap_logo = QPixmap("Img/Korail_logo.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(300)
    self.logo.setPixmap(QPixmap(pixmap_logo))

    # 로그인 박스
    self.login_box = QLabel('', self)
    self.login_box.resize(500, 400)
    self.login_box.move(100, 230)
    self.login_box.setStyleSheet('background-color: white; border-radius: 10px; border: 1px solid black;')

    # 회원가입 박스
    self.signup_box = QLabel('', self)
    self.signup_box.resize(500, 400)
    self.signup_box.move(700, 230)
    self.signup_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')

    # 로그인 설정 버튼
    self.login_button = PushButton('Login', self)
    self.login_button.move(260, 150)
    self.login_button.resize(170, 50)
    self.login_button.set_defualt_style("background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
    self.login_button.set_hovering_style("background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
    self.login_button.initStyle()
    self.login_button.clicked.connect(lambda x:ClickEvent.Login_Button(self))

    # 회원가입 설정 버튼
    self.signup_button = PushButton('Signup', self)
    self.signup_button.move(865, 150)
    self.signup_button.resize(170, 50)
    self.signup_button.set_defualt_style("background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white;")
    self.signup_button.set_hovering_style("background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
    self.signup_button.initStyle()
    self.signup_button.clicked.connect(lambda x:ClickEvent.Signup_Button(self))

    # 제출 버튼
    self.submit_button = PushButton('로그인', self)
    self.submit_button.set_defualt_style("background-color: #3056ff; border-radius: 10px; font: 30px; font-weight: bold; color: white;")
    self.submit_button.set_hovering_style("background-color: #133aeb; border-radius: 10px; font: 30px; font-weight: bold; color: white;")
    self.submit_button.initStyle()
    self.submit_button.resize(200, 80)
    self.submit_button.move(550, 670)

class ClickEvent:
    def Login_Button(self):
        self.login_box.setStyleSheet("background-color: white; border-radius: 10px; border: 1px solid black;")
        self.signup_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')

        self.signup_button.set_defualt_style(
            "background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white" )
        self.signup_button.set_hovering_style(
            "background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.signup_button.initStyle()
        self.login_button.set_defualt_style(
            "background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.login_button.set_hovering_style(
            "background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.login_button.initStyle()

        self.submit_button.setText('로그인')
        status = "Login"

    def Signup_Button(self):
        self.signup_box.setStyleSheet("background-color: white; border-radius: 10px; border: 1px solid black;")
        self.login_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')

        self.login_button.set_defualt_style(
            "background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.login_button.set_hovering_style(
            "background-color: #ededed; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.login_button.initStyle()
        self.signup_button.set_defualt_style(
            "background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.signup_button.set_hovering_style(
            "background-color: white; border-radius: 10px; font: 20px; font-weight: bold; border: 1px solid white")
        self.signup_button.initStyle()

        self.submit_button.setText('회원가입')
        status = "Signup"