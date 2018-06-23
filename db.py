import sqlite3, os
con = sqlite3.connect(os.getcwd() + '/db.sqlite3')
cursor = con.cursor()
# cursor.execute("INSERT INTO Users(ID, Name, Age) VALUES(1, 'Amr', 24)")
cursor.execute("SELECT * FROM Users")
print(cursor.fetchall())
con.commit()
cursor.close()
con.close()