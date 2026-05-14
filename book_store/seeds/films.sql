DROP TABLE IF EXISTS films;
DROP SEQUENCE IF EXISTS films_id_seq;

CREATE SEQUENCE IF NOT EXISTS films_id_seq;
CREATE TABLE films(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    director VARCHAR(255)
);

TRUNCATE table films;

INSERT INTO films(title, director) VALUES ('The Hunger Games', 'Gary Ross');
INSERT INTO films(title, director) VALUES ('Tenet', 'Christopher Nolan');
INSERT INTO films(title, director) VALUES ('Project Hail Mary', 'Phil Lord');
INSERT INTO films(title, director) VALUES ('Dune', 'Denis Villeneuve');