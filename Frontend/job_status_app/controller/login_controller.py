import requests
import http
from model.UserAuth import UserAuth
from model.User import User
from serializer.user_serializer import UserSerializer
import time
cache = {}

class LoginController():
    
    def __init__(self, user_auth=None, is_authed=False) -> None:
        self.user_auth = user_auth
        self.app_user = None
        self._is_authed = is_authed
        self._user_json = ""
    
    def get_user(self) -> User:
        
        if not self._is_authed:
            return None

        if self._is_in_cache(self._user_json):
            return UserSerializer(self._user_json).map_json_to_user()

        user_json = self._get_user_json_from_server()

        if not (self._cache_element(user_json)):
            return None
        
        # map data to object
        user = UserSerializer(user_json).map_json_to_user()
        self.app_user = user
        
        return user

    def authenticate(self) -> bool:
        try:
            auth_response = self._authentication_response()
            if auth_response.status_code == http.HTTPStatus.OK:
                self._is_authed = True
                return True
            else:
                raise Exception("User could not be authenticated")
        except Exception as e:
            return False
    
    def _cache_element(self, element) -> bool:
        if element == []:
            return False
        return True
        
    def _is_in_cache(self, element) -> bool:
        
        if element in cache:
            return True
        return False
    
    def _get_user_json_from_server(self) -> requests.Response.json:
        return requests.get(f'http://127.0.0.1:8000/api/v1/user/{self.user_auth.username}').json()
    
    def _authentication_response(self) -> requests.Response:
        return requests.post(f'http://127.0.0.1:8000/api/v1/auth',json=self.user_auth.to_json())