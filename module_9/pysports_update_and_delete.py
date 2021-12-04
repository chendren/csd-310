import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='pysports',
                                         user='root',
                                         password='Ostrich%2020')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
        print("MySQL connection is open")

cursor = connection.cursor()

# Update newly added player's team to different team_name value


cursor.execute("DELETE FROM players WHERE first_name = 'Amy'")

cursor.execute("SELECT player_id, first_name, last_name, team_name from players inner join team on players.team_id = team.team_id ORDER BY player_id")

players2 = cursor.fetchall()

print("-- DISPLAYING PLAYERS AFTER UPDATE --")
for players in players2:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team Name: {}".format(players[3]))
    print("")

input("\n\n Press any key to continue. . . ")