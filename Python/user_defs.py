from input_helper import *


class user_class:
     user_type = 0
     menu = ["not logged in bozo"]
     def __init__(self, user_type):
          self.user_type = user_type
          
     def execute_option(self, choice):
          pass

     def show_options(self):
          self.execute_option(self, get_menu_input("etst", self.menu))



class member(user_class):
     menu = ["member option", "another"]
     
     def execute_option(self, choice):
          match choice:
               case 0: print("do option 0")
               case 1: print("do option 1")


class trainer(user_class):
     menu = ["trainer option", "another"]

     def execute_option(self, choice):
          match choice:
               case 0: print("do option 0")
               case 1: print("do option 1")


class admin(user_class):
     menu = ["admin option", "another"]

     def execute_option(self, choice):
          match choice:
               case 0: print("do option 0")
               case 1: print("do option 1")

