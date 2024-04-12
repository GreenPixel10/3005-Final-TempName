--CREATE DATABASE GymClubData;
--server name: FinalProj
--username: projuser
--password: projuser
--host: localhost

CREATE TABLE Member (
    member_id SERIAL PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    age INTEGER,
    join_date DATE
);

CREATE TABLE Trainer (
    trainer_id SERIAL PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);

CREATE TABLE Admin (
    admin_id SERIAL PRIMARY KEY,
    email VARCHAR(320) NOT NULL,
    password VARCHAR(50) NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL
);


CREATE TABLE FitnessGoal (
    goal_id SERIAL PRIMARY KEY,
    member_id INTEGER, --FOREIGN KEY
    current_best FLOAT,
    goal_value FLOAT,
    type_of_goal VARCHAR(100),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);


CREATE TABLE Exercise (
    member_id INTEGER, -- FOREIGN KEY
    description VARCHAR(255),
    date DATE,
    time TIME,
    blood_pressure INTEGER,
    heartrate_avg INTEGER,
    weight FLOAT,
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

CREATE TABLE Room (
    room_id SERIAL PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE Timeslot (
    timeslot_id SERIAL PRIMARY KEY,
    time TIME,
    day_of_the_week INTEGER CHECK (day_of_the_week BETWEEN 1 AND 7)
);

CREATE TABLE Session (
    session_id SERIAL PRIMARY KEY,
    trainer_id INTEGER,
    room_id INTEGER,
    timeslot_id INTEGER,
    group_session BOOLEAN,
    price INT,
    FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id),
    FOREIGN KEY (room_id) REFERENCES Room(room_id),
    FOREIGN KEY (timeslot_id) REFERENCES Timeslot(timeslot_id)
);

CREATE TABLE Unavailability (
    trainer_id INTEGER,
    timeslot_id INTEGER,
    FOREIGN KEY (trainer_id) REFERENCES Trainer(trainer_id),
    FOREIGN KEY (timeslot_id) REFERENCES Timeslot(timeslot_id)
);





CREATE TABLE Equipment (
    equipment_serial INTEGER PRIMARY KEY,
    equipment_type VARCHAR(50),
    room_id INTEGER,
    date_of_last_maintenance DATE,
    FOREIGN KEY (room_id) REFERENCES Room(room_id)
);


CREATE TABLE Signed_up_for (
    member_id INTEGER,
    session_id INTEGER,
    date DATE,
    FOREIGN KEY (member_id) REFERENCES Member(member_id),
    FOREIGN KEY (session_id) REFERENCES Session(session_id) ON DELETE CASCADE
);
