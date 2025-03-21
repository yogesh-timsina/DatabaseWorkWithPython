import mysql.connector
conn=mysql.connector.connect(host="localhost",user="root",db="mydb",password="")
cursor=conn.cursor()
DBstructure="Insert into studentdetail(id,name,rollno) values(%s,%s,%s)"
DB_list=[(4,"samin",4),(5,"anil",5)]
cursor.executemany(DBstructure,DB_list)
conn.commit()
print(cursor.rowcount," Data are store in database ")
conn.close()
cursor.close()