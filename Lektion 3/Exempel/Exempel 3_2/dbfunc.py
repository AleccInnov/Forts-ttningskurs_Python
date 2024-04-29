import sqlite3

def connect_to_database():
    conn = sqlite3.connect('tasks.db')
    return conn

def create_table(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    age INTEGER
                )''')
    conn.commit()

def add_user(conn):
    name = input("Vad heter användaren? ")
    age = input("Hur gammal är användaren? ")
    
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", (name, age))
    conn.commit()
    print("Användaren är tillagd!")

def view_users(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    
    print("\nAlla användare:")
    for user in users:
        print(user)

def update_user_name(conn):
    user_id = int(input("Vilket användarID ska uppdateras? "))
    new_name = input("Lägg in ett nytt namn. ")
      
    cursor = conn.cursor()

    update_query = "UPDATE users SET name = ? WHERE id = ?"

    cursor.execute(update_query, (new_name, user_id))
    conn.commit()
    print("Användarnamnet uppdaterad!")

def update_user_age(conn):
    user_id = int(input("Vilket användarID ska uppdateras? "))
    new_age = input("Lägg in en ny ålder. ")
      
    cursor = conn.cursor()

    update_query = "UPDATE users SET age =? WHERE id = ?"
    print (update_query)
    cursor.execute(update_query, (new_age, user_id))
    conn.commit()
    print("Användarens ålder uppdaterad!")


def delete_user(conn):
    user_id = int(input("Vilket id vill du radera? "))

    cursor = conn.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print("Användaren har raderats!")

