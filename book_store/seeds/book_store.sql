DROP TABLE IF EXISTS books;
DROP SEQUENCE IF EXISTS books_id_seq;

CREATE SEQUENCE IF NOT EXISTS books_id_seq;
CREATE TABLE books(
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    author VARCHAR(255)
);

INSERT INTO books(title, author) VALUES ('The Hungry Caterpiller', 'Eric Carle');
INSERT INTO books(title, author) VALUES ('Amber the Orange Fairy', 'Daisy Meadows');
INSERT INTO books(title, author) VALUES ('The Elephant Vanishes', 'Haruki Murakami');
INSERT INTO books(title, author) VALUES ('Dune', 'Frank Herbert');