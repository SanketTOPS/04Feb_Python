import pymysql

try:
    db = pymysql.connect(host="localhost", user="root", password="", database="pydb")
    print("Database connected!")
except Exception as e:
    print(e)

cr = db.cursor()
# Table Create
tbl_create = (
    "create table studinfo(id integer primary key auto_increment,name text, city text)"
)

try:
    cr.execute(tbl_create)
    print("Table created!")
except Exception as e:
    print(e)


# Insert Data
"""insert_data = "insert into studinfo(name,city)values('sanket','rajkot'),('nirav','baroda'),('hitesh','surat'),('mitesh','navsari'),('ashok','morbi')"

try:
    cr.execute(insert_data)
    db.commit()
    print("Record inserted!")
except Exception as e:
    print(e)"""


# Update Data
"""update_data = "update studinfo set name='pritesh',city='ahmedabad' where id=5"
try:
    cr.execute(update_data)
    db.commit()
    print("Record updated!")
except Exception as e:
    print(e)"""


# Delete Data
"""delete_data = "delete from studinfo where id=5"
try:
    cr.execute(delete_data)
    db.commit()
    print("Record deleted!")
except Exception as e:
    print(e)"""
