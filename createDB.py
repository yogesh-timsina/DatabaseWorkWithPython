import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="")
cursor=conn.cursor()
cursor.execute("create database mydb")
print("Creating database successful")
cursor.close()
conn.close()