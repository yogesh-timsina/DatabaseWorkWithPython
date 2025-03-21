import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",db="mydb")
cursor=conn.cursor()
cursor.execute("""Create table StudentDetail (
    id int primary key,
    name varchar(30),
    rollno int
    )""")
print("creating table successful")
conn.close()
cursor.close()