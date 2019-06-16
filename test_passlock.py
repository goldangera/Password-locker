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