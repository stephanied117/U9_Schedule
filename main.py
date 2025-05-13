import mysql.connector

connection = mysql.connector.connect(user='kyley9',
                                    password='224085274',
                                    host='10.8.37.226',
                                    database='kyley9_db')

cursor = connection.cursor()
query="CREATE TABLE"
cursor.execute(query)
print("Enter a student ID: ")
query=""
cursor.execute(query)
print("Period: " )
print("Course: " )
print("Room: " )
print("Teacher: " )

