CREATE TABLE continents (
    id SERIAL PRIMARY KEY,
    name TEXT
);

CREATE TABLE countries (
    id SERIAL PRIMARY KEY,
    name TEXT,
    continent_id INTEGER REFERENCES continents
);

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    admin INTEGER,
    country_id INTEGER REFERENCES countries
);

CREATE TABLE directors (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    description TEXT,
    country_id INTEGER REFERENCES countries
);

CREATE TABLE screenwriters (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE,
    description TEXT,
    country_id INTEGER REFERENCES countries
);

CREATE TABLE languages (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE genres (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE
);

CREATE TABLE films (
    id SERIAL PRIMARY KEY,
    visible INTEGER,
    name TEXT UNIQUE,
    description TEXT,
    year INTEGER,
    country_id INTEGER REFERENCES countries,
    language_id INTEGER REFERENCES languages,
    genre_id INTEGER REFERENCES genres,
    director_id INTEGER REFERENCES directors,
    screenwriter_id INTEGER REFERENCES screenwriters
);

CREATE TABLE reviews (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users,
    film_id INTEGER REFERENCES films,
    content TEXT,
    grade INTEGER,
    submitted TIMESTAMP
);