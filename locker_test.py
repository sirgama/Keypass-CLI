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
        
    
        
        





if __name__ == "__main__":
    unittest.main()