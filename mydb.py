import mysql.connector

database = mysql.connector.connect(
    host = ' localhost',
    user = 'root',
    passwd = '1234',
)

# prepare a cursor object
cursorObject = database.cursor()

# create database
cursorObject.execute("CREATE DATABASE elderco")
print('all done!')
