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
    

    class Credential:
    '''
    Class to create  account credentials, generate passwords and save their information
    '''
     # Class Variables
    credentials_list = []
    profile_credentials_list = []
    @classmethod
    def check_profile(cls, first_name, password):
        '''
        Method that checks if the name and password entered match entries in the profiles_list
        '''
        current_profile = ''
        not_in_the_system = 'Sorry Profile not found'
        for profile in Profile.profiles_list:
            if (profile.first_name == first_name and profile.password == password):
                current_profile = profile.first_name
        return current_profile
            elif 
        return not_in_the_system
    
    def __init__(self, profile_name, site_name, account_name, password):
        '''
        Method to define the properties for each profile object.
        '''

        # instance variables
        self.profile_name = profile_name
        self.site_name = site_name
        self.account_name = account_name
        self.password = password

    def save_credentials(self):
        '''
        Function to save a newly created profile instance
        '''
        # global profiles_list
        Credential.credentials_list.append(self)





