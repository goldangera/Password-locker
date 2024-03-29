import pyperclip
import unittest
from passlock import Profile, Credential

class TestProfile(unittest.TestCase):
     '''
    Test class that defines test cases for the profile class behaviours.
    Args:
        unittest.TestCase: helps in creating test cases
    '''

    def setUp(self):
        '''
        Function to create a profile account before each test
        '''
        self.new_profile = Profile('golda', 'nkirote', 'golda6888')

    def test__init__(self):
        '''
        Test to if check the initialization/creation of profile instances is properly done
        '''
        self.assertEqual(self.new_profile.first_name, 'golda')
        self.assertEqual(self.new_profile.sur_name, 'nkirote')
        self.assertEqual(self.new_profile.password, 'golda6888')
    
    def test_save_profile(self):
        '''
        Test to check if the new profiles info is saved into the profiles list
        '''
        self.new_profile.save_profile()
        self.assertEqual(len(Profile.profiles_list), 1)

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    Args:
        unittest.TestCase: helps in creating test cases
    '''
    def test_check_profile(self):
        '''
        Function to test whether the login function check_profile works as expected
        '''
        self.new_profile = Profile('golda', 'nkirote', 'golda6888')
        self.new_profile.save_profile()
        profile2 = Profile('golda', 'nkirote', 'golda6888')
        profile2.save_profile()

        for profile in Profile.profiles_list:
            if profile.first_name == profile2.first_name and profile.password == profile2.password:
                current_profile = profile.first_name
        return current_profile

        self.assertEqual(current_profile, Credential.check_profile(
            profile2.password, profile2.first_name))

    def setUp(self):
        '''
        Function to create an account's credentials before each test
        '''
        self.new_credential = Credential(
            'golda', 'Instagram', 'test', 'golda6888') 
    def test__init__(self):
        '''
        Test to if check the initialization/creation of credential instances is properly done
        '''
        self.assertEqual(self.new_credential.profile_name, 'golda')
        self.assertEqual(self.new_credential.site_name, 'Instagram')
        self.assertEqual(self.new_credential.account_name, 'test')
        self.assertEqual(self.new_credential.password, 'golda6888')
    def test_save_credentials(self):
        '''
        Test to check if the new credential info is saved into the credentials list
        '''
        self.new_credential.save_credentials()
        twitter = Credential('golda', 'Twitter', 'works', 'golda6888')
        twitter.save_credentials()
        self.assertEqual(len(Credential.credentials_list), 2)

    def tearDown(self):
        '''
        Function to clear the credentials list after every test
        '''
        Credential.credentials_list = []
        Profile.profiles_list = []

    def test_display_credentials(self):
        '''
        Test to check if the display_credentials method, displays the correct credentials.
        '''
        self.new_credential.save_credentials()
        twitter = Credential('golda', 'Twitter', 'works', 'golda6888')
        twitter.save_credentials()
        gmail = Credential('golda', 'Gmail', 'send', 'golda6888')
        gmail.save_credentials()
        self.assertEqual(
            len(Credential.display_credentials(twitter.profile_name)), 3)
    def test_find_by_site_name(self):
        '''
        Test to check if the find_by_site_name method returns correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('golda', 'Twitter', 'works', 'golda6888')
        twitter.save_credentials()
        credential_exists = Credential.find_by_site_name('Twitter')
        self.assertEqual(credential_exists, twitter)

    def test_copy_credential(self):
        '''
        Test to check if the copy a credential method copies correct credential
        '''
        self.new_credential.save_credentials()
        twitter = Credential('golda', 'Twitter', 'works', 'golda6888')
        twitter.save_credentials()
        find_credential = None
        for credential in Credential.profile_credentials_list:
            find_credential = Credential.find_by_site_name(
                credential.site_name)
            return pyperclip.copy(find_credential.password)
        Credential.copy_credential(self.new_credential.site_name)
        self.assertEqual('golda6888', pyperclip.paste())
        print(pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
