1. Managing a Fitness Center Database
Objective: This assignment is centered around Data Manipulation Language (DML) operations in a fitness center database. You will be working on inserting, updating, and deleting data related to gym members, and workout sessions, emphasizing the practical application of SQL DML commands in a real-world scenario.

Members Table Structure:

CREATE TABLE Members (
    id INT PRIMARY KEY,
    name VARCHAR(255) NOT NULL,
    age INT,
);
WorkoutSessions Table Structure:

CREATE TABLE WorkoutSessions (
    session_id INT PRIMARY KEY,
    member_id INT,
    session_date DATE,
    session_time VARCHAR(50),
    activity VARCHAR(255),
    FOREIGN KEY (member_id) REFERENCES Members(id)
);
Task 1: SQL Data Insertion

Problem Statement: Your task is to populate the Members and WorkoutSessions tables with relevant data. This will involve inserting records into both tables while ensuring data integrity and consistency.
Expected Outcome: New member records are successfully added to the Members table with their respective details.
Task 2: SQL Data Update

Problem Statement: Update the workout session time for a specific member. Assume member 'Jane Doe' has changed her workout session from morning to evening.
Expected Outcome: The WorkoutSessions table is successfully updated to reflect the new session time for Jane Doe.
Task 3: SQL Data Deletion

Problem Statement: Remove data of a member who has canceled their gym membership. Assume member 'John Smith' has canceled his membership.
Expected Outcome: John Smith's record is successfully removed from the Members table, reflecting his cancellation of the gym membership.
