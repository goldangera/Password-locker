from passlock import Profile, Credentials
import random

def create_profile(fname, lname, password):
    '''
    Function to create a new profile account
    '''
    new_profile = Profile(fname, lname, password)
    return new_profile


def save_profile(profile):
    '''
    Function to save a new profile account
    '''
    Profile.save_profile(profile)

def verify_profile(first_name, password):
    '''
    Function that verifies the existance of the profile before creating credentials
    '''
    checking_profile = Credential.check_profile(first_name, password)
    return checking_profile

def generate_password():
    '''
    Function to generate a password automatically
    '''
    gen_pass = Credential.generate_password()
    return gen_pass