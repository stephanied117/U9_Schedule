import mysql.connector

connection = mysql.connector.connect(user='kyley9',
                                    password='224085274',
                                    host='10.8.37.226',
                                    database='kyley9_db')

cursor = connection.cursor()
query="CREATE TABLE"
cursor.execute(query)
status=input("Are you a teacher or a student?\n")
query=""
input("Enter a Teacher ID:\n")
query=""
input("Enter a Student ID:\n")
query=""
cursor.execute(query)
print("SCHEDULE")
schedule=""

print("Period: ")
print("Course: ")
print("Room: ")
print("Teacher: ")

