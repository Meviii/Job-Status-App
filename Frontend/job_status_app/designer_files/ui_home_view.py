# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home_view.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(800, 600)
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(149, 533, 511, 51))
        self.add_job_column_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.add_job_column_layout.setObjectName(u"add_job_column_layout")
        self.add_job_column_layout.setContentsMargins(0, 0, 0, 0)
        self.add_job_button = QPushButton(Dialog)
        self.add_job_button.setObjectName(u"add_job_button")
        self.add_job_button.setGeometry(QRect(670, 538, 91, 41))
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(291, 20, 291, 81))
        self.search_line = QLineEdit(Dialog)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setGeometry(QRect(630, 94, 131, 21))
        self.jobs_button = QPushButton(Dialog)
        self.jobs_button.setObjectName(u"jobs_button")
        self.jobs_button.setGeometry(QRect(23, 130, 111, 41))
        font = QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.jobs_button.setFont(font)
        self.table_button = QPushButton(Dialog)
        self.table_button.setObjectName(u"table_button")
        self.table_button.setGeometry(QRect(23, 180, 111, 41))
        self.table_button.setFont(font)
        self.table_widget = QTableWidget(Dialog)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setGeometry(QRect(150, 120, 611, 411))
        self.status_label = QLabel(Dialog)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(675, 579, 81, 16))
        self.status_label.setAlignment(Qt.AlignCenter)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_job_button.setText(QCoreApplication.translate("Dialog", u"Add Job", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Job Applications</span></p></body></html>", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search...", None))
        self.jobs_button.setText(QCoreApplication.translate("Dialog", u"Jobs", None))
        self.table_button.setText(QCoreApplication.translate("Dialog", u"Table ", None))
        self.status_label.setText("")
    # retranslateUi

