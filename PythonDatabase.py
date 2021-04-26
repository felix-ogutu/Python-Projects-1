import mysql.connector

root = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="mySupermarket"
)
mycursor = root.cursor()

# create table customers
mycursor.execute("Create table customers(name vanchar(255),address vanchar(255))")
