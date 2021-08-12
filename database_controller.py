import sqlite3
con = sqlite3.connect('database_file.db')

cur = con.cursor()

cur.execute('''CREATE TABLE players
            (lastname text,
            firstname text,
            position text,
            team text,
            college text)''')

con.commit()
con.close()
