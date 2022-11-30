import unittest
import http
import requests
from controller.login_controller import LoginController
from model.UserAuth import UserAuth

class TestLoginController(unittest.TestCase):

    def setUp(self) -> None:
        self.auth_user = UserAuth("usermustpass", "apass123")
        self.login_controller = LoginController(self.auth_user, True)
        self.app_user = None

    def test_should_auth_user(self):
        is_authed = self.login_controller.authenticate()
        
        assert is_authed == True
    
    def test_should_get_user(self):
        self.app_user = self.login_controller.get_user()
        
        assert self.app_user != None
    
    def run_tests(self):
        unittest.main()