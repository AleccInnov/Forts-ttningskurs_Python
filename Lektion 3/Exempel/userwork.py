import sqlite3
from dbfunc import *

def main():
    conn = connect_to_database()
    create_table(conn)

    while True:
        print("\nMenu:")
        print("1. Ny användare")
        print("2. Användarlista")
        print("3. Updatera användarens namn")
        print("4. Updatera användarens ålder")
        print("5. Radera användare")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            add_user(conn)
        elif choice == '2':
            view_users(conn)
        elif choice == '3':
            update_user_name(conn)
        elif choice == '4':
            update_user_age(conn)
        elif choice == '5':
            delete_user(conn)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

    conn.close()

if __name__ == "__main__":
    main()
