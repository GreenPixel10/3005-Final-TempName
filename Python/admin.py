from input_helper import *
def manage_rooms():
    choice = get_menu_input("What would you like to do?",["List Sessions","Create Session","Update Session","Remove Session"])
    match choice:
        case 0:
            print("Here are all the sessions:")
            #pull all the sessions, display with id
        case 1:
            ftrainer = get_text_input("What is the first name of the trainer to will host it?")
            ltrainer = get_text_input("What is their last name")
            #get trainer_id from searching name
            room = get_text_input("Which room do you want it to take place in?")
            #get room_id from search room
            time = get_time_input("What time do you want it to take place at?")
            date = get_number_input("What date do you want it to take place on? (1-7 starting on monday)")
            #see if this timeslot exists
            #if it doesnt, create one
            group = get_bool_input("Will this be a group session?")
            price = get_number_input("How much does it cost?")
            #create the actual session
        case 2:
            session_id = get_text_input("What is the id of the session you would like to update?")
            #display the whole session
            choice2 = get_menu_input("What part would you like to update:",["Trainer","Room","Timeslot","Group Session","Price"])
            match choice2:
                case 0: 
                    fname = get_text_input("Enter new first name:")
                    lname = get_text_input("Enter new last name:")
                    #get trainer id from name
                    newVal = ""
                    updateMe = "trainer_id"
                case 1: 
                    roomName = get_text_input("Enter new room name:")
                    #get room id from name
                    newVal = ""
                    updateMe = "room_id"
                case 2: 
                    time = get_time_input("Enter new time:")
                    date = get_number_input("Enter new date: (1-7 starting on monday)")
                    #check if that timeslot exist
                    #if not create one
                    #get the id for it
                    newVal = ""
                    updateMe = "timeslot_id"
                case 3: 
                    newVal = get_bool_input("Change it to:")
                    updateMe = "group_session"
                case 4: 
                    newVal = get_number_input("Change the price to:")
                    updateMe = "price"
            #sql update based on newVal and updateme
        case 3:
            session_id = get_number_input("What is the id of the session you want to remove?")
            #remove the session from id


def monitor_equipment():
    choice = get_menu_input("What would you like to do",["View Equipment","Maintain Equipment"])
    match choice:
        case 0: 
            print("Here is all the equipment:")
            #get all the equipment and display
        case 1:
            equipment_id = get_number_input("What is the id of the equipment that got maintained?")
            #update the last maintained date to today





def view_billing():
    #print all the payments
    return

