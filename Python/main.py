from input_helper import *


menu = ["World peace",
        "Hamburger",
        "Launch warheads"]


print(get_text_input("Enter your name", 4))
print()

print(get_number_input("Enter your age", 25, 36))
print()

print(get_menu_input("What would you like to do?", menu))
print()
