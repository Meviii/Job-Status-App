import requests
import http

class HomeController():
    
    def __init__(self, app_user):
        self.app_user = app_user
    
    def save(self) -> bool:
        try:
            response = self._patch_user_to_server()
            if response.status_code != http.HTTPStatus.OK:
                return False
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
            return (False, "Internal Error")

        return True
    
    def _patch_user_to_server(self):
        json = self._save_user(self.app_user.get_json())
        return requests.patch(f'http://127.0.0.1:8000/api/v1/user/{self.app_user.username}', json=json)
    
    def fix_new_column_format(self, column_name):
        column_name = column_name[0].upper() + column_name[1:].lower()
        return column_name
    
    # Saves user. Does not save new password, id or activity status
    def _save_user(self, data):
        to_return = {}
        for i,x in data.items():
            if i != "password" and i != "id" and i != "is_active":
                to_return[i] = x
        return to_return