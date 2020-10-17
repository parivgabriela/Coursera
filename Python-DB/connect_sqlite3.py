import sqlite3 
import hashlib
conn =sqlite3.connect(":memory")
cursor=conn.cursor()
#creo la tabla
cursor.execute=("""CREATE TABLE currency
                    (ID integer primary key, name text, symbol text)""")


#inserto los valores
cursor.execute("INSERT INTO currecy VALUES (1, 'Peso (ARG)','$')")
cursor.execute("INSERT INTO currecy VALUES (1, 'Dolar','U$S')")
#guardo los cambios
conn.commit()
#revierto los cambios, se borran los insert
#conn.rollback() 

query="SELECT * FROM currency"
currencies=cursor.execute(query).fetchall()
print(currencies)
conn.close()    

#crear funcion
def md5sum(t):
    return hashlib.md5(t).hexdigest()
conn.sqlite3.connect(":memory:")
conn.create_function("md5",1,md5sum)

cursor.execute("select md5(?)",(b"foo"))
print(cursor.fetchone()[0])

conn.close()

class MySum:
    def __init__(self):
        self.count=0
    def step(self,value):
        self.count+=value
    def finalize(self):
        return self.count

conn=sqlite3.connect(":memory:")
conn.create_function("mysum",1,MySum)
cursor.=conn.cursor()
cursor.execute("create table test(i)")
cursor.execute("insert into test(i) values(1)")
cursor.execute("insert into test(i) values(2)")
cursor.execute("select mysum (i) from test")
print(cursor.fetchone()[0])
conn.close()
