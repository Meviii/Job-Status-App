from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.uic import loadUi
from controller.login_controller import LoginController
from model.UserAuth import UserAuth
import view.view_loader as vl
from PyQt5.QtCore import QTimer

PATH = 'designer_files/login_view.ui'
class Ui_LoginWindow(QDialog):
    def __init__(self, widget):
        super(Ui_LoginWindow, self).__init__()
        loadUi(PATH, self)
        self.widget = widget
        self.app_user = None
        self.login_controller = LoginController()
        
        widget.setFixedHeight(400)
        widget.setFixedWidth(350)
        
        self._buttons()
        
    def _buttons(self):
        self.login_button.clicked.connect(self.login)
        
    def login(self):
        username = self.username_field.text()
        password = self.password_field.text()
        
        if self._fields_empty():
            self.response_label.setText("Empty fields.")
            return
             
        user_to_auth = UserAuth(username, password) # Create User Authentication object
        self.login_controller.user_auth = user_to_auth # Set user authentication object to login controller
        
        # Temporarily disable button to prevent API spam
        self.login_button.setEnabled(False)
        QTimer.singleShot(3000, lambda: self.login_button.setDisabled(False))
        
        if not (self.login_controller.authenticate()):
            self.response_label.setText("Wrong credentials.")
            return

        # Get user
        self.app_user = self.login_controller.get_user()

        if self.app_user == None:
            self.response_label.setText("Internal Error")
            return
        
        vl.load_home_view(self, self.app_user)
    
    def _fields_empty(self) -> bool:
        if self.username_field.text() == "" or self.password_field.text() == "":
            return True
        return False
