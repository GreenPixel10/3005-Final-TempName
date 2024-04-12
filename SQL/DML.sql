INSERT INTO Member (member_id,first_name, last_name, email, join_date, password, age) VALUES
(1,'John', 'Doe', 'john.doe@example.com', '2023-09-01', 'johnGotThatDoe27', 79),
(2,'Jane', 'Smith', 'jane.smith@example.com', '2023-09-01', 'ryanGoslingFan42', 23),
(3,'Jim', 'Beam', 'jim.beam@example.com', '2023-09-02', 'beamMachine88', 9);

INSERT INTO Trainer (trainer_id,first_name, last_name, email, password) VALUES
(1,'Randy', 'Lahey', 'randy.lahey@example.com', 'laheySucks37'),
(2,'Mathew', 'Stove', 'mathew.stove@example.com', 'grapeSodiesRule11');

INSERT INTO Admin (admin_id,first_name, last_name, email, password) VALUES
(1,'Neo', 'FromTheMatix', 'neo.fromthematrix@example.com', 'color 0A'),
(2,'Walter', 'White', 'walter.white@example.com', 'jesseFan37');

INSERT INTO FitnessGoal (goal_id, member_id, current_best, goal_value, type_of_goal) VALUES
(1, 1, 4500, 5000, 'Run Distance in 20 minutes (metres)'),
(2, 2, 3000, 6000, 'Run Distance in 20 minutes (metres)'),
(3, 3, 2850, 3000, 'Run Distance in 20 minutes (metres)'),
(4, 1, 40, 50, 'Swim Distance (laps)'),
(5, 2, 57, 60, 'Swim Distance (laps)'),
(6, 3, 166, 180, 'Bench Press Weight (lb)'),
(7, 2, 200, 215, 'Bench Press Weight (lb)');

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

INSERT INTO Room (room_id,name) VALUES
(1,'weight'),
(2,'treadmill'),
(3,'pool'),
(4,'openRoom1'),
(5,'openRoom2');

INSERT INTO Equipment (equipment_serial, equipment_type, room_id, date_of_last_maintenance) VALUES
(123451, 'Treadmill', 2, '2023-09-12'),
(123452, 'Treadmill', 2, '2023-09-12'),
(123453, 'Treadmill', 2, '2023-09-12'),
(123454, 'Treadmill', 4, '2023-09-12'),
(123455, 'Treadmill', 5, '2023-09-12'),
(124225, 'Reactor Core', 3, '1956-03-22'),
(124221, 'Bench', 1, '2023-06-23'),
(124222, 'Bench', 1, '2023-06-23'),
(124223, 'Bench', 1, '2023-06-23'),
(124224, 'Bench', 4, '2023-06-23'),
(124226, 'Bench', 4, '2023-06-23');


INSERT INTO Timeslot (timeslot_id, time, day_of_the_week) VALUES
(1, '06:00:00', 3), (2, '07:00:00', 3), (3, '08:00:00', 3),
(4, '09:00:00', 3), (5, '10:00:00', 3), (6, '11:00:00', 3),
(7, '13:00:00', 3), (8, '14:00:00', 3), (9, '15:00:00', 3),
(10, '16:00:00', 3), (11, '17:00:00', 3), (12, '18:00:00', 3),
(13, '19:00:00', 3), (14, '20:00:00', 3), (15, '06:00:00', 4),
(16, '07:00:00', 4), (17, '08:00:00', 4), (18, '09:00:00', 4),
(19, '10:00:00', 4), (20, '11:00:00', 4), (21, '13:00:00', 4),
(22, '14:00:00', 4), (23, '15:00:00', 4), (24, '16:00:00', 4),
(25, '17:00:00', 4), (26, '18:00:00', 4), (27, '19:00:00', 4),
(28, '20:00:00', 4), (29, '06:00:00', 5), (30, '07:00:00', 5),
(31, '08:00:00', 5), (32, '09:00:00', 5), (33, '10:00:00', 5),
(34, '11:00:00', 5), (35, '13:00:00', 5), (36, '14:00:00', 5),
(37, '15:00:00', 5), (38, '16:00:00', 5), (39, '17:00:00', 5),
(40, '18:00:00', 5), (41, '19:00:00', 5), (42, '20:00:00', 5),
(43, '06:00:00', 6), (44, '07:00:00', 6), (45, '08:00:00', 6),
(46, '09:00:00', 6), (47, '10:00:00', 6), (48, '11:00:00', 6),
(49, '13:00:00', 6), (50, '14:00:00', 6), (51, '15:00:00', 6),
(52, '16:00:00', 6), (53, '17:00:00', 6), (54, '18:00:00', 6),
(55, '19:00:00', 6), (56, '20:00:00', 6), (57, '06:00:00', 7),
(58, '07:00:00', 7), (59, '08:00:00', 7), (60, '09:00:00', 7),
(61, '10:00:00', 7), (62, '11:00:00', 7), (63, '13:00:00', 7),
(64, '14:00:00', 7), (65, '15:00:00', 7), (66, '16:00:00', 7),
(67, '17:00:00', 7), (68, '18:00:00', 7), (69, '19:00:00', 7),
(70, '20:00:00', 7);



INSERT INTO Session (session_id,trainer_id, room_id, timeslot_id, group_session, price) VALUES
(1, 1, 3, 1, False, 45),
(2, 2, 4, 2, True, 45),
(3, 2, 3, 3, False, 45),
(4, 1, 3, 4, False, 45),
(5, 1, 3, 5, False, 45),
(6, 1, 3, 6, False, 45),
(7, 2, 3, 7, False, 45),
(8, 1, 3, 8, False, 45),
(9, 2, 3, 9, False, 45),
(10, 1, 1, 10, False, 45),
(11, 1, 5, 11, True, 45),
(12, 1, 4, 12, True, 45);

INSERT INTO Signed_up_for (member_id, session_id, date) VALUES
(1, 1, '2023-06-23'),
(1, 2, '2023-04-23'),
(1, 3, '2023-04-23'),
(2, 2, '2023-08-23'),
(2, 7, '2023-08-23'),
(3, 8, '2024-01-23');




INSERT INTO Unavailability (trainer_id, timeslot_id) VALUES
(1, 51),
(1, 52),
(1, 53),
(1, 54),
(1, 55),
(2, 27),
(2, 28),
(2, 29),
(2, 30),
(2, 45),
(2, 56),
(2, 57),
(2, 58);

ALTER SEQUENCE Timeslot_timeslot_id_seq RESTART WITH 71;
ALTER SEQUENCE Session_session_id_seq RESTART WITH 13;
ALTER SEQUENCE Room_room_id_seq RESTART WITH 6;
ALTER SEQUENCE FitnessGoal_goal_id_seq RESTART WITH 20;
ALTER SEQUENCE Member_member_id_seq RESTART WITH 4;
ALTER SEQUENCE Trainer_trainer_id_seq RESTART WITH 3;
ALTER SEQUENCE Admin_admin_id_seq RESTART WITH 3;
