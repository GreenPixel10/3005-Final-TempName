from input_helper import *

from sql_helper import *



def __main__():

     print("welcome yada yada")

     #print(get_email_input("Enter an email:"))
     print(format_date(get_date_input("Date")))

     print(format_time(get_time_input("Time")))

     

     choice = get_menu_input("What would you like to do?", ["Login", "Register"])

     match choice:
          case 0: pass
          case 1: pass


__main__()
 
