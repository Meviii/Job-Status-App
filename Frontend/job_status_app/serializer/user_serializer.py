from model.User import User

class UserSerializer():
    
    def __init__(self, json_dict) -> None:
        self.data = json_dict
        self.user = User()
        
    def map_json_to_user(self) -> User:
        try:
            for i, v in self.data.items():
                self.user.__setattr__(i, v)
        except:
            return None
        return self.user
