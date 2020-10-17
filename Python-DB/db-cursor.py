import sqlite3 
import hashlib
conn =sqlite3.connect(":memory:")
cursor=conn.cursor()
#creo la tabla
cursor.execute=("""CREATE TABLE currency
                    (ID integer primary key, name text, symbol text)""")


#inserto los valores
cursor.execute("INSERT INTO currecy VALUES (1, 'Peso (ARG)','$')")
cursor.execute("INSERT INTO currecy VALUES (1, 'Dolar','U$S')")
#guardo los cambios
conn.commit()

query="SELECT * FROM currency"
currencies=cursor.execute(query).fetchone()
print(cursor.fetchone())
print(cursor.fetchone())
currencies=cursor.execute(query).fetchall()
print(currencies)

conn.close()
