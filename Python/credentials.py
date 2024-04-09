from input_helper import *
from datetime import date

def createUser(id):
    email = get_email_input("Enter Email Address: ")
    password = get_text_input("Enter Password: ")
    fname = get_text_input("Enter First Name: ")
    lname = get_text_input("Enter Last Name: ")
    age = get_number_input("Enter Age: ")
    join_date = date.today()

    #INSERT INTO Member (first_name, last_name, email, join_date, password, age) VALUES
    #(fname, lname, email, join_date, password, age)
    print("Added User. Loging in now")
    #get their id
        #id = 
    #perm level 3 for members
    return 3

def loginUser(id):
    while(True):
        email = get_email_input("Enter Email Address: ")
        if(email == "return"):
            #send them back to the main, with "perm" 0, to send them to create user
            return 0 

        password = get_text_input("Enter Password: ")

        #check if admin has this user
            #id = 
            #return 1 (permission level)
        #check if trainer has this user
            #id = 
            #return 2 (permission level)
        #check if member has this user
            #id = 
            #return 3 (permission level)
        #if no one has this user:
        choice = get_menu_input("Username or Password is incorrect.", ["Create a New User", "Try Again"])

        match choice:
            case 0: return 0
            case 1: continue


    


