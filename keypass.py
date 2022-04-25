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











if __name__ == '__main__':
    
    main()   