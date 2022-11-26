import unittest
import http
import requests

class TestApi(unittest.TestCase):

    def test_correct_auth(self):
        result = False
        ask_for_auth = requests.post('http://localhost:8000/api/v1/auth/', json={'username': 'usermustpasss', 'password': 'apass123'})
        
        if ask_for_auth.status_code == http.HTTPStatus.OK:
            result = True
        
        assert(result == True)
        
        
if __name__ == '__main__':
    unittest.main()