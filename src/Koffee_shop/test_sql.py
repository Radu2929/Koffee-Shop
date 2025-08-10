import mysql.connector
from mysql.connector import Error

# Connect to MySQL
connection = mysql.connector.connect(
    host="192.168.0.139",       # your VM IP
    user="your_user",           # your MySQL username
    password="your_password",   # your MySQL password
    database="koffee_shop_db"      # your database name
)

mycursor = connection.cursor()

mycursor.execute("SHOW TABLES")

myresult = mycursor.fetchall()

print(myresult)
