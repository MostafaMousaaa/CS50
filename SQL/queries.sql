-- Basic SELECT queries
-- Get all students
SELECT * FROM students;

-- Get specific columns
SELECT name, house FROM students;

-- Filter with WHERE clause
SELECT name FROM students WHERE house = 'Gryffindor';

-- Order results
SELECT name, year FROM students ORDER BY year DESC, name ASC;

-- Limit results
SELECT name FROM students LIMIT 3;

-- Advanced filtering
SELECT name FROM students WHERE year >= 3 AND house IN ('Gryffindor', 'Ravenclaw');

-- Pattern matching with LIKE
SELECT title FROM shows WHERE title LIKE '%The%';

-- Count records
SELECT COUNT(*) FROM students;
SELECT COUNT(*) as gryffindor_count FROM students WHERE house = 'Gryffindor';

-- Group by and aggregate functions
SELECT house, COUNT(*) as student_count 
FROM students 
GROUP BY house 
ORDER BY student_count DESC;

-- Average, min, max
SELECT 
    AVG(rating) as avg_rating,
    MIN(rating) as min_rating,
    MAX(rating) as max_rating
FROM ratings;

-- Having clause (filter groups)
SELECT house, COUNT(*) as count
FROM students 
GROUP BY house 
HAVING count >= 2;

-- JOIN operations
-- Inner join - students with their enrollments and course info
SELECT s.name, c.title, e.grade
FROM students s
INNER JOIN enrollments e ON s.id = e.student_id
INNER JOIN courses c ON e.course_id = c.id;

-- Left join - all students, whether enrolled or not
SELECT s.name, c.title
FROM students s
LEFT JOIN enrollments e ON s.id = e.student_id
LEFT JOIN courses c ON e.course_id = c.id;

-- Multiple joins - shows with genres and ratings
SELECT s.title, g.name as genre, r.rating
FROM shows s
JOIN show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
JOIN ratings r ON s.id = r.show_id
ORDER BY r.rating DESC;

-- Subqueries
-- Students in the same house as Harry Potter
SELECT name FROM students 
WHERE house = (
    SELECT house FROM students WHERE name = 'Harry Potter'
);

-- Shows with above average ratings
SELECT title, year FROM shows
WHERE id IN (
    SELECT show_id FROM ratings 
    WHERE rating > (SELECT AVG(rating) FROM ratings)
);

-- Complex query - Student GPA calculation
SELECT 
    s.name,
    AVG(
        CASE e.grade
            WHEN 'A' THEN 4.0
            WHEN 'B' THEN 3.0
            WHEN 'C' THEN 2.0
            WHEN 'D' THEN 1.0
            WHEN 'F' THEN 0.0
        END
    ) as gpa
FROM students s
JOIN enrollments e ON s.id = e.student_id
GROUP BY s.id, s.name
ORDER BY gpa DESC;

-- Window functions (if supported)
SELECT 
    name, 
    house, 
    year,
    RANK() OVER (PARTITION BY house ORDER BY year DESC) as house_rank
FROM students;

-- UPDATE operations
UPDATE students SET year = year + 1 WHERE year < 4;

UPDATE ratings SET votes = votes + 1 WHERE show_id = 1;

-- DELETE operations
DELETE FROM enrollments WHERE grade = 'F';

-- Complex delete with subquery
DELETE FROM students 
WHERE id NOT IN (
    SELECT DISTINCT student_id FROM enrollments
);

-- INSERT operations
INSERT INTO students (name, house, year) 
VALUES ('Neville Longbottom', 'Gryffindor', 3);

-- Insert from select
INSERT INTO courses (title, department)
SELECT DISTINCT 'Advanced ' || title, department
FROM courses
WHERE credits = 4;

-- Analytical queries
-- Top rated shows by genre
SELECT 
    g.name as genre,
    s.title,
    r.rating,
    RANK() OVER (PARTITION BY g.name ORDER BY r.rating DESC) as genre_rank
FROM shows s
JOIN show_genres sg ON s.id = sg.show_id
JOIN genres g ON sg.genre_id = g.id
JOIN ratings r ON s.id = r.show_id
ORDER BY g.name, genre_rank;

-- Course enrollment statistics
SELECT 
    c.title,
    c.department,
    COUNT(e.student_id) as enrolled_students,
    AVG(
        CASE e.grade
            WHEN 'A' THEN 4.0
            WHEN 'B' THEN 3.0
            WHEN 'C' THEN 2.0
            WHEN 'D' THEN 1.0
            WHEN 'F' THEN 0.0
        END
    ) as avg_grade
FROM courses c
LEFT JOIN enrollments e ON c.id = e.course_id
GROUP BY c.id, c.title, c.department
ORDER BY enrolled_students DESC;
