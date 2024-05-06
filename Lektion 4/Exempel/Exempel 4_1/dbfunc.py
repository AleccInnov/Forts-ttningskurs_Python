import sqlite3

def connect_to_database():
    conn = sqlite3.connect('lesson3.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS highscore (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    score INTEGER
                )''')
    
    cursor.execute('''CREATE TABLE IF NOT EXISTS game (
                    id INTEGER PRIMARY KEY,
                    value TEXT NOT NULL
                )''')
    conn.commit()

def play(conn):
    cursor = conn.cursor()
    win = 0
    loose = 0

    name = input("Vad heter du? ")
    game_choice = input("Sten, sax eller påse? ")

    if game_choice.upper()=="STEN":
        game_choice = "rock"
    elif game_choice.upper()=="PÅSE":
        game_choice = "paper"
    elif game_choice.upper()=="SAX":
        game_choice = "scissors"
    else:
        print("Felaktigt val!")
        
    cursor.execute("SELECT value FROM game ORDER BY RANDOM()")
    answer = cursor.fetchone()[0]  # Första elementet hämtas

    if game_choice == "rock":
        if answer == "rock":
            print("Oavgjort, försök igen")
        elif answer == "paper":
            win = 1
        else:
            loose = 1
    elif game_choice == "paper":
        if answer == "rock":
            loose = 1
        elif answer == "scissors":
            win = 1
        else:
            print("Oavgjort, försök igen")
    elif game_choice == "scissors":
        if answer == "rock":
            loose = 1
        elif answer == "paper":
            win = 1
        else:
            print("Oavgjort, försök igen")

    if win == 1:
        
        cursor.execute("SELECT COUNT(*) AS HITS FROM highscore WHERE name = ?", (name,))
        hits = cursor.fetchone()[0]  # Hämtar första
        if hits > 0:
            update_query = "UPDATE highscore SET score = score + 1 WHERE name = ?"
            cursor.execute(update_query, (name,))
        else:
            cursor.execute("INSERT INTO highscore (name, score) VALUES (?,?)", (name, 1))
            
        conn.commit()
        print("Du vann!")
    elif loose == 1:
        print("Du förlorade, försök igen")

    cursor.close()

def view_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM highscore ORDER BY score DESC")
    users = cursor.fetchall()
    
    print("\nHighscorelistan:")
    for user in users:
        print(user)

    cursor.close()



