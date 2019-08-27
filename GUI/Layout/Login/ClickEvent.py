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
        status = "Login"

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
        status = "Signup"