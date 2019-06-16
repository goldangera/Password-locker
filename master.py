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