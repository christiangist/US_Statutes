import psycopg2

conn = psycopg2.connect(dbname="us_statutes", user="cgist14")
cur = conn.cursor()

cur.execute("INSERT INTO states (name, abbreviation) VALUES (%s, %s)", ("New York", "NY"))
conn.commit()
cur.close()
conn.close()