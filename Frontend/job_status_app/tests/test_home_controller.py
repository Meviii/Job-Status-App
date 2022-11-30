import unittest
import http
import requests
from controller.home_controller import HomeController
from model.UserAuth import UserAuth
from model.User import User

class TestHomeController(unittest.TestCase):
    
    @unittest.skip("Not implemented")
    def setUp(self) -> None:
        app_user = User("1", )
        self.home_controller = HomeController(self.app_user, True)