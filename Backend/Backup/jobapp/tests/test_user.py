from django.test import TestCase
from ..model.models import User

class TestUser(TestCase):
    
    def setUp(self) -> None:
        User.objects.create(username="test", password="test", table_columns="test", table_data="test")
    
    # def test_create_user(self):
    #     user = User.objects.create(username="test2", password="test", table_columns="test", table_data="test")
    #     self.assertEqual(user.username, "test2")
        
    def test_delete_user(self):
        self.assertEqual(0, 1)
    
    # def test_update_user(self):
    #     pass
    
    # def test_add_table_col(self):
    #     pass
    
    # def test_add_table_data(self):
    #     pass

    # def test_get_table_data(self):
    #     pass