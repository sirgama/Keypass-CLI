import unittest

from locker import Credentials, User

class TestUser(unittest.TestCase):
    def setUp(self):
        self.new_user = User("sirgama","42625435")
        
    def tearDown(self):
        User.user_list = []
        
    def test_init(self):
        self.assertEqual(self.new_user.username, "sirgama")
        self.assertEqual(self.new_user.password,"42625435")
        
    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
 
        
        
        
        
        
        
        
        
        
        

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials("Instagram","sirgama","42625435") #creates new credentials sample for testing purposes
        
    
    def tearDown(self):
        Credentials.credential_list = []
        
       
    def test_init(self):
        self.assertEqual(self.new_credentials.platform,"Instagram")
        self.assertEqual(self.new_credentials.username,"sirgama")
        self.assertEqual(self.new_credentials.password,"42625435")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_delete_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","Stella","12345")
        test_credentials.save_credentials()
                
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_save_multiple_credentials(self):
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","Stella","12345")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)
        
    def test_find_credentials_by_platform(self):
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","Stella","12345")
        test_credential.save_credentials()
        
        found_platform = Credentials.find_by_platform("Twitter")
        self.assertEqual(found_platform.username, test_credential.username)
        
    def test_display_credentials(self):
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)
        





if __name__ == "__main__":
    unittest.main()