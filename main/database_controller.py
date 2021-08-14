import sqlite3

# This function reads organizedfootball.txt and creates a player object.
# Once the player object is full, player values are pushed to the database.
def write_player_data_to_db():
    player = []

    con = sqlite3.connect('database_file.db')
    cur = con.cursor()

    with open('organizedfootball.txt', 'r') as filestream:
        for line in filestream:
            datalist = line.split(", ")

    for value in datalist:
        player.append(value)
        if(len(player) == 5):
            cur.execute('INSERT INTO players VALUES (:lastname, :firestname, :position, :team, :college)', (player[0], player[1], player[2], player[3], player[4]))
            # print(player)
            player.clear()

    con.commit()
    con.close()
            
def create_db():
    con = sqlite3.connect('database_file.db')
    cur = con.cursor()

    cur.execute('''CREATE TABLE IF NOT EXISTS players
            (lastname text,
            firstname text,
            position text,
            team text,
            college text)''')

    con.commit()
    con.close()
