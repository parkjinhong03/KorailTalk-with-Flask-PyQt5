from PyQt5.QtWidgets import *


def clear_table(self):
    self.hide_train_list = QLabel('', self)
    self.hide_train_list.resize(1100, 700)
    self.hide_train_list.move(100, 150)
    self.hide_train_list.setStyleSheet('background-color: #edf4ff;')
    self.hide_train_list.show()