class User:
    def __init__(self, username: str, password: str):
        self.__username = username
        self.__password_hash = hash(password)
    
    @property
    def username(self) -> str:
        return self.__username
    
    @property
    def password(self):
        raise NotImplementedError
    
    @password.setter
    def password(self, new_password: str):
        self.__password_hash = hash(password)

