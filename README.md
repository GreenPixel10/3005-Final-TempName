# 3005-Final-TempName


To run:
install python 3.12.2 or python 3.10.7 (other versions are untested)
create a data base called GymClubData in pgAdmin 4
run the ddl.sql file in the query part of the database
then run the dml.sql file in the query part of the database
in sql_helper.py, change the 
    DB_NAME = "GymClubData"
    DB_USER = "projuser"
    DB_PASS = "projuser"
    DB_HOST = "localhost"
    DB_PORT = "5432"
to your correct values
open a command prompt in the folder named Python
enter the command:
    python .\main.py



sample login for each type of user:
Member email: john.doe@example.com
Member Password: johnGotThatDoe27

Trainer email: mathew.stove@example.com
Trainer Password: grapeSodiesRule11

Admin Email: walter.white@example.com
Admin Password: jesseFan37


list of rooms (for creating sessions as admin)
weight
treadmill
pool
class
spin

list of trainers to book (when creating sessions as admin)
Mathew Stove
Randy Lahey

Python Version:
Python 3.12.2
or
Python 3.10.7
Operating system:
Windows 11

Demonstration Video Link:
