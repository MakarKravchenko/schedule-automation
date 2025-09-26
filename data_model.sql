-- Data model for schedule automation system
CREATE TABLE Teachers (
    id INTEGER PRIMARY KEY,
    name TEXT,
    subject TEXT
);

CREATE TABLE Groups (
    id INTEGER PRIMARY KEY,
    name TEXT,
    students_count INTEGER
);

CREATE TABLE Rooms (
    id INTEGER PRIMARY KEY,
    room_number TEXT,
    capacity INTEGER
);
