from input_helper import *
from format_helper import *

def dashboard():
     display_excercises()
     current_bests()
     health_stats()

def display_excercises():
     ex = get_excercises()
     for i in ex:
          print(i)

def display_current_bests():

def display_health_stats():
     avgs = get_averages()
     print("Your average blood pressure is", avgs[0])
     print("Your average heart rate is", avgs[1])
     draw_graph(get_weights()[10:], 10)

#################
###sql helpers###
#################

def get_averages():
     #SELECT AVG(blood_pressure)FROM Exercise WHERE member_id = id;
     #SELECT AVG(heartrate_avg)FROM Exercise WHERE member_id = id;
     return (avg_bp, avg_hr)

def get_weights():
     #SELECT weight FROM Exercise WHERE member_id = id ORDER BY date;
     return weights

def get_excercises():
     pass #get all excercises from database

def get_goals():
     pass #get all goals from database


###################
###other helpers###
###################

def average_index(items, index):
     total = 0
     for i in items:
          total += i[index]
     return total/len(items)
          
