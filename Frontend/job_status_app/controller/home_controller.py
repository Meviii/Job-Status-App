import requests
import http
from model.User import User
from model.UserAuth import UserAuth
from serializer.user_serializer import UserSerializer

cache = {}

class HomeController():
    
    def __init__(self, app_user):
        self.app_user = app_user
    
    def save(self) -> bool:
        try:
            response = self._put_user_to_server()
            if response != http.HTTPStatus.OK:
                return False
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return (False, "Internal Error")

        return True
    
    def _put_user_to_server(self):
        json = self._user_json_without_password(self.app_user.get_json())
        return requests.put(f'http://127.0.0.1:8000/api/v1/user/{self.app_user.username}', json=json)
        
    def _user_json_without_password(self, json):
        print(json)
        return json