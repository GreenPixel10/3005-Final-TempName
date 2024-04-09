from input_helper import *
def view_unavailibility(id):
    #use id to pull up the trainers unavailibility from id
    print("Here is your unavailibility: ")
    #splice the data, and output:
    #for blah blah blah
        #print(i)


def search_member(fname, lname):
    #search member by names
    #print all the info about that member (maybe actually run their like check stats and stuff)
    return
    


def edit_unavailibility(id):
    choice = get_menu_input("What would you like to do?", ["Add Unavailability", "Remove Unavailability"])

    match choice:
        case 0: 
            time = get_time_input("What time would you like to add? ", False)
            date = get_number_input("What day of the week? (1-7, starting on Monday)")
            #check if that timeslot exists
                #create timeslot var with time and date
            #get timeslot id
            #add timeslot to unavailibility with timeslot id and trainer id
        case 1:
            time = get_time_input("What time would you like to remove? ", False)
            date = get_number_input("What day of the week? (1-7, starting on Monday)")
            #find timeslot id from time and date
            #remove it from the unavailibility table 

