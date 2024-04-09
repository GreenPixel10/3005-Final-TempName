
promptchar = "-> "
days = [31,28,31,30,31,30,31,31,30,31,30,31]
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]



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


def get_email_input(prompt):
     while True:
          email = get_text_input(prompt, 129)
          emailsplit = email.split("@")
          if len(emailsplit) == 2 and emailsplit[0] and emailsplit[1]:
               domain = emailsplit[1]
               domainsplit = domain.split(".")
               #if there's at least 1 dot AND every split section has something in it
               if len(domainsplit) >= 2 and sum(bool(i) for i in domainsplit) == len(domainsplit):
                    return email

          print("Invalid email format")



def get_password_input(prompt):
    print(prompt)
    print("Password must be at least 7 characters and contain a capital, number, and special character.")
    while True:
            has_cap = False
            has_number = False
            has_special = False
            long = False
            valid_chars = True

            password = get_text_input("")
            if len(password) >= 7: long = True

            for i in password:
                char = ord(i)
                if char >= 65 and char <= 90: has_cap = True
                elif char >= 48 and char <= 57: has_number = True
                elif (char >= 97 and char <= 122) or char == 32: pass
                elif char >= 33 and char <= 126:  has_special = True
                else: valid_chars = False

            if not has_cap: print("-Password must have a capital letter")
            if not has_number: print("-Password must have a number")
            if not has_special: print("-Password must have a special character")
            if not long: print("-Password not long enough")
            if not valid_chars: print("-Invalid character(s)")

            if(has_cap and has_number and has_special and long and valid_chars): return password
            else: print("Please try again.")


def get_new_password(prompt):
    while True:
        password = get_password_input(prompt)
        password2 = get_text_input("\nRe-enter your password")
        if password == password2: return password
        else: print("Passwords don't match! Try again\n")




def get_date_input(prompt):
     print(prompt)
     year = get_number_input("Enter a year", 1, 9999)
     month = get_number_input("Enter a month", 1, 12)
     leap = int(month == 2 and ((year % 4 == 0) and ((year % 100 != 0) or (year % 400 == 0)))) #=1 if leap year
     day = get_number_input("Enter a day", 1, days[month-1] + leap)
     return (year, month, day)


def get_time_input(prompt, with_seconds = False):
     print(prompt)
     hours = get_number_input("Enter hour value", 0, 23)
     minutes = get_number_input("Enter minute value", 0, 59)
     seconds = 0
     if with_seconds: seconds = get_number_input("Enter seconds value", 0, 59)
     return (hours, minutes, seconds)


 def get_bool_input(prompt):
      print(prompt)
      choice = get_text_input("Yes or No: ")
      if choice == "yes" or choice == "Yes":
           return True
      else:
           return False
