import random
import string
import pyperclip

class User: 
    """
    Create User class that generates new instances users.

    """
    
    user_list = [] 
    
    def __init__(self,username,password):
        """
        method that defines the properties of a user.
        """
        self.username = username
        self.password = password
        
        
    def save_user(self):
        """
        A method that saves a new user instace into the user list
        """
        User.user_list.append(self)
        
    @classmethod
    def verify_user(cls, username, password):
        """
        A method that verifies if the user exists in the user list the user list
        """
        userinstance = ""
        for user in User.user_list:
            if(user.username == username and user.password == password):
                userinstance = username
        return userinstance
        
    




class Credentials:  
    
    """
    Create credentials class to help create new objects of credentials
    """
    credential_list = [] #list of stored credentials will be here
    
    def __init__(self,platform,username,password):
        """
        method that defines user credentials to be stored
        """
        
        self.platform = platform
        self.username = username
        self.password = password
        
    def save_credentials (self):
        """
        method to store a new credential to the credentials list
        """
        Credentials.credential_list.append(self)
        
    def delete_credentials (self):
        """
        delete_accounts method that deletes an account credentials from the accounts
        """
        Credentials.credential_list.remove(self)
        
    @classmethod
    def display_credentials (cls):
         return cls.credential_list
     
    @classmethod
    def find_by_platform (cls, social):
        """
        Method that takes in a account_name and returns a credential that matches that account_name.

        """
        for media_platform in cls.credential_list:
            if media_platform.platform == social:
                return media_platform
    @classmethod
    def copy_password(cls,social):
        """
        Method that will be used to copy a password.

        """
        found_accounts = Credentials.find_credential(social)
        pyperclip.copy(found_accounts.password)
    
    
    @classmethod
    def check_existing_credential (cls, social):
        for media_platform in cls.credential_list:
            if media_platform.platform == social:
                return True
        return False
    
    @classmethod
    def display_credentials(cls):
        """
        Method that returns all items in the credentials list

        """
        return cls.credential_list
    
    