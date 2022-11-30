import requests
import http
from model.User import User
from model.UserAuth import UserAuth
from serializer.user_serializer import UserSerializer

cache = {}

class HomeController():
    
    def __init__(self, app_user):
        pass
        