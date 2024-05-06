import sqlite3
from dbfunc import *

def main():
    conn = connect_to_database()
    create_table(conn)

    while True:
        print("\nMenu:")
        print("1. Vill du spela?")
        print("2. Highscore")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            play(conn)
        elif choice == '2':
            view_users(conn)
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
