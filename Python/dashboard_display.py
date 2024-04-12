from input_helper import *
from format_helper import *
from sql_helper import *

def dashboard(id):
     display_excercises(id)
     display_current_bests(id)
     display_health_stats(id)

     input("Press enter to return to the main menu")

def display_excercises(id):
    print("\nHere is your exercise log:")
    print_exercise(id)

def display_current_bests(id):
    print("\nHere are some of your completed goals!")
    goals = get_goals(id, False)
    display_goals(goals)

def display_health_stats(id):
    bp, hr = get_averages(id)
    #print(type(bp[0][0]))
    print()
    print("Your average blood pressure is", int(bp[0][0]))
    print("Your average heart rate is", int(hr[0][0]))
    w = get_weights(id)
    print("\nHere is your weight over your recent exercises:")
    draw_graph(w, 10)

#################
###sql helpers###
#################
