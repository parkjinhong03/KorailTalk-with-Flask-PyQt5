from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5 import QtCore

class PushButton(QPushButton):
    default_style = ""
    hovering_style = ""

    def __init__(self, *__args):
         super().__init__(*__args)
         self.installEventFilter(self)


    def eventFilter(self, object, event):
        if event.type() == QtCore.QEvent.HoverEnter:
            QApplication.setOverrideCursor(Qt.PointingHandCursor)
            if self.hovering_style != "":
                self.setStyleSheet(self.hovering_style)
            return True
        elif event.type() == QtCore.QEvent.HoverLeave:
            QApplication.setOverrideCursor(Qt.ArrowCursor)
            if self.default_style != "":
                self.setStyleSheet(self.default_style)
            return True

        return False

    def initStyle(self):
        self.setStyleSheet(self.default_style)

    def set_defualt_style(self, def_st):
        self.default_style = def_st

    def set_hovering_style(self, hovering_st):
        self.hovering_style = hovering_st