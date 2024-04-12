from input_helper import *
from sql_helper import *
import random


def update_personal_info(id):
    print()
    options = ["First name", "Last Name", "Email", "Password", "Age", "Cancel (Go Back)"]
    while True:
        print_member_info(id)
        choice = get_menu_input("What would you like to update?", options)

        match choice:
            case 0:
                update_profile_first_name(id)
            case 1:
                update_profile_last_name(id)
            case 2:
                update_profile_email(id)
            case 3:
                update_profile_password(id)
            case 4:
                update_profile_age(id)
            case 5:
                return

def update_profile_first_name(id):
    fname = get_text_input("Enter the new first name")
    update_userinfo_field(id, "first_name", fname)

def update_profile_last_name(id):
    lname = get_text_input("Enter the new last name")
    update_userinfo_field(id, "last_name", lname)

def update_profile_email(id):
    email = get_email_input('Enter your new email')
    if email_confirm(email):
        print("Success!")
        update_userinfo_field(id, "email", email)
    else:
        print("Sorry, we could not verify that email address.")

def update_profile_age(id):
    age = get_number_input("Enter your new age", 0, 1000)
    update_userinfo_field(id, "age", age)

def update_profile_password(id):
    email = "" #get email from database
    print("\nBefore updating your password, we must perform quick security check.")
    if email_confirm(email):
        print("Success!")
        print()
        password = get_new_password("Enter your new password:")
        update_userinfo_field(id, "password", password)
    else:
        print("Sorry, we could not verify that email address.")

def email_confirm(address):
    code = str(random.randint(100000, 999999))
    print("\nSending a confirmation email to", address)
    #send email, if this was functional
    print("The email contains a 6 digit security code (hint: " + code + ")" )
    return get_text_input("Enter the code to continue")


def fitness_goals(id):
    print()
    options = ["Add Goal", "Update Goal", "Delete Goal", "Cancel (Go Back)"]
    options_limited = ["Add Goal", "Cancel (Go Back)"]
    while True:
        goals = get_goals(id)
        display_goals(goals)

        choice = get_menu_input("What would you like to do?", options if len(goals) > 0 else options_limited)

        match choice:
            case 0:
                add_goal(id)
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
        print(str(g)+">", "{}: Target {}, Current Best {}".format(goals[g][3], goals[g][2], goals[g][1]))
    print()


def add_goal(id):
    type = get_text_input("What type of goal are you setting (e.g. \"Pounds deadlifted\")", 100)
    val = get_number_input("What value are you aiming for (e.g. \"150\")", 1, 1000000000)
    add_goal_sql(id, type, val)
    print()

def update_goal():
    pass #should we include this

def delete_goal():
    pass




def exercise_logging():
    pass
