from input_helper import *
from credentials import *
from trainer import *
from sql_helper import *



def __main__():

     print("welcome yada yada")

     #print(get_email_input("Enter an email:"))
     #print(format_date(get_date_input("Date")))

     #print(format_time(get_time_input("Time")))

     

     choice = get_menu_input("What would you like to do?", ["Login", "Register"])

     match choice:
          case 0: 
               #perm is permission level (1 admin, 2 trainer, 3 member)
               #id is the id of the user from the table
               perm = loginUser(id)
               if perm == 0:
                    perm = createUser(id)
          case 1: perm = createUser(id)

     #when a admin logs in
     if perm == 1:
          exit()
     #when a trainer logs in
     if perm == 2:
          while(True):
               choice = get_menu_input("What would you like to do?", ["Search Member", "View Unavailability", "Edit Unavaility"])
               match choice:
                    case 0:
                         fname = get_text_input("What is their first name?")
                         lname = get_text_input("What is their last name?")
                         search_member(fname, lname)
                    case 1: view_unavailibility(id)
                    case 2: edit_unavailibility(id)
          

     #when a member logs in
     if perm == 3:
          exit()
          


__main__()
 
