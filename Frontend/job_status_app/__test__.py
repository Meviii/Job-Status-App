from model.User import User
from model.UserAuth import UserAuth
from serializer import user_serializer
from controller.home_controller import HomeController
from tests.test_home_controller import TestHomeController
from tests.test_login_controller import TestLoginController

def test_login_controller():
    tlc = TestLoginController()
    tlc.run_tests()

def test_home_controller():
    pass
    
def test_user_serializer():
    to_serialize = {"id":1,
                    "username":"newuser1",
                    "password":"pbkdf2_sha256$390000$HlYXD1qEW5zHO4o22yenhi$PFoO59Q64Y61nyYUJttUnSATUp25u4GQWxwHYysVuog=",
                    "table_columns":"cols",
                    "table_data":"data",
                    "is_active":True}
    
    user = user_serializer.UserSerializer(to_serialize).map_json_to_user()
    print(user)

if __name__ == "__main__":
    
    test_login_controller()