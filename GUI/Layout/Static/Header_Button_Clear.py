def header_btn_clear(self):
    self.header.close()
    self.main.close()
    self.header_logo_background.close()
    self.logo.close()
    self.my_information_button.close()
    try:
        self.logout_button.close()
    except:
        pass