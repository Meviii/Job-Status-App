from model.User import User
from model.UserAuth import UserAuth
from serializer import user_serializer
from controller.home_controller import HomeController
from tests.test_home_controller import TestHomeController
from tests.test_login_controller import TestLoginController
from PyQt5 import QtWidgets
import sys
import view.home_view as home_view

def test_login_controller():
    tlc = TestLoginController()
    tlc.run_tests()

def test_home_controller():
    pass
    
def test_user_serializer():
    to_serialize = {"id" : 1,
                    "username" : "newuser1",
                    "password" : "pbkdf2_sha256$390000$HlYXD1qEW5zHO4o22yenhi$PFoO59Q64Y61nyYUJttUnSATUp25u4GQWxwHYysVuog=",
                    "table_columns": ["Role", "Company", "Status"],
                    "table_data": [["Software Engineer", "Google", "Applied"],
                                   ["Software Engineer", "Facebook", "Applied"]],
                    "is_active": True}
    user = user_serializer.UserSerializer(to_serialize).map_json_to_user()
    return user

def _get_dummy_user():
    to_serialize = {"id" : 1,
                    "username" : "user1",
                    "password" : "admin",
                    "table_columns": ["Role", "Company", "Status"],
                    "table_data": [["Software Engineer", "Google", "Applied"],
                                   ["Software Engineer", "Facebook", "Applied"]],
                    "is_active": True}
    
    return user_serializer.UserSerializer(to_serialize).map_json_to_user()

def test_home_view():
    app_user = _get_dummy_user()
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    main = home_view.Ui_HomeWindow(widget, app_user)
    widget.addWidget(main)
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    
    test_home_view()
    # test_user_serializer()