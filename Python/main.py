from input_helper import *

from credentials import *

from user_defs import *



user = user_class(0)
          

def __main__():

     print("welcome yada yada")

     choice = get_menu_input("What would you like to do?", ["Login", "Register"])

     match choice:
          case 0: user = log_in()
          case 1: user = register()

     user.show_options(user)

__main__()
