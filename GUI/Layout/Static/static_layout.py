from PyQt5.QtWidgets import *

def static(self):
    self.header = QLabel('', self)
    self.header.resize(1300, 100)
    self.header.setStyleSheet("background-color: #083282;")

    self.main = QLabel('', self)
    self.main.resize(1300, 1200)
    self.main.move(0, 100)
    self.main.setStyleSheet("background-color: white;")