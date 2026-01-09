import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="bankuser",
    password="bank123",
    database="bank"
)

print("CONNECTED OK")
conn.close()
