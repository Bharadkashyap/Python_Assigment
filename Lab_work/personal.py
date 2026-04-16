#31-01-2024
import mysql.connector
cn=mysql.connector.connect(host="localhost",user="root",password="",database="personal")
c1=cn.cursor()
"""
#creating table
t="create table personal(rno int,sname varchar(10));"
c1.execute(t)
cn.commit()
#inserting
a="insert into personal values(1,'kashyap');"
c1.execute(a)
cn.commit()
#selecting
b="select * from personal "
c1.execute(b)
ta=c1.fetchall()
for i in ta:
    print(i)
#updating
c="update personal set sname='hardik' where sname='hardip'"
c1.execute(c)
cn.commit()
#deleting
d="delete from personal where sname='hardik'"
c1.execute(d)
cn.commit()
#altering
e="alter table personal add(city varchar(20))"
c1.execute(e)
cn.commit()"""
f="truncate table personal"
c1.execute(f)
cn.commit()
