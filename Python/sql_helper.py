import psycopg2
from input_helper import int_to_day
from datetime import date

#replace with your db information
DB_NAME = "GymClubData2"
DB_USER = "projuser"
DB_PASS = "projuser"
DB_HOST = "localhost"
DB_PORT = "5432"



def insert_member(first_name, last_name, email, join_date, age, mem_password):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO Member (first_name, last_name, email, join_date, password, age) VALUES ('{}', '{}', '{}', '{}','{}','{}')".format(first_name, last_name, email, join_date, mem_password, age))


    conn.commit()
    cur.close()
    conn.close()

def get_id_from_name(fname,lname,table):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    if(table == "Member"): id = "member_id"
    elif(table == "Trainer"): id = "trainer_id"
    elif(table == "Admin"): id = "admin_id"
    else:
        print("Error get_id_from_name")
        exit()
    cur.execute("SELECT {} FROM {} WHERE first_name = '{}' AND last_name = '{}'".format(id, table, fname, lname))
    ret_id = cur.fetchone()
    ret_id = ret_id[0]
    cur.close()
    conn.close()
    return ret_id

def check_creds(email,password,table):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    if(table == "Member"): id = "member_id"
    elif(table == "Trainer"): id = "trainer_id"
    elif(table == "Admin"): id = "admin_id"
    else:
        print("Error check_creds")
        exit()
    cur.execute("SELECT {} FROM {} WHERE email = '{}' AND password = '{}'".format(id,table,email, password))
    user_id = cur.fetchone()
    cur.close()
    conn.close()
    if user_id:
        return user_id[0]
    return 0


