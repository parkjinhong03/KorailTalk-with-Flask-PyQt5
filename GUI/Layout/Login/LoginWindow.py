from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from Layout.Static.Button_Hover import PushButton
from Layout.Login.Click.ClickEvent import ClickEvent
from Layout.Static.Header_Button import Header_Button
from Layout.Search.Clear.Search_clear import search_clear

status = "Login"


def log_out(self):
    reply = QMessageBox.question(self, 'Message', '정말로 로그아웃 하시겠습니까?', QMessageBox.Yes | QMessageBox.No, QMessageBox.Yes)
    if reply == QMessageBox.No:
        return
    search_clear(self)
    LoginWindow(self)


def LoginWindow(self):
    self.logout_button = PushButton('로그아웃', self)
    self.logout_button.resize(140, 60)
    self.logout_button.move(1110, 20)
    self.logout_button.set_defualt_style("border-radius: 5px; border: 1px solid white; background-color: rgb(255, 255, 255, 50); font: 20px; font-weight: bold; color: white;")
    self.logout_button.set_hovering_style("border-radius: 5px; border: 1px solid white; background-color: rgba(0, 0, 0, 100); font: 20px; font-weight: bold; color: white;")
    self.logout_button.initStyle()
    self.logout_button.clicked.connect(lambda x:log_out(self))
    self.logout_button.close()

    Header_Button(self)
    self.my_information_button.close()
    self.main.setStyleSheet('background-color: #bad4db;')
    # 로고 사진
    self.logo = QLabel(self)
    self.logo.resize(400, 50)
    self.logo.move(500, 25)
    pixmap_logo = QPixmap("Img/Korail_logo.PNG")
    pixmap_logo = pixmap_logo.scaledToWidth(300)
    self.logo.setPixmap(QPixmap(pixmap_logo))
    self.logo.show()

    # 로그인 박스
    self.login_box = QLabel('', self)
    self.login_box.resize(500, 400)
    self.login_box.move(100, 230)
    self.login_box.setStyleSheet('background-color: white; border-radius: 10px; border: 1px solid black;')
    self.login_box.show()

    self.line1 = QLabel(self)
    self.line1.resize(400, 1)
    self.line1.move(150, 500)
    self.line1.setStyleSheet("border: 1px solid black;")
    self.line1.show()

    # 회원가입 박스
    self.signup_box = QLabel('', self)
    self.signup_box.resize(500, 400)
    self.signup_box.move(700, 230)
    self.signup_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')
    self.signup_box.show()

    # 로그인 설정 버튼
    self.login_button = PushButton('Login', self)
    self.login_button.move(260, 150)
    self.login_button.resize(170, 50)
    self.login_button.set_defualt_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
    self.login_button.set_hovering_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
    self.login_button.initStyle()
    self.login_button.clicked.connect(lambda x:ClickEvent.Login_Button(self))
    self.login_button.show()

    # 회원가입 설정 버튼
    self.signup_button = PushButton('Signup', self)
    self.signup_button.move(865, 150)
    self.signup_button.resize(170, 50)
    self.signup_button.set_defualt_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white;")
    self.signup_button.set_hovering_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
    self.signup_button.initStyle()
    self.signup_button.clicked.connect(lambda x:ClickEvent.Signup_Button(self))
    self.signup_button.show()

    # 로그인 LineEdit & Label
    self.login_label_id = QLabel('ID', self)
    self.login_label_id.resize(50, 50)
    self.login_label_id.move(170, 300)
    self.login_label_id.setStyleSheet("font: 50px; font-weight: bold;")
    self.login_label_id.show()

    self.login_input_id = QLineEdit(self)
    self.login_input_id.resize(280, 40)
    self.login_input_id.move(280, 305)
    self.login_input_id.setPlaceholderText('아이디를 입력하세요.')
    self.login_input_id.setStyleSheet("font: 20px; font-weight: bold; border: 1px solid #828282; border-radius: 10px;")
    self.login_input_id.show()

    self.login_label_pw = QLabel('PW', self)
    self.login_label_pw.resize(90, 50)
    self.login_label_pw.move(155, 400)
    self.login_label_pw.setStyleSheet("font: 50px; font-weight: bold;")
    self.login_label_pw.show()

    self.login_input_pw = QLineEdit(self)
    self.login_input_pw.resize(280, 40)
    self.login_input_pw.move(280, 405)
    self.login_input_pw.setEchoMode(QLineEdit.Password)
    self.login_input_pw.setPlaceholderText('비밀번호를 입력하세요.')
    self.login_input_pw.setStyleSheet("font: 20px; font-weight: bold; border: 1px solid #828282; border-radius: 10px;")
    self.login_input_pw.show()

    self.lost_id = QPushButton('비밀번호가 기억이 안나시나요?', self)
    self.lost_id.resize(350, 50)
    self.lost_id.move(180, 530)
    self.lost_id.setStyleSheet("font: 20px; color: blue; font-weight: bold; background-color: white; border: 0px;")
    self.lost_id.clicked.connect(lambda X: ClickEvent.Lost_Button(self))
    self.lost_id.show()

    # 회원가입 LineEdit & Label
    self.signup_label_id = QLabel('ID', self)
    self.signup_label_id.resize(50, 50)
    self.signup_label_id.move(770, 300)
    self.signup_label_id.setStyleSheet("font: 50px; font-weight: bold;")
    self.signup_label_id.show()

    self.signup_input_id = QLineEdit(self)
    self.signup_input_id.resize(280, 40)
    self.signup_input_id.move(880, 305)
    self.signup_input_id.setStyleSheet("font: 20px; font-weight: bold; border: 1px solid #828282; border-radius: 10px;")
    self.signup_input_id.show()

    self.signup_label_pw = QLabel('PW', self)
    self.signup_label_pw.resize(90, 50)
    self.signup_label_pw.move(755, 400)
    self.signup_label_pw.setStyleSheet("font: 50px; font-weight: bold;")
    self.signup_label_pw.show()

    self.signup_input_pw = QLineEdit(self)
    self.signup_input_pw.resize(280, 40)
    self.signup_input_pw.move(880, 405)
    self.signup_input_pw.setEchoMode(QLineEdit.Password)
    self.signup_input_pw.setStyleSheet("font: 20px; font-weight: bold; border: 1px solid #828282; border-radius: 10px;")
    self.signup_input_pw.show()

    self.signup_label_pwc = QLabel('PWC', self)
    self.signup_label_pwc.resize(100, 50)
    self.signup_label_pwc.move(750, 500)
    self.signup_label_pwc.setStyleSheet("font: 40px; font-weight: bold;")
    self.signup_label_pwc.show()

    self.signup_input_pwc = QLineEdit(self)
    self.signup_input_pwc.resize(280, 40)
    self.signup_input_pwc.move(880, 505)
    self.signup_input_pwc.setEchoMode(QLineEdit.Password)
    self.signup_input_pwc.setStyleSheet("font: 20px; font-weight: bold; border: 1px solid #828282; border-radius: 10px;")
    self.signup_input_pwc.show()

    self.signup_input_id.setReadOnly(True)
    self.signup_input_pw.setReadOnly(True)
    self.signup_input_pwc.setReadOnly(True)

    # 제출 버튼
    self.submit_button = PushButton('로그인', self)
    self.submit_button.set_defualt_style("background-color: #3056ff; border-radius: 10px; font: 30px; font-weight: bold; color: white;")
    self.submit_button.set_hovering_style("background-color: #133aeb; border-radius: 10px; font: 30px; font-weight: bold; color: white;")
    self.submit_button.initStyle()
    self.submit_button.resize(200, 80)
    self.submit_button.move(550, 670)
    self.submit_button.clicked.connect(lambda X: ClickEvent.Submit_Button(self))
    self.submit_button.show()