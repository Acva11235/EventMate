import mysql.connector
conn= mysql.connector.connect(host="localhost", user="root", password= "Mysql1234")
print()
conn.close()
