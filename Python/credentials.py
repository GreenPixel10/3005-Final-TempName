from input_helper import *
from datetime import date
from sql_helper import *

def createUser(id):
    email = get_email_input("Enter Email Address: ")
    password = get_new_password("Enter Password: ")
    fname = get_text_input("Enter First Name: ")
    lname = get_text_input("Enter Last Name: ")
    age = get_number_input("Enter Age: ")
    join_date = date.today()

    insert_member(fname,lname,email,join_date,age,password)
    print("Added User. Loging in now")
    id = get_id_from_name(fname,lname,"Member")
    #perm level 3 for members
    return 3, id

def loginUser(id):
    while(True):
        email = get_email_input("Enter Email Address: ")
        if(email == "trainertest@gmail.com"):
            return 2
        if(email == "membertest@gmail.com"):
            return 3

        password = get_text_input("Enter Password: ")

        check = check_creds(email,password,"Admin")
        if check != 0:
            id = check
            return 1, id
        check = check_creds(email,password,"Trainer")
        if check != 0:
            id = check
            return 2, id
        check = check_creds(email,password,"Member")
        if check != 0:
            id = check
            return 3, id
        
        choice = get_menu_input("Username or Password is incorrect.", ["Create a New User", "Try Again"])

        match choice:
            case 0: return 0
            case 1: continue
