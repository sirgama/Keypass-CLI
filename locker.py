
class Credentials:      #class that creates instances of passwords
    
    
    credential_list = [] #list of stored credentials will be here
    
    def __init__(self, platform, username, password):
        
        self.platform = platform
        self.username = username
        self.password = password
        
    def save_credentials (self):
        Credentials.credential_list.append(self)
        
    