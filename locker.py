
class User: #creates a user instance for login purposes
    
    user_list = [] #list of users willbe stored here
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        
    def save_user(self):
        User.save_user.append(self)
    












class Credentials:      #class that creates instances of passwords
    
    
    credential_list = [] #list of stored credentials will be here
    
    def __init__(self, platform, username, password):
        
        self.platform = platform
        self.username = username
        self.password = password
        
    def save_credentials (self):
        Credentials.credential_list.append(self)
        
        