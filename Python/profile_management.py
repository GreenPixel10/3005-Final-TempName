from input_helper import *
import random


def update_personal_info():
    print()
    options = ["First name", "Last Name", "Email", "Password", "Age", "Cancel (Go Back)"]
    while True:
        print()
        choice = get_menu_input("What would you like to update?", options)

        match choice:
            case 0:
                update_profile_first_name()
            case 1:
                update_profile_last_name()
            case 2:
                update_profile_email()
            case 3:
                update_profile_password()
            case 4:
                update_profile_age()
            case 5:
                return

def update_profile_first_name():
    fname = get_text_input("Enter the new first name")
    #update account
def update_profile_last_name():
    lname = get_text_input("Enter the new last name")
    #update account

def update_profile_email():
    email = get_email_input('Enter your new email')
    if email_confirm(email):
        print("Success!")
        #update account
    else:
        print("Sorry, we could not verify that email address.")

def update_profile_age():
    age = get_number_input("Enter your new age", 0, 1000)
    #update account

def update_profile_password():
    email = "" #get email from database
    print("\nBefore updating your password, we must perform quick security check.")
    if email_confirm(email):
        print("Success!")
        print()
        password = get_new_password("Enter your new password:")
        #update account
    else:
        print("Sorry, we could not verify that email address.")

def email_confirm(address):
    code = str(random.randint(100000, 999999))
    print("\nSending a confirmation email to", address)
    #send email, if this was functional
    print("The email contains a 6 digit security code (hint: " + code + ")" )
    return get_text_input("Enter the code to continue")


def fitness_goals():
    print()
    options = ["Add Goal", "Update Goal", "Delete Goal", "Cancel (Go Back)"]
    options_limited = ["Add Goal", "Cancel (Go Back)"]
    while True:
        #select * from goals where id = id
        goals = []
        display_goals(goals)

        choice = get_menu_input("What would you like to do?", options if len(goals) > 0 else options_limited)

        match choice:
            case 0:
                add_goal()
            case 1:
                update_goal()
            case 2:
                delete_goal()
            case 3:
                return


def display_goals(goals):

    if len(goals) == 0:
        print("You have no goals set!\n")
        return

    for g in range(len(goals)):
        print(str(g)+":", goals[g][0], goals[g][0], goals[g][0]) #update with proper formatting
    print()


def add_goal():
    type = get_text_input("What type of goal are you setting (e.g. \"Pounds deadlifted\")", 100)
    val = get_number_input("What value are you aiming for (e.g. \"150\")", 1, 1000000000)
    #add

def update_goal():
    pass #should we include this

def delete_goal():
    pass

def excercise_logging():
    pass
