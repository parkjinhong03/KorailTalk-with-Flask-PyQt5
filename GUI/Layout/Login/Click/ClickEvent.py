from Layout.Login import LoginWindow
from Layout.Login.Click.ClickFunc import ClickFunc
from Layout.Login.Clear import Login_Clear
from Layout.Static import static_layout
from PyQt5.QtWidgets import *


class ClickEvent:
    def Login_Button(self):
        self.login_box.setStyleSheet("background-color: white; border-radius: 10px; border: 1px solid black;")
        self.signup_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')

        self.signup_button.set_defualt_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white" )
        self.signup_button.set_hovering_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.signup_button.initStyle()
        self.login_button.set_defualt_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.login_button.set_hovering_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.login_button.initStyle()

        self.lost_id.setStyleSheet("font: 20px; color: blue; font-weight: bold; background-color: white; border: 0px;")

        self.login_input_id.setPlaceholderText('아이디를 입력하세요.')
        self.login_input_pw.setPlaceholderText('바밀번호를 입력하세요.')
        self.signup_input_id.setPlaceholderText('')
        self.signup_input_pw.setPlaceholderText('')
        self.signup_input_pwc.setPlaceholderText('')

        self.signup_input_id.setText('')
        self.signup_input_pw.setText('')
        self.signup_input_pwc.setText('')

        self.login_input_id.setReadOnly(False)
        self.login_input_pw.setReadOnly(False)

        self.signup_input_id.setReadOnly(True)
        self.signup_input_pw.setReadOnly(True)
        self.signup_input_pwc.setReadOnly(True)

        self.submit_button.setText('로그인')
        LoginWindow.status = "Login"


    def Signup_Button(self):
        self.signup_box.setStyleSheet("background-color: white; border-radius: 10px; border: 1px solid black;")
        self.login_box.setStyleSheet('background-color: #ededed; border-radius: 10px; border: 1px solid black;')

        self.login_button.set_defualt_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.login_button.set_hovering_style("background-color: #ededed; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.login_button.initStyle()
        self.signup_button.set_defualt_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.signup_button.set_hovering_style("background-color: white; border-radius: 10px; font: 30px; font-weight: bold; border: 1px solid white")
        self.signup_button.initStyle()

        self.lost_id.setStyleSheet("font: 20px; color: blue; font-weight: bold; background-color: #ededed; border: 0px;")

        self.login_input_id.setPlaceholderText('')
        self.login_input_pw.setPlaceholderText('')
        self.signup_input_id.setPlaceholderText('아이디를 입력하세요.')
        self.signup_input_pw.setPlaceholderText('비밀번호를 입력하세요.')
        self.signup_input_pwc.setPlaceholderText('비밀번호를 재입력하세요.')

        self.login_input_id.setText('')
        self.login_input_pw.setText('')

        self.login_input_id.setReadOnly(True)
        self.login_input_pw.setReadOnly(True)

        self.signup_input_id.setReadOnly(False)
        self.signup_input_pw.setReadOnly(False)
        self.signup_input_pwc.setReadOnly(False)

        self.submit_button.setText('회원가입')
        LoginWindow.status = "Signup"

    def Submit_Button(self):
        if LoginWindow.status == 'Login':
            _userID = self.login_input_id.text()
            _userPW = self.login_input_pw.text()
            code = ClickFunc.Login(self, _userID, _userPW)
            if code == 200:
                self.clear_LoginWindow = QLabel('', self)
                self.clear_LoginWindow.resize(1300, 800)
                self.clear_LoginWindow.setStyleSheet("background-color: white;")
                self.clear_LoginWindow.show()


        if LoginWindow.status == 'Signup':
            _userID = self.signup_input_id.text()
            _userPW = self.signup_input_pw.text()
            _userPWC = self.signup_input_pwc.text()
            if _userPWC == '' or _userPW == '' or _userID == '':
                QMessageBox.about(self, 'Error', 'Please enter a value, not a black.')

            code = ClickFunc.Signup(self, _userID, _userPW, _userPWC)
            if code == 200:
                ClickEvent.Login_Button(self)

    def Lost_Button(self):
        QMessageBox.about(self, 'Message', '그러게 왜 잃어 버림?')