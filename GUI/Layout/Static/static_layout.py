from PyQt5.QtWidgets import *


def static(self):
    self.header = QLabel('', self)
    self.header.resize(1300, 100)
    self.header.setStyleSheet("background-color: #083B82;")
    self.header.show()

    self.main = QLabel('', self)
    self.main.resize(1300, 1200)
    self.main.move(0, 100)
    self.main.setStyleSheet("background-color: #bad4db")
    self.main.show()