import unittest

from locker import Credentials

class TestCredentials(unittest.TestCase):
    
    def setUp(self):
        self.new_credentials = Credentials("Instagram","sirgama","42625435") #creates new credentials sample for testing purposes
        
    
    def tearDown(self):
        Credentials.credential_list = []
        
        





if __name__ == "__main__":
    unittest.main()