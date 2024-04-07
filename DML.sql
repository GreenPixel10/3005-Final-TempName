INSERT INTO Member (first_name, last_name, email, join_date, password, age) VALUES
('John', 'Doe', 'john.doe@example.com', '2023-09-01', 'johnGotThatDoe27', 79),
('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01', 'ryanGoslingFan42', 23),
('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02', 'beamMachine88', 9);

INSERT INTO Trainer (first_name, last_name, email, password) VALUES
('Randy', 'Lahey', 'randy.lahey@example.com', 'laheySucks37'),
('Mathew', 'Stove', 'mathew.stove@example.com', 'grapeSodiesRule11');

INSERT INTO Admin (first_name, last_name, email, password) VALUES
('Neo', 'FromTheMatix', 'neo.fromthematrix@example.com', 'color 0A'),
('Walter', 'White', 'walter.white@example.com', 'jesseFan37');

INSERT INTO FitnessGoal (member_id, current_best, goal_value, type_of_goal) VALUES
(1, 20, 18, 'Run 5k In (minutes)'),
(2, 23.2, 22, 'Run 5k In (minutes)'),
(3, 18, 17, 'Run 5k In (Minutes)'),
(1, 40, 50, 'Swim Distance (laps)'),
(2, 57, 60, 'Swim Distance (laps)'),
(3, 166, 180, 'Bench Press Weight (lb)'),
(2, 200, 215, 'Bench Press Weight (lb)');

INSERT INTO Exercise (member_id, description, date, time, blood_pressure, heartrate_avg, weight) VALUES
(1, 'Ran 5km', '2024-04-07', '06:27:00', 110, 100, 150),
(1, 'Swam 30 laps', '2024-03-07', '07:30:00', 111, 97, 151),
(1, 'Lifted weighs for 20 minutes', '2024-04-03', '15:59:00', 110, 103, 149),
(1, 'Used the rock wall for 1 hour', '2024-03-17', '12:20:00', 109, 112, 148),
(2, 'Ran 7km', '2024-04-07', '13:27:00', 122, 120, 180),
(2, 'Swam 12 laps', '2024-03-23', '09:30:00', 120, 110, 175),
(2, 'Lifted weighs for 45 minutes', '2024-04-06', '18:00:00', 121, 115, 179),
(2, 'Used the rock wall for 30 minutes', '2024-04-01', '11:23:00', 120, 116, 182),
(3, 'Ran 2km', '2024-03-27', '23:27:00', 137, 124, 167),
(3, 'Swam 28 laps', '2024-03-12', '19:10:00', 135, 132, 170),
(3, 'Lifted weighs for 12 minutes', '2024-03-11', '23:11:00', 135, 123, 169);

INSERT INTO Room (name) VALUES
('weight'),
('treadmill'),
('pool'),
('openRoom1'),
('openRoom2');

INSERT INTO Equipment (equipment_serial, equipment_type, room_id, date_of_last_maintenance) VALUES
(123451, 'Treadmill', 2, '2023-09-12'),
(123452, 'Treadmill', 2, '2023-09-12'),
(123453, 'Treadmill', 2, '2023-09-12'),
(123454, 'Treadmill', 4, '2023-09-12'),
(123455, 'Treadmill', 5, '2023-09-12'),
(124221, 'Bench', 1, '2023-06-23'),
(124222, 'Bench', 1, '2023-06-23'),
(124223, 'Bench', 1, '2023-06-23'),
(124224, 'Bench', 4, '2023-06-23'),
(124225, 'Bench', 4, '2023-06-23');