def get_unavailibility(trainer_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT timeslot_id FROM Unavailability WHERE trainer_id = '{}'".format(trainer_id))
    rows = cur.fetchall()
    for timeslot_id in rows:
        timeslot_id = timeslot_id[0]
        cur.execute("SELECT day_of_the_week, time FROM Timeslot WHERE timeslot_id = '{}'".format(timeslot_id))
        timeslot_info = cur.fetchone()
        print(int_to_day(timeslot_info[0]) + " at "+ str(timeslot_info[1]))
    cur.close()
    conn.close()


def print_member_info(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT first_name, last_name, email, age, join_date FROM Member WHERE member_id = '{}'".format(id))
    returns = cur.fetchone()
    print("Name: " + returns[0] + " " + returns[1])
    print("Email: " + returns[2])
    print("Age: " + str(returns[3]))
    print("Join Date: " + str(returns[4]))


    cur.close()
    conn.close()

def print_fitness_goals(member_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT current_best, goal_value, type_of_goal FROM FitnessGoal WHERE member_id = '{}'".format(member_id))
    returns = cur.fetchall()
    for info in returns:
        pr, goal_value, type_of_goal = info
        print("Goal Name: " + type_of_goal + " | Goal Value: " + str(goal_value) + " | Current Best: " + str(pr))

    cur.close()
    conn.close()

def print_exercise(member_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT description, date, time, blood_pressure, heartrate_avg, weight FROM Exercise WHERE member_id ='{}'".format(member_id))
    returns = cur.fetchall()

    for info in returns:
        description, date, time, blood_pressure, heartrate_avg, weight = info
        print("Description: " + description + " | Date: " + str(date) + " | Time: " + str(time) + " | Blood Pressure: "+ str(blood_pressure) +" | Average Heart Rate: " + str(heartrate_avg) + " | Weight: " + str(weight))

    cur.close()
    conn.close()


def get_timeslot(time, day):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT timeslot_id FROM Timeslot WHERE time = '{}' AND day_of_the_week = '{}'".format(time, day))
    timeslot_id = cur.fetchone()

    cur.close()
    conn.close()
    if timeslot_id:
        return timeslot_id[0]
    return 0

def get_timeslot_from_id(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT time, day_of_the_week FROM Timeslot WHERE timeslot_id = '{}'".format(id))
    returns = cur.fetchone()
    return returns

def create_timeslot(time, date):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO Timeslot (time, day_of_the_week) VALUES ('{}', '{}') RETURNING timeslot_id".format(time, date))
    id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return id


def add_unavailibility(trainer_id, time_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("INSERT INTO Unavailability (trainer_id, timeslot_id) VALUES ('{}','{}')".format(trainer_id, time_id))

    conn.commit()
    cur.close()
    conn.close()

def remove_unavailibility(trainer_id, time_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM unavailability WHERE trainer_id = '{}' AND timeslot_id = '{}'".format(trainer_id, time_id))

    conn.commit()
    cur.close()
    conn.close()

def print_sessions():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM Session")
    rows = cur.fetchall()
    for info in rows:
        #session_id, trainer_id, room_id, time_id, group, price = info
        #time, day = get_timeslot_from_id(time_id)
        display_session(info, True)
        #print("Session Id: " + str(session_id) + " | Trainer Id: " + str(trainer_id) + " | Room_Id: "+ str(room_id) + " | Date: " + int_to_day(day) + " | Time: " + str(time) + " | Group: " + str(group) + " | Price: " + str(price))
    cur.close()
    conn.close()
    return len(info)

def get_room_id_from_name(name):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT room_id FROM Room WHERE name = '{}'".format(name))
    ret_id = cur.fetchone()
    ret_id = ret_id[0]
    cur.close()
    conn.close()
    return ret_id

def get_room_name_from_id(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT name FROM Room WHERE room_id = '{}'".format(id))
    ret_name = cur.fetchone()
    ret_name = ret_name[0]
    cur.close()
    conn.close()
    return ret_name

def get_trainer_from_id(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT first_name, last_name FROM Trainer WHERE trainer_id = '{}'".format(id))
    t = cur.fetchone()
    cur.close()
    conn.close()
    return t


def create_session(trainer_id,room_id,timeslot_id,group,price):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("INSERT INTO Session (trainer_id, room_id, timeslot_id, group_session, price) VALUES ('{}', '{}','{}','{}','{}')".format(trainer_id,room_id,timeslot_id,group,price))

    conn.commit()
    cur.close()
    conn.close()


def session_update(session_id,newVal,updateMe):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("UPDATE Session SET {} = '{}' WHERE session_id = {}".format(updateMe, newVal, session_id))

    conn.commit()
    cur.close()
    conn.close()


def remove_session(session_id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("DELETE FROM session WHERE session_id = '{}'".format(session_id))

    conn.commit()
    cur.close()
    conn.close()

def print_equipment():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT * FROM equipment")
    returns = cur.fetchall()

    for info in returns:
        serial, type, room_id, last_main = info
        print("Serial: " + str(serial) + " | Type: " + type + " | Room Id: " + str(room_id) + " | Last Maintained: "+ str(last_main))

    cur.close()
    conn.close()

def maintain_eq(serial):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    day = date.today()
    cur.execute("UPDATE equipment SET date_of_last_maintenance = '{}' WHERE equipment_serial = {}".format(day,serial))

    conn.commit()
    cur.close()
    conn.close()



def print_signed_up_for():
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()

    cur.execute("SELECT * FROM signed_up_for")
    returns = cur.fetchall()

    for info in returns:
        mem_id, session_id, date = info
        print("Member Id: " + str(mem_id) + " | Session id: " + str(session_id) + " | Date of transaction: " + str(date))

    cur.close()
    conn.close()



    #########



def update_userinfo_field(id, field, value):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("UPDATE Member SET {} = '{}' WHERE member_id = {}".format(field, value, id))

    conn.commit()
    cur.close()
    conn.close()


def get_averages(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT AVG(blood_pressure)FROM Exercise WHERE member_id = {}".format(id))
    avg_bp = cur.fetchall()
    cur.execute("SELECT AVG(heartrate_avg)FROM Exercise WHERE member_id = {}".format(id))
    avg_hr = cur.fetchall()
    cur.close()
    conn.close()


    return avg_bp, avg_hr

def get_weights(id):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT weight FROM Exercise WHERE member_id = {} ORDER BY date".format(id))
    wights = cur.fetchall()
    cur.close()
    conn.close()
    return weights

def get_excercises():
    pass #get all excercises from database

def get_goals(id, uncompleted = True):
    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    cur.execute("SELECT * FROM FitnessGoal WHERE member_id = {} AND current_best {} goal_value".format(id, "<" if uncompleted else ">="))
    goals = cur.fetchall()
    cur.close()
    conn.close()
    return goals


def add_goal_sql(id, type, val):

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    query = "INSERT INTO FitnessGoal (member_id, current_best, goal_value, type_of_goal) VALUES ({}, 0, {}, '{}')".format(id, val, type)
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()


def get_sessions(id):

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    query = "SELECT session_id, trainer_id, room_id, timeslot_id, group_session, price FROM (signed_up_for NATURAL JOIN session) WHERE member_id = {}".format(id)
    cur.execute(query)
    sessions = cur.fetchall()
    cur.close()
    conn.close()
    return sessions

def display_session(s, show_ID = False): #session_id, trainer_id, room_id, timeslot_id, group_session, price
    ts = get_timeslot_from_id(s[3])
    t = get_trainer_from_id(s[1])
    if show_ID: print(str(s[0]) + ": ", end = " ")
    print("Group session" if s[4] else "Solo session", end = " ")
    print("every {} at {}".format(int_to_day(ts[1]), ts[0]), end = " ")
    print("in the", get_room_name_from_id(s[2]), "room,", end = " ")
    print("with trainer", t[0], t[1], "(${})".format(s[5]))


def buy_session(id, session_id):

    conn = psycopg2.connect(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)
    cur = conn.cursor()
    query = "INSERT INTO Signed_up_for (member_id, session_id, date) VALUES ({}, {}, '{}')".format(id, session_id, date.today())
    cur.execute(query)
    conn.commit()
    cur.close()
    conn.close()
