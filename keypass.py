#!/usr/bin/env python3.9

from locker import Credentials, User


def create_user(username, password):
    new_user = User(username, password)
    return new_user

def save_user(locker):
    locker.save_user()

def log_user(username, password):
    confirm_user = User.verify_user(username,password)
    return confirm_user

def create_credentials(platform, username, password):
    new_credentials = Credentials(platform, username, password)
    return new_credentials

def save_credentials(locker):
    locker.save_credentials()
    
def find_credential(social):
    return Credentials.find_by_platform(social)

def check_existing_credential(social):
    return Credentials.credential_exists(social)

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
    print(" To login with an existing account use: LO ")
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
            pass_option = input("").lower()
            
            if pass_option == "up":
                password = input("Enter Password:  ")
                break
            elif pass_option == "gp":
                password = "*#99108Kgh%4"
                break
            else:
                print("Kindly select a valid option")
                
        save_user(create_user(username,password))
        
        print("-_-"*100)
        print("Account created Successfully ")
        print(f"Your username is: {username}, and Password is: {password}")
        print("Kindly save your password!")
    
    elif user_code == "lo":
        print("_-_"*100)
        print(" ")
        print("Enter your Keypass username and password to proceed!")
        
        username = input("Username:  ")
        password = input("Password:   ")
        
        login = log_user(username, password)
        
        if log_user == login:
            print("_-_"*60)
            print("Hi {username}, Welcome back to Keypass!!!")
            print("----------------------------------------------")
    
    while True:
        print("Use the following codes to proceed:")
        print("")
        print("Create new credentials: NC")
        print("Display all credentials: DC")
        print("Search for a credential: SC")
        print("Delete credential: DL")
        print("Exit From Keypass:  EX")
        
        user_code = input("").lower()
        
        if user_code == "nc":
            print("Create a new credential!")
            print(".................................")
            print(".................................")
            print("Enter Application/Software name (Eg: Github)")
            platform = input("")
            print("Print your Application Username: ")
            username = input("")
            print("Your Application password: ")
            password = input("")
            
            save_credentials(create_credentials(platform,username,password))
            
            print(f"Credentials for {platform} successfully created and saved")
            
            
            print("\n")
            
        elif user_code == "dc":
            print("Here's a list of all Credentials")
            print("\n")
            for credential in display_credentials():
                print(f"Account:  {credential.platform}    Username: {username}    Password:  {password}")
                print("\n")
                print(".................................................................................")
                print("\n")
            else:
                print("No existing user credentials. Please create some")
                
                
        elif user_code == "sc":
            
            print("Let's help you search for stored  account details")
            print("\n")
            print("Kindly enter the Software/application name:")
            search_item = input("")
            if find_credential(search_item):
                search_platform = find_credential(search_item)
                print("----------------------------------------------------------")
                print(f"Application: {search_platform.platform}")
                print(f"Username: {search_platform.username}   Password: {search_platform.password}")
                print("__________________________________________________________")
            else: 
                print("The Account doesnt seem to exist")
                
        elif user_code == "dl":
            print("\n")
            print("Kindly enter the Software/application name you want to delele")
            search_item = input("")
            if find_credential(search_item):
                search_platform = find_credential(search_item)
                print("----------------------------------------------------------")
                search_platform.delete_credentials()
                print("\n")
                print(f"Application: {search_platform.platform} with its respective details have been deleted") 
                print("\n")
                
            else:
                print("Application doesn't seem to exist in our records")
                
        elif user_code == "ex":
            print("\n")
            print("Thank you for your time in KEYPASS, we hope it was of great help")
            
            break
        else:
            print("Kindly choose a valid option") 
        











if __name__ == '__main__':
    
    main()   