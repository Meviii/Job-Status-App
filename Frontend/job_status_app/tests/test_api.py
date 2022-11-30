import unittest
import http
import requests
import time

class TestApi(unittest.TestCase):

    @unittest.skip("demonstrating skipping")
    def test_correct_auth(self):
        result = False
        ask_for_auth = requests.post('http://127.0.0.1:8000/api/v1/auth', json={'username': 'usermustpasss', 'password': 'apass123'})
        
        if ask_for_auth.status_code == http.HTTPStatus.OK:
            result = True
        
        assert(result == True)
        
    def test_get_users(self):
        user_data = requests.get('http://127.0.0.1:8000/api/v1/user/usermustpass').json()
        
if __name__ == '__main__':
    unittest.main()