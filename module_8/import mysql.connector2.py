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

cursor.execute("SELECT team_id, team_name, mascot FROM team")

teams = cursor.fetchall()

print("-- DISPLAYING TEAM RECORDS --")
for team in teams:
    print("Team ID: {}".format(team[0]))
    print("Team Name: {}".format(team[1]))
    print("Mascot: {}".format(team[2]))
    print("")

cursor.execute("SELECT player_id, first_name, last_name, team_id FROM players")

players2 = cursor.fetchall()

print("-- DISPLAYING PLAYER RECORDS --")
for players in players2:
    print("Player ID: {}".format(players[0]))
    print("First Name: {}".format(players[1]))
    print("Last Name: {}".format(players[2]))
    print("Team ID: {}".format(players[3]))
    print("")

input("\n\n Press any key to continue. . . ")