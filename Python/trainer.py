from input_helper import *
from sql_helper import *
def view_unavailibility(id):
    print("Here is your unavailibility: ")
    get_unavailibility(id)



def search_member(id):
    while True:
        fname = get_text_input("What is their first name?")
        lname = get_text_input("What is their last name?")
        member_id = get_id_from_name(fname, lname, "Member")
        if member_id == 0: print("No user of that name, try again:")
        else: break
    print_member_info(member_id)
    print_fitness_goals(member_id)
    print_exercise(member_id)
    return
    


def edit_unavailibility(id):
    choice = get_menu_input("What would you like to do?", ["Add Unavailability", "Remove Unavailability"])

    match choice:
        case 0: 
            time = get_time_input("What time would you like to add? ", False)
            date = get_number_input("What day of the week? (1-7, starting on Monday)", 1, 7)
            time_id = get_timeslot(time, date)
            if time_id == 0:
                time_id = create_timeslot(time, date)
            
            add_unavailibility(id, time_id)
        case 1:
            time = get_time_input("What time would you like to remove? ", False)
            date = get_number_input("What day of the week? (1-7, starting on Monday)", 1, 7)
            time_id = get_timeslot(time, date)
            if time_id == 0: return
            remove_unavailibility(id, time_id)


