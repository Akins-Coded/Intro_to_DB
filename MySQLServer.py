import mysql.connector
from mysql.connector import Error

def create_database():
    try:
        # Establishing connection to MySQL server
        connection = mysql.connector.connect(
            host='localhost',
            user='your_username',  # Replace with your MySQL username
            password='your_password'  # Replace with your MySQL password
        )

        # Creating a cursor object using the cursor() method
        cursor = connection.cursor()

        # Creating database if not exists
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error creating database: {e}")

    finally:
        # Closing database connection if still open
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

if __name__ == "__main__":
    create_database()
