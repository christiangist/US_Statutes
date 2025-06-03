import psycopg2

conn = psycopg2.connect(
    dbname="us_statutes", 
    user="cgist14",
    host="localhost"
)


cur = conn.cursor()

# 1. Insert state (New York)
cur.execute("""
    INSERT INTO states (name, abbreviation)
    VALUES (%s, %s)
    ON CONFLICT (abbreviation) DO NOTHING
    RETURNING id
""", ("New York", "NY"))
state_id = cur.fetchone()
if state_id is None:
    cur.execute("SELECT id FROM states WHERE abbreviation = 'NY'")
    state_id = cur.fetchone()
state_id = state_id[0]

# 2. Insert category (Theft)
cur.execute("""
    INSERT INTO categories (name)
    VALUES (%s)
    ON CONFLICT (name) DO NOTHING
    RETURNING id
""", ("Theft",))
category_id = cur.fetchone()
if category_id is None:
    cur.execute("SELECT id FROM categories WHERE name = 'Theft'")
    category_id = cur.fetchone()
category_id = category_id[0]

# 3. Insert classification (Class A Misdemeanor)
cur.execute("""
    INSERT INTO classifications (label, max_jail_months, max_fine_usd, probation_length_months)
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (label) DO NOTHING
    RETURNING id
""", ("Class A Misdemeanor", 12, 1000, 36))
classification_id = cur.fetchone()
if classification_id is None:
    cur.execute("SELECT id FROM classifications WHERE label = 'Class A Misdemeanor'")
    classification_id = cur.fetchone()
classification_id = classification_id[0]

# 4. Insert statute (Petit Larceny)
cur.execute("""
    INSERT INTO statutes (state_id, category_id, title, description, citation)
    VALUES (%s, %s, %s, %s, %s)
    RETURNING id
""", (
    state_id,
    category_id,
    "Petit Larceny",
    "A person is guilty of petit larceny when they steal property.",
    "NY Penal Law § 155.25"
))
statute_id = cur.fetchone()[0]

# 5. Insert punishment
cur.execute("""
    INSERT INTO punishments (statute_id, classification_id, notes)
    VALUES (%s, %s, %s)
""", (
    statute_id,
    classification_id,
    "Up to 1 year in jail or 3 years probation, and/or $1000 fine."
))

conn.commit()
print("✅ NYC statute data inserted successfully.")





cur.close()
conn.close()