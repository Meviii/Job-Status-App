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
        self.horizontalLayoutWidget.setGeometry(QRect(169, 533, 511, 51))
        self.add_job_column_layout = QHBoxLayout(self.horizontalLayoutWidget)
        self.add_job_column_layout.setObjectName(u"add_job_column_layout")
        self.add_job_column_layout.setContentsMargins(0, 0, 0, 0)
        self.add_job_button = QPushButton(Dialog)
        self.add_job_button.setObjectName(u"add_job_button")
        self.add_job_button.setGeometry(QRect(690, 538, 91, 41))
        self.title_label = QLabel(Dialog)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(291, 20, 291, 81))
        self.search_line = QLineEdit(Dialog)
        self.search_line.setObjectName(u"search_line")
        self.search_line.setGeometry(QRect(650, 94, 131, 21))
        self.status_label = QLabel(Dialog)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setGeometry(QRect(675, 579, 81, 16))
        self.status_label.setAlignment(Qt.AlignCenter)
        self.scrollArea = QScrollArea(Dialog)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setGeometry(QRect(170, 120, 611, 411))
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 609, 409))
        self.table_widget = QTableWidget(self.scrollAreaWidgetContents)
        self.table_widget.setObjectName(u"table_widget")
        self.table_widget.setGeometry(QRect(-1, -1, 611, 411))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.columns_combo_box = QComboBox(Dialog)
        self.columns_combo_box.setObjectName(u"columns_combo_box")
        self.columns_combo_box.setGeometry(QRect(20, 150, 131, 21))
        self.columns_combo_box.setEditable(False)
        self.column_delete_button = QPushButton(Dialog)
        self.column_delete_button.setObjectName(u"column_delete_button")
        self.column_delete_button.setGeometry(QRect(48, 180, 75, 23))
        self.table_label = QLabel(Dialog)
        self.table_label.setObjectName(u"table_label")
        self.table_label.setGeometry(QRect(7, 110, 161, 31))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.table_label.setFont(font)
        self.new_column_line_edit = QLineEdit(Dialog)
        self.new_column_line_edit.setObjectName(u"new_column_line_edit")
        self.new_column_line_edit.setGeometry(QRect(20, 220, 131, 20))
        self.add_new_col_button = QPushButton(Dialog)
        self.add_new_col_button.setObjectName(u"add_new_col_button")
        self.add_new_col_button.setGeometry(QRect(49, 250, 75, 23))
        self.delete_rows_button = QPushButton(Dialog)
        self.delete_rows_button.setObjectName(u"delete_rows_button")
        self.delete_rows_button.setGeometry(QRect(554, 93, 91, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.add_job_button.setText(QCoreApplication.translate("Dialog", u"Add Job", None))
        self.title_label.setText(QCoreApplication.translate("Dialog", u"<html><head/><body><p><span style=\" font-size:24pt; font-weight:600;\">Job Applications</span></p></body></html>", None))
        self.search_line.setPlaceholderText(QCoreApplication.translate("Dialog", u"Search...", None))
        self.status_label.setText("")
        self.columns_combo_box.setCurrentText("")
        self.columns_combo_box.setPlaceholderText("")
        self.column_delete_button.setText(QCoreApplication.translate("Dialog", u"Delete", None))
        self.table_label.setText(QCoreApplication.translate("Dialog", u"Table Management", None))
        self.new_column_line_edit.setPlaceholderText(QCoreApplication.translate("Dialog", u"New Column..", None))
        self.add_new_col_button.setText(QCoreApplication.translate("Dialog", u"Add", None))
        self.delete_rows_button.setText(QCoreApplication.translate("Dialog", u"Delete ALL Rows", None))
    # retranslateUi

