CREATE TABLE users (
	id SERIAL NOT NULL,
	username VARCHAR(32) NOT NULL,
	email VARCHAR,
	PRIMARY KEY (id),
	UNIQUE (username),
	UNIQUE (email)
);

INSERT INTO users (username, email)
VALUES ('John'::VARCHAR, 'john@example.com'::VARCHAR)
RETURNING users.id;

SELECT users.id AS users_id,
       users.username AS users_username,
       users.email AS users_email
FROM users
-- WHERE users.id = %(pk_1)s::INTEGER
WHERE users.id = 1::INTEGER;
-- {'pk_1': 1}
-- User(id=1, username='John', email='john@example.com'))
