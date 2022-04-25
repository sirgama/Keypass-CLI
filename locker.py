


class User: #creates a user instance for login purposes
    
    user_list = [] #list of users willbe stored here
    
    def __init__(self,username,password):
        self.username = username
        self.password = password
        
        
    def save_user(self):
        User.user_list.append(self)
        
    @classmethod
    def verify_user(cls, username, password):
        userinstance = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                userinstance = username
        return userinstance
        
    




class Credentials:      #class that creates instances of passwords
    
    
    credential_list = [] #list of stored credentials will be here
    
    def __init__(self,platform,username,password):
        
        self.platform = platform
        self.username = username
        self.password = password
        
    def save_credentials (self):
        Credentials.credential_list.append(self)
        
    def delete_credentials (self):
        Credentials.credential_list.remove(self)
        
    @classmethod
    def display_credentials (cls):
         return cls.credential_list
     
    @classmethod
    def find_by_platform (cls, social):
        for media_platform in cls.credential_list:
            if media_platform.platform == social:
                return media_platform
    
    @classmethod
    def display_credentials(cls):
        return cls.credential_list