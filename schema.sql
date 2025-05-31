CREATE TABLE states (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    abbreviation CHAR(2) UNIQUE NOT NULL
);

CREATE TABLE classifications (
    id SERIAL PRIMARY KEY,
    label TEXT NOT NULL,
    max_jail_months INTEGER,
    max_fine_usd INTEGER,
    probation_length_months INTEGER
);

CREATE TABLE statutes (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT,
    citation TEXT,
    state_id INTEGER REFERENCES states(id),
    category TEXT
);

CREATE TABLE punishments (
    id SERIAL PRIMARY KEY,
    statute_id INTEGER REFERENCES statutes(id),
    classification_id INTEGER REFERENCES classifications(id),
    notes TEXT
);