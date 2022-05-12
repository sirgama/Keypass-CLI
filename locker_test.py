import unittest

from locker import Credentials, User

class TestUser(unittest.TestCase):
    """
    A Test class that defines test cases for the User class.
    """
    def setUp(self):
        """
        Method that runs before each individual test methods run.
        """
        self.new_user = User("sirgama","42625435")
        
    def tearDown(self):
        """
        Method that initiates an empty array.
        """
        User.user_list = []
        
    def test_init(self):
        """
        test case to chek if the object has been initialized correctly
        """
        self.assertEqual(self.new_user.username, "sirgama")
        self.assertEqual(self.new_user.password,"42625435")
        
    def test_save_user(self):
        """
        test case to test if a new user instance has been saved into the User list

        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),1)
 
      

class TestCredentials(unittest.TestCase):
    """
    A test class that defines test cases for credentials class

    """ 
    
    def setUp(self):
        """
        Method that runs before each individual credentials test methods run.

        """
        self.new_credentials = Credentials("Instagram","sirgama","42625435") #creates new credentials sample for testing purposes
        
    
    def tearDown(self):
        
        Credentials.credential_list = []
        
       
    def test_init(self):
        """
        Test case to check if a new Credentials instance has been initialized correctly
        """
        self.assertEqual(self.new_credentials.platform,"Instagram")
        self.assertEqual(self.new_credentials.username,"sirgama")
        self.assertEqual(self.new_credentials.password,"42625435")
        
    def test_save_credentials(self):
        self.new_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_delete_credentials(self):
        """
        test case to test if the credential object is saved into the credentials list.

        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","Stella","12345")
        test_credentials.save_credentials()
                
        
        self.new_credentials.delete_credentials()
        self.assertEqual(len(Credentials.credential_list),1)
        
    def test_save_multiple_credentials(self):
        '''
        test to check if we can save multiple credentials objects to our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credentials = Credentials("Twitter","Stella","12345")
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credential_list),2)
        
    def test_find_credentials_by_platform(self):
        '''
        test to check if we can find credentials objects from our credentials list
        '''
        self.new_credentials.save_credentials()
        test_credential = Credentials("Twitter","Stella","12345")
        test_credential.save_credentials()
        
        found_platform = Credentials.find_by_platform("Twitter")
        self.assertEqual(found_platform.username, test_credential.username)
        
    def test_display_credentials(self):
        '''
        method that displays all the credentials that has been saved by the user
        '''
        self.assertEqual(Credentials.display_credentials(), Credentials.credential_list)
        





if __name__ == "__main__":
    unittest.main()