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
