from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from controller.home_controller import HomeController
import view.view_loader as view_loader

PATH = 'designer_files/home_view.ui'
class Ui_HomeWindow(QDialog):
    def __init__(self, widget, app_user):
        super(Ui_HomeWindow, self).__init__()
        loadUi(PATH, self)
        self.widget = widget
        self.app_user = app_user
        self._home_controller = HomeController(self.app_user)
        self._table_QlineEdits = []
        
        # Display Settings
        widget.setWindowTitle("Home - Job Status App")
        widget.setFixedHeight(600)
        widget.setFixedWidth(800)
        
        # load columns for add job section
        self._load_columns_for_add_job()
        
        # load table data
        self._load_table_data()
        
        # load columns into table management
        self._load_columns_for_table_management()
        
        # Initialize buttons
        self._buttons()
        
    def _buttons(self):
        self.add_job_button.clicked.connect(self.add_job)
        self.table_widget.itemChanged.connect(self.update_table_data)
        self.column_delete_button.clicked.connect(self.delete_column)
        self.add_new_col_button.clicked.connect(self.add_column)
        self.delete_rows_button.clicked.connect(self.delete_rows)
        
    def delete_rows(self):
        self.app_user.table_data = []
        if not self._save_user():
            self.status_label.setText("Error Saving.")
        
        self._load_table_data()
    
    def delete_column(self):
        for i in self.app_user.table_columns:
            if i.lower() == self.columns_combo_box.currentText().lower():
                self.app_user.table_columns.remove(i)
                break
            
        if not self._save_user():
            self.status_label.setText("Error Saving.")
        
        view_loader.load_home_view(self, self.app_user)
        
    def add_column(self):
        new_column = self._home_controller.fix_new_column_format(self.new_column_line_edit.text())
        self.app_user.table_columns.append(new_column)
        
        if not self._save_user():
            self.status_label.setText("Error Saving.")
    
        view_loader.load_home_view(self, self.app_user)
        
    def _load_columns_for_table_management(self):
        for i in self.app_user.table_columns:
            self.columns_combo_box.addItem(i)
        
    def update_table_data(self, item):
        
        # Update specific entry in table data in app_user
        for i, job in enumerate(self.app_user.table_data):
            for v, entry in enumerate(job):
                if i == item.row() and v == item.column():
                    self.app_user.table_data[i][v] = item.text()
                    
                    # Save user to server
                    if not self._save_user():
                        self.status_label.setText("Error Saving.")
        
    def _load_columns_for_add_job(self):
        cols = self.app_user.table_columns
        
        if len(cols) == 0:
            self.add_job_button.setEnabled(False)    
            return
        
        for idx in range(len(cols)):
            # label
            self.add_job_column_layout.addWidget(QLabel(cols[idx]))
            
            # line edit
            qline_edit = QLineEdit()
            qline_edit.setObjectName(f"line_edit_{cols[idx]}")
            self._table_QlineEdits.append(qline_edit)
            self.add_job_column_layout.addWidget(qline_edit)
        
    def _load_table_data(self):
        self.table_widget.setColumnCount(len(self.app_user.table_columns))              # set number of columns
        self.table_widget.setRowCount(len(self.app_user.table_data))                    # set number of rows
        self.table_widget.setHorizontalHeaderLabels(self.app_user.table_columns)        # set column headers
            
        for i, job in enumerate(self.app_user.table_data):
            for x, entry in enumerate(job):
                self.table_widget.setItem(i, x, QTableWidgetItem(entry))
        
        self.table_widget.horizontalHeader().setStretchLastSection(True)                # stretch last column to fill table
        self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # stretch all columns to fill table
        
    def add_job(self):
        job_to_add = []
        for job_column_line_edit in self._table_QlineEdits:
            job_to_add.append(job_column_line_edit.text())
        self.app_user.table_data.append(job_to_add)
        
        if not self._home_controller.save(): # update user
            self.status_label.setText("Error.")
            
        self._table_QlineEdits.clear()  # clear line edits
        self._load_table_data()         # reload table data
        
    def search_function():
        pass
    
    def _search_by_option():
        pass
    
    def _table_view():
        pass
    
    def _jobs_view():
        pass
    
    def _save_user(self) -> bool:
        if not self._home_controller.save():
            return False
        return True