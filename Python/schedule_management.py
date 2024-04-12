from input_helper import *
from sql_helper import *
from format_helper import *
import random

def schedule_management(id):
    while True:
        print()
        choice = get_menu_input("What would you like to do?", ["View registrations", "New registration", "Back to main menu"])

        match choice:
            case 0:
                display_sessions(id)
            case 1:
                add_session(id)
            case 2:
                return


def display_sessions(id):
    sessions = get_sessions(id)
    if len(sessions) == 0:
        print("You are not signed up for any sessions\n")
        return

    print()
    for s in sessions:
        display_session(s)


def add_session(id):
    num_sessions = print_sessions()
    if num_sessions == 0:
        print("No sessions for you!")
        return

    choice = get_number_input("Enter an ID to sign up for that session")
    buy_session(id, choice)
    print("Billing...")
    print("Transaction successful!")
