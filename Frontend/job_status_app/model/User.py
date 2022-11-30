import string

class User:    
    def __init__(self, id="", username="", password="", table_columns="", table_data="", is_active=""):
        
        self.id = id
        self.username = username
        self.password = password
        self.table_columns = table_columns
        self.table_data = table_data
        self.is_active = is_active
    
    def __str__(self) -> str:
        return f"User: {self.username}\nPassword: {self.password}\nTable Columns: {self.table_columns}\nTable Data: {self.table_data}\nIs Active: {self.is_active}"