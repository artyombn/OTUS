SELECT 1;

SELECT 1 + 2;

SELECT 1 as "one";
SELECT 1 + 2 "one and two";

SELECT 1 "one", 2 "two", 1 + 2 "1+2";

CREATE TABLE autors
(
    id SERIAL PRIMARY KEY,
    username VARCHAR UNIQUE NOT NULL
);

CREATE TABLE posts
(
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    body TEXT NOT NULL DEFAULT '',
    autor_id INTEGER NOT NULL,

    CONSTRAINT fk_author
        FOREIGN KEY (autor_id)
            REFERENCES autors(id)
);

ALTER TABLE autors
ADD COLUMN email VARCHAR UNIQUE;

SELECT id, username
FROM autors;

SELECT *
FROM autors
ORDER BY id DESC;

INSERT INTO autors(username)
VALUES ('cat');

INSERT INTO autors(username)
VALUES ('bob'),
       ('alice');


INSERT INTO autors(username, email)
VALUES ('kyle', 'kyle@example.com'),
('andrew', NULL);

UPDATE autors
SET email = 'admin@example.com'
WHERE username = 'admin';

SELECT *
FROM autors
WHERE email IS NOT NULL;

UPDATE autors
SET email = 'kyle@gmail.com'
WHERE email = 'kyle@example.com';

SELECT id, username, length(username)
FROM autors
ORDER BY length(username), username;

SELECT id, username, concat(username, '@yandex.ru')
FROM autors;

UPDATE autors
SET email = concat(username, '@ya.ru')
WHERE  email IS NULL and length(username) > 4;

UPDATE autors
SET email = concat(username, '@rambler.ru')
WHERE  email IS NULL;

SELECT *
FROM autors
WHERE email ilike '%rambler.%'
ORDER BY id;


--

SELECT *
FROM posts
ORDER BY id;

INSERT INTO posts (title, autor_id)
VALUES ('SQL Lesson', 3),
       ('Postgres Lesson', 5),
       ('DataBase Lesson', 5);

SELECT id, title, autor_id
FROM posts;

SELECT p.id, p.title, a.username, a.email
FROM posts p
JOIN autors a ON a.id = p.autor_id;


SELECT a.id, a.username, count(p.id) "posts-count"
FROM autors a
JOIN posts p ON a.id = p.autor_id
GROUP BY a.id
ORDER BY a.id;

SELECT a.id, a.username, p.id, p.title
FROM autors a
LEFT JOIN posts p ON a.id = p.autor_id
ORDER BY a.id;