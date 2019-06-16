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

