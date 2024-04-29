import sqlite3

def connect_to_database():
    conn = sqlite3.connect('users.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')
    conn.commit()

def main():
    conn = connect_to_database()
    create_table(conn)

    while True:
        choice = input("Hämta användare: ")
        cursor = conn.cursor()
        select_query = "SELECT * FROM users WHERE name=?"
        cursor.execute(select_query, (choice,))

        users = cursor.fetchall()
    
        print("\nDin användare:")
        for user in users:
            print(user)


    conn.close()

if __name__ == "__main__":
    main()

