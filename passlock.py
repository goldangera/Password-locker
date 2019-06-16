import random 
import string 
import pyperclip

# G .list
global profiles_list

class Profile:
    '''
    Class to create and save profile information
    '''
    # Class Variables
    # global profiles_list
    profiles_list = []

    def __init__(self, first_name, sur_name, password):
        '''
        Method to define each profile object properties.
        '''

        # instance variables
        self.first_name = first_name
        self.sur_name = sur_name
        self.password = password

    def save_profile(self):
        '''
        Function to save a newly created profile instance
        '''
        Profile.profiles_list.append(self)



