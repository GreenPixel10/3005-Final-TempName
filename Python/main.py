from input_helper import *
from credentials import *
from trainer import *
from profile_management import *
from schedule_management import *
from dashboard_display import *
from sql_helper import *
from admin import *


debug = True

def __main__():
     id = 1
     while True:

         if debug:
             id = 3
             perm = 3
         else:
             choice = get_menu_input("\nWhat would you like to do?", ["Login", "Register", "Exit"])

             match choice:
                  case 0:
                       #perm is permission level (1 admin, 2 trainer, 3 member)
                       #id is the id of the user from the table
                       perm, id = loginUser(id)
                       if perm == 0:
                            perm, id = createUser(id)
                  case 1: perm, id = createUser(id)
                  case 2: exit()

         while True:
             #when a admin logs in
             if perm == 1:

                   choice = get_menu_input("\nWhat would you like to do?", ["Room Booking Management","Monitor Equipment","View Billing History", "Log Out"])
                   match choice:
                        case 0: manage_rooms()
                        case 1: monitor_equipment()
                        case 2: view_billing()
                        case 3: break
             #when a trainer logs in
             if perm == 2:

                   choice = get_menu_input("\nWhat would you like to do?", ["Search Member", "View Unavailability", "Edit Unavaility", "Log Out"])
                   match choice:
                        case 0:
                             fname = get_text_input("What is their first name?")
                             lname = get_text_input("What is their last name?")
                             search_member(fname, lname)
                        case 1: view_unavailibility(id)
                        case 2: edit_unavailibility(id)
                        case 3: break

             #when a member logs in
             if perm == 3:
                   choice = get_menu_input("\nWhat would you like to access?", ["Personal information", "Fitness goals", "Exercise Logging", "Dashboard Display", "Schedule Management", "Log Out"])
                   match choice:
                        case 0: update_personal_info(id)
                        case 1: fitness_goals(id)
                        case 2: exercise_logging(id)
                        case 3: dashboard(id)
                        case 4: schedule_management(id)
                        case 5: break

__main__()
