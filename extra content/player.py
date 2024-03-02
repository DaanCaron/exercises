class Player:
     
    def __init__(self, name, token):
        self.name = name
        self.token = token

    @property
    def name(self):
        return self.__name
    

    @name.setter
    def name(self, name):
        self.__name = name
    
    @property
    def token(self):
        return self.__token

    @token.setter
    def token(self, token):
        self.__token = token
    
    def __str__(self):
        return f"Player {self.name} will play with token {self.token}."