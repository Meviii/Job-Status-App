# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_login_dialog(object):
    def setupUi(self, login_dialog):
        if not login_dialog.objectName():
            login_dialog.setObjectName(u"login_dialog")
        login_dialog.resize(350, 400)
        self.title_label = QLabel(login_dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(30, 50, 291, 81))
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        self.title_label.setFont(font)
        self.title_label.setAlignment(Qt.AlignCenter)
        self.verticalLayoutWidget = QWidget(login_dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 140, 131, 71))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setSpacing(9)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.username_field = QLineEdit(self.verticalLayoutWidget)
        self.username_field.setObjectName(u"username_field")
        self.username_field.setMinimumSize(QSize(0, 25))

        self.verticalLayout.addWidget(self.username_field)

        self.password_field = QLineEdit(self.verticalLayoutWidget)
        self.password_field.setObjectName(u"password_field")
        self.password_field.setMinimumSize(QSize(0, 25))
        self.password_field.setEchoMode(QLineEdit.Password)

        self.verticalLayout.addWidget(self.password_field)

        self.login_button = QPushButton(login_dialog)
        self.login_button.setObjectName(u"login_button")
        self.login_button.setGeometry(QRect(180, 216, 61, 25))
        self.response_label = QLabel(login_dialog)
        self.response_label.setObjectName(u"response_label")
        self.response_label.setGeometry(QRect(110, 219, 71, 16))

        self.retranslateUi(login_dialog)

        QMetaObject.connectSlotsByName(login_dialog)
    # setupUi

    def retranslateUi(self, login_dialog):
        login_dialog.setWindowTitle(QCoreApplication.translate("login_dialog", u"Login", None))
        self.title_label.setText(QCoreApplication.translate("login_dialog", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Login</span></p><p><br/></p></body></html>", None))
        self.username_field.setPlaceholderText(QCoreApplication.translate("login_dialog", u"Username", None))
        self.password_field.setPlaceholderText(QCoreApplication.translate("login_dialog", u"Password", None))
        self.login_button.setText(QCoreApplication.translate("login_dialog", u"Login", None))
        self.response_label.setText("")
    # retranslateUi

