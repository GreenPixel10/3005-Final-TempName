from input_helper import *


def dashboard():
     display_excercises()
     current_bests()
     health_stats()

def display_excercises():
     ex = get_excercises()
     for i in ex:
          print(i)

def display_current_bests(ex):
     g = get_goals()
     for i in ex:
          print(i)

def display_health_stats(ex):
     ex = get_excercises()
     for i in ex:
          print(i)

#################
###sql helpers###
#################

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
          
