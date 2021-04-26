import mysql.connector

Supermarket = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="password"
)

mycursor = Supermarket.cursor()
mycursor.execute("CREATE DATABASE School")
