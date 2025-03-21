import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",password="",db="mydb")
cursor=conn.cursor()
cursor.execute("""INSERT INTO studentdetail(id,name,rollno)
    values(1,"Yogesh",1),(2,"swikrit",2),(3,"Sushant",3)""")
conn.commit()
print(cursor.rowcount,"Data are insert")
cursor.close()
conn.close()