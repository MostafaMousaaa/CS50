-- Create Students Database
CREATE DATABASE IF NOT EXISTS students;
USE students;

-- Students table
CREATE TABLE students (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    house TEXT NOT NULL,
    year INTEGER NOT NULL CHECK (year >= 1 AND year <= 4)
);

-- Courses table
CREATE TABLE courses (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL UNIQUE,
    credits INTEGER NOT NULL DEFAULT 3,
    department TEXT NOT NULL
);

-- Enrollments table (many-to-many relationship)
CREATE TABLE enrollments (
    student_id INTEGER,
    course_id INTEGER,
    grade TEXT CHECK (grade IN ('A', 'B', 'C', 'D', 'F')),
    semester TEXT NOT NULL,
    PRIMARY KEY (student_id, course_id, semester),
    FOREIGN KEY (student_id) REFERENCES students(id),
    FOREIGN KEY (course_id) REFERENCES courses(id)
);

-- Insert sample students
INSERT INTO students (name, house, year) VALUES
    ('Harry Potter', 'Gryffindor', 3),
    ('Hermione Granger', 'Gryffindor', 3),
    ('Ron Weasley', 'Gryffindor', 3),
    ('Draco Malfoy', 'Slytherin', 3),
    ('Luna Lovegood', 'Ravenclaw', 2),
    ('Cedric Diggory', 'Hufflepuff', 4);

-- Insert sample courses
INSERT INTO courses (title, credits, department) VALUES
    ('Computer Science 50', 4, 'Computer Science'),
    ('Introduction to Psychology', 3, 'Psychology'),
    ('Calculus I', 4, 'Mathematics'),
    ('English Literature', 3, 'English'),
    ('Physics I', 4, 'Physics');

-- Insert sample enrollments
INSERT INTO enrollments (student_id, course_id, grade, semester) VALUES
    (1, 1, 'A', 'Fall 2023'),
    (1, 3, 'B', 'Fall 2023'),
    (2, 1, 'A', 'Fall 2023'),
    (2, 2, 'A', 'Fall 2023'),
    (2, 3, 'A', 'Fall 2023'),
    (3, 1, 'B', 'Fall 2023'),
    (3, 4, 'C', 'Fall 2023'),
    (4, 2, 'B', 'Fall 2023'),
    (5, 1, 'A', 'Fall 2023'),
    (6, 1, 'A', 'Fall 2023');

-- Create Shows Database
CREATE DATABASE IF NOT EXISTS shows;
USE shows;

-- Shows table
CREATE TABLE shows (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    year INTEGER,
    episodes INTEGER
);

-- Genres table
CREATE TABLE genres (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL UNIQUE
);

-- Show_Genres junction table
CREATE TABLE show_genres (
    show_id INTEGER,
    genre_id INTEGER,
    PRIMARY KEY (show_id, genre_id),
    FOREIGN KEY (show_id) REFERENCES shows(id),
    FOREIGN KEY (genre_id) REFERENCES genres(id)
);

-- Ratings table
CREATE TABLE ratings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    show_id INTEGER,
    rating REAL CHECK (rating >= 0.0 AND rating <= 10.0),
    votes INTEGER DEFAULT 0,
    FOREIGN KEY (show_id) REFERENCES shows(id)
);

-- Insert sample data
INSERT INTO shows (title, year, episodes) VALUES
    ('The Office', 2005, 201),
    ('Breaking Bad', 2008, 62),
    ('Friends', 1994, 236),
    ('Game of Thrones', 2011, 73),
    ('Stranger Things', 2016, 42);

INSERT INTO genres (name) VALUES
    ('Comedy'),
    ('Drama'),
    ('Crime'),
    ('Fantasy'),
    ('Science Fiction'),
    ('Horror');

INSERT INTO show_genres (show_id, genre_id) VALUES
    (1, 1), -- The Office - Comedy
    (2, 2), (2, 3), -- Breaking Bad - Drama, Crime
    (3, 1), -- Friends - Comedy
    (4, 2), (4, 4), -- Game of Thrones - Drama, Fantasy
    (5, 2), (5, 5), (5, 6); -- Stranger Things - Drama, Sci-Fi, Horror

INSERT INTO ratings (show_id, rating, votes) VALUES
    (1, 8.7, 550000),
    (2, 9.4, 1600000),
    (3, 8.9, 890000),
    (4, 9.2, 1900000),
    (5, 8.8, 750000);

-- Create indexes for better performance
CREATE INDEX idx_students_house ON students(house);
CREATE INDEX idx_students_year ON students(year);
CREATE INDEX idx_shows_year ON shows(year);
CREATE INDEX idx_ratings_rating ON ratings(rating);
