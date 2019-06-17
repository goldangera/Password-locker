#!/usr/bin/env python3.6
import random
from passlock import Profile, Credential

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

def create_credential(profile_name, site_name, account_name, password):
    '''
    Function to create a new credential
    '''
    new_credential = Credential(
        profile_name, site_name, account_name, password)
    return new_credential


def save_credential(credential):
    '''
    Function to save a newly created credential
    '''
    Credential.save_credentials(credential)


def display_credentials(profile_name):
    '''
    Function to display credentials saved by a profile
    '''
    return Credential.display_credentials(profile_name)


def copy_credential(site_name):
    '''
    Function to copy a credentials details to the clipboard
    '''
    return Credential.copy_credential(site_name)


def main():
    print(' ')
    print('Greetings! Enjoy the Password Locker experience.')
    while True:
        print(' ')
        print("-"*60)
        print(
            'Use these codes to navigate: \n cl-Create an Account \n si-Log In \n dn-Exit')
        short_code = input('Enter a choice: ').lower().strip()
        if short_code == 'dn':
            break

        elif short_code == 'cl':
            print("-"*60)
            print(' ')
            print('To create a new account:')
            first_name = input('Enter your first name - ').strip()
            sur_name = input('Enter your surname - ').strip()
            password = input('Enter your password - ').strip()
            save_profile(create_profile(first_name, sur_name, password))
            print(" ")
            print(
                f'New Account Created for: {first_name} {sur_name} using password: {password}')
        elif short_code == 'si':
            print("-"*60)
            print(' ')
            print('To login, enter your account details:')
            profile_name = input('Enter your first name - ').strip()
            password = str(input('Enter your password - '))
            profile_exists = verify_profile(profile_name, password)
            if profile_exists == profile_name:
                print(" ")
                print(
                    f'Welcome {profile_name}. Please choose an option to continue.')
                print(' ')
                while True:
                    print("-"*60)
                    print(
                        'Navigation codes: \n cc-Create a Credential \n dc-Display Credentials \n dub-Copy Password \n dn-Exit')
                    short_code = input('Enter a choice: ').lower().strip()
                    print("-"*60)
                    if short_code == 'dn':
                        print(" ")
                        print(f'Goodbye {profile_name}')
                        break
                    elif short_code == 'cc':
                        print(' ')
                        print('Enter your credential details:')
                        site_name = input('Enter the site\'s name- ').strip()
                        account_name = input(
                            'Enter your account\'s name - ').strip()
                        while True:
                            print(' ')
                            print("-"*60)
                            print(
                                'Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n dn-exit')
                            psw_choice = input(
                                'Enter an option: ').lower().strip()
                            print("-"*60)
                            if psw_choice == 'ep':
                                print(" ")
                                password = input(
                                    'Enter your password: ').strip()
                                break
                            elif psw_choice == 'gp':
                                password = generate_password()
                                break
                            elif psw_choice == 'dn':
                                break
                            else:
                                print('Kindly choose the correct option.')
                        save_credential(create_credential(
                            profile_name, site_name, account_name, password))
                        print(' ')
                        print(
                            f'Credential Created: Site Name: {site_name} - Account Name: {account_name} - Password: {password}')
                        print(' ')
                    elif short_code == 'dc':
                        print(' ')
                        if display_credentials(profile_name):
                            print('Here is a list of all your credentials')
                            print(' ')
                            for credential in display_credentials(profile_name):
                                print(
                                    f'Site Name: {credential.site_name} - Account Name: {credential.account_name} - Password: {credential.password}')
                            print(' ')
                        else:
                            print(' ')
                            print("No saved credentials have been found")
                            print(' ')
                    elif short_code == 'dub':
                        print(' ')
                        chosen_site = input(
                            'Enter the site name for the credential password to copy: ')
                        copy_credential(chosen_site)
                        print('')
                    else:
                        print('Kindly choose the correct option')

            else:
                print(' ')
                print('Sorry, wrong input . Try again or Create an Account.')

        else:
            print("-"*60)
            print(' ')
            print('Kindly choose the correct option.')


if __name__ == '__main__':
    main()
