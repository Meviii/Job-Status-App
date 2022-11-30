from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi

PATH = 'designer_files/home_view.ui'
class Ui_HomeWindow(QDialog):
    def __init__(self, widget, app_user):
        super(Ui_HomeWindow, self).__init__()
        loadUi(PATH, self)
        self.widget = widget
        self.app_user = app_user
        widget.setFixedHeight(600)
        widget.setFixedWidth(800)
        