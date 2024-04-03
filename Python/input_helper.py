
promptchar = "-> "

     
def get_text_input(prompt, charlim = 0):
     while True:
          user_input = input(prompt + promptchar)
          if charlim > 0 and len(user_input) > charlim:
               print("Text must be ", charlim, "characters or less.")
               continue
          
          return user_input



def get_number_input(prompt, min_val = -100000000, max_val = 100000000):
     while True:
          
          user_input = input(prompt + promptchar)

          try:
               user_input_int = int(user_input)
          except ValueError:
               print("Not a valid number")
               continue

          if user_input_int < min_val or user_input_int > max_val:
               print("Number must be between", min_val, "and", max_val)
               continue
          
          return user_input_int



def get_menu_input(prompt, items):
     print(prompt)
     for i in range(len(items)):
          print(str(i)+":", items[i])
     return get_number_input("Enter your choice by number", 0, len(items)-1)
     
