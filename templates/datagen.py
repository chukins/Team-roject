import sqlite3
conn = sqlite3.connect('database.db')

c = conn.cursor()

c.execute("""CREATE TABLE Log in details (
          username text,
          email text,
          Password text
          )""")
conn.commit()

conn.close()
