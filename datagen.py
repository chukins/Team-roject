import sqlite3
conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE LoginDetails (
          Username text UNIQUE,
          Password text NOT NULL
          )""")
conn.commit()

conn.close()
