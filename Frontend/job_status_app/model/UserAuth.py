import string

class UserAuth:    
    def __init__(self, username, password):
        
        self.username = username
        self.password = password
    
    def to_json(self):
        return self.__dict__
    
    def __str__(self) -> str:
        return f"User: {self.username}"