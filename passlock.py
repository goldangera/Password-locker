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
        for profile in Profile.profiles_list:
            if (profile.first_name == first_name and profile.password == password):
                current_profile = profile.first_name
                return current_profile
        
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

    @classmethod
    def generate_password(size=8, char=string.ascii_uppercase+string.ascii_lowercase+string.digits):
        '''
        Function to generate an 8 character password for a credential
        '''
        gen_pass = ''.join(random.choice(char) for _ in range(size))
        return gen_pass

    @classmethod
    def display_credentials(cls, profile_name):
        '''
        Class method to display the list of credentials saved
        '''
        profile_credentials_list = []
        for credential in cls.credentials_list:
            if credential.profile_name == profile_name:
                profile_credentials_list.append(credential)
        return profile_credentials_list


    @classmethod
    def find_by_site_name(cls, site_name):
        '''
        Method that takes in a site_name and returns a credential that matches that site_name.
        '''
        for credential in cls.credentials_list:
            if credential.site_name == site_name:
                return credential


    @classmethod
    def copy_credential(cls, site_name):
        '''
        Class method that copies a credential's info after the credential's site name is entered
        '''
        find_credential = Credential.find_by_site_name(site_name)
        
        return pyperclip.copy(find_credential.password)
    