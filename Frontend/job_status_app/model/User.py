import string
import json

class User:    
    def __init__(self, id="", username="", password="", table_columns="", table_data="", is_active=""):
        
        self.id = id
        self.username = username
        self.password = password
        self.table_columns = table_columns
        self.table_data = table_data
        self.is_active = is_active
    
    def add_job(self, job) -> bool:
        self.table_data.append(job)
    
    def get_jobs(self) -> list:
        return self.table_data
    
    def remove_job(self, job) -> bool:
        pass
    
    def update_job(self, job) -> bool:
        pass
    
    def add_column(self, column) -> bool:
        pass
    
    def remove_column(self, column) -> bool:
        pass
    
    def get_json(self):
        data = self.__dict__
        return data
        
    def __str__(self) -> str:
        return f"User: {self.username}\nPassword: {self.password}\nTable Columns: {self.table_columns}\nTable Data: {self.table_data}\nIs Active: {self.is_active}"