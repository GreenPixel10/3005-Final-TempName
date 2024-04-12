from input_helper import *
from sql_helper import *
def manage_rooms():
    while True:
        choice = get_menu_input("What would you like to do?",["List Sessions","Create Session","Update Session","Remove Session","Go Back"])
        match choice:
            case 0:
                print("Here are all the sessions:")
                print_sessions()
            case 1:
                while True:
                    ftrainer = get_text_input("What is the first name of the trainer to will host it?")
                    ltrainer = get_text_input("What is their last name")
                    trainer_id = get_id_from_name(ftrainer,ltrainer, "Trainer")
                    if trainer_id == 0: 
                        print("That trainer does not exist, try again:")
                    else: break
                while True:
                    room = get_text_input("Which room do you want it to take place in?")
                    room_id = get_room_id_from_name(room)
                    if room_id == 0: 
                        print("That room does not exist, try again:")
                    else: break
                time = get_time_input("What time do you want it to take place at?")
                date = get_number_input("What date do you want it to take place on? (1-7 starting on monday)",1 , 7)

                #see if this timeslot exists
                #if it doesnt, create one
                time_id = get_timeslot(time, date)
                if time_id == 0:
                    time_id = create_timeslot(time, date)

                group = get_bool_input("Will this be a group session?")
                price = get_number_input("How much does it cost?")

                #create the actual session
                create_session(trainer_id,room_id,time_id,group,price) 

            case 2:
                print_sessions()
                session_id = get_text_input("What is the id of the session you would like to update?")

                choice2 = get_menu_input("What part would you like to update:",["Trainer","Room","Timeslot","Group Session","Price"])
                match choice2:
                    case 0: 
                        while True:
                            fname = get_text_input("Enter new first name:")
                            lname = get_text_input("Enter new last name:")
                            newVal = get_id_from_name(fname,lname, "Trainer")
                            updateMe = "trainer_id"
                            if newVal == 0: 
                                print("That trainer does not exist, try again:")
                            else: break
                    case 1:
                        while True:
                            roomName = get_text_input("Enter new room name:")
                            newVal = get_room_id_from_name(roomName)
                            updateMe = "room_id"
                            if newVal == 0:
                                print("That room does not exist, try again:")
                            else: break
                    case 2: 
                        time = get_time_input("Enter new time:")
                        date = get_number_input("Enter new date: (1-7 starting on monday)", 1, 7)
                        time_id = get_timeslot(time, date)
                        if time_id == 0:
                            time_id = create_timeslot(time, date)
                        newVal = time_id
                        updateMe = "timeslot_id"
                    case 3: 
                        newVal = get_bool_input("Change it to:")
                        updateMe = "group_session"
                    case 4: 
                        newVal = get_number_input("Change the price to:")
                        updateMe = "price"
                #sql update based on newVal and updateme
                session_update(session_id,newVal,updateMe)
            case 3:
                session_id = get_number_input("What is the id of the session you want to remove?")
                #remove the session from id
                remove_session(session_id)
            case 4: break


def monitor_equipment():
    while True:
        choice = get_menu_input("What would you like to do",["View Equipment","Maintain Equipment", "Go Back"])
        match choice:
            case 0: 
                print("Here is all the equipment:")
                print_equipment()
            case 1:
                serial = get_number_input("What is the serial number of the equipment that got maintained?")
                maintain_eq(serial)
            case 2: break





def view_billing():
    print_signed_up_for()
    return

