import mysql.connector

Supermart = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password"
)
print(Supermart)

mycursor = Supermart.cursor()
mycursor.execute("CREATE DATABASE Eastmatt")



for x in mycursor:
    print(x)
