import sqlite3

conn = sqlite3.connect('example.db')  # Skapar databas-koppling eller skapa en db-fil om den inte redan finns

cursor = conn.cursor()  # Skapar en cursor så att vi kan jobba med databasen

# Skapa en tabell  om den inte redan existerar
cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')

# Lägga in värden i tabellen
cursor.execute("INSERT INTO users (name, age) VALUES ('Gudrun', 28);")

# Committa - dvs se till att detta verkligen blir av
conn.commit()

# Hämta värden från tabellen
cursor.execute("SELECT * FROM users")
print(cursor.fetchall())

# Stäng databaskopplingen
conn.close()
