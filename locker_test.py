import unittest

from locker import Credentials

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