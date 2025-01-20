CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER
);

INSERT INTO users (name, age) VALUES ('Alice', 30);

UPDATE users SET age = 35 WHERE name = 'Alice';

DELETE FROM users WHERE name = 'Bob';

SELECT * FROM users;
