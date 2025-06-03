CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    abbreviation CHAR(2) UNIQUE NOT NULL
);

CREATE TABLE classifications (
    id SERIAL PRIMARY KEY,
    label TEXT UNIQUE NOT NULL,
    max_jail_months INTEGER,
    max_fine_usd INTEGER,
    probation_length_months INTEGER
);

CREATE TABLE statutes (
    id SERIAL PRIMARY KEY,
    state_id INTEGER REFERENCES states(id),
    category_id INT REFERENCES categories(id),
    title TEXT NOT NULL,
    description TEXT,
    citation TEXT
);

CREATE TABLE punishments (
    id SERIAL PRIMARY KEY,
    statute_id INTEGER REFERENCES statutes(id),
    classification_id INTEGER REFERENCES classifications(id),
    notes TEXT
);

CREATE TABLE categories (
    id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);