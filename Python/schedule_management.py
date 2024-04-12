from input_helper import *
from sql_helper import *
from format_helper import *
import random

def schedule_management(id):
    while True:
        print()
        choice = get_menu_input("What would you like to do?", ["View registrations", "New registration", "Cancel registration", "Back to main menu"])

        match choice:
            case 0:
                display_sessions(id)
            case 1:
                add_session(id)
            case 2:
                remove_session(id)
            case 3:
                return


def display_sessions(id):
    sessions = get_sessions(id)
    if len(sessions) == 0:
        print("\nYou are not signed up for any sessions\n")
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


def remove_session(id):
    sessions = get_sessions(id)
    if len(sessions) == 0:
        print("You are not signed up for any sessions\n")
        return

    print()

    for s in range(len(sessions)):
        print(s+1, ">", end = "")
        display_session(sessions[s])

    choice = get_number_input("Enter an number to cancel that session", 1, len(sessions))
    cancel_session(id, sessions[choice-1][0])
    print("Refunding...")
    print("Cancellation successful")
