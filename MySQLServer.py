import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user= "root",
    password="yourpassword",
)



mycursor = db.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
db.commit()
print("Database 'alx_book_store' created successfully!")