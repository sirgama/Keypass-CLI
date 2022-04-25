#!/usr/bin/env python3.9

from locker import Credentials, User


def create_user(username, password):
    new_user = User(username, password)
    return new_user

def save_user(locker):
    locker.save_user()

def create_credentials(platform, username, password):
    new_credentials = Credentials(platform, username, password)
    return new_credentials

def save_credentials(locker):
    locker.save_credentials()
    
def find_credential(social):
    return Credentials.find_by_platform(social)

def delete_credential(locker):
    locker.delete_credentials()
    
def display_credentials():
    return Credentials.display_credentials()


def main():
    print("                                                                                     ")
    print("-----------------------------Welcome to KEYPASS!!!-----------------------------------")
    print("-----------------------The command line password saving tool-------------------------")
    print("--------------------                                           ----------------------")
    print("----------------                                                   ------------------")
    print("------------                                                          ---------------")
    print("---------                                                                 -----------")
    print("                                                                                     ")
    print("                                                                                     ")
    print("                                                                                     ")
    print("                                                                                     ")
    
    print("Hello, Keypass helps you to store your credentials in a safe place")
    print("Use these commands to proceed to your keypass account")
    print("                                                                   ")
    print(" To create account use: CA ")
    print("                                                                   ")
    print("                                                                   ")
    
    user_code = input("").lower().strip()
    
    if user_code == "ca":
        
        print("To Create Account, Kindly fill the following:")
        
        username = input("Enter Username:  ")
        print("---------------------------------")
        
        while True:
            print("                                                                   ")
            print("Use the following codes to proceed:")
            print("UP: Use your own password \n GP: Let keypass generate a random password for you")
            pass_option = input("").lower().strip()
            
            if pass_option == "up":
                password = input("Enter Password:  ")
                break
            elif pass_option == "gp":
                password = "*#99108Kgh%4"
                break
            else:
                print("Kindly select a valid option")











if __name__ == '__main__':
    
    main()   