import sqlite3
conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE LoginDetails (
          Username text Unique,
          Email text Unique,
          Password text
          )""")
conn.commit()

conn.close()
