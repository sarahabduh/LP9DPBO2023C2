import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="db_praktikum"
)

dbcursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = [("Van", "Mountain 21"),
       ("John", "Highway 21"),
       ("Raven", "Suncet Terrace"),
       ("Kedama", "Pet Shop")]

dbcursor.executemany(sql, val)

mydb.commit()

print(dbcursor.rowcount, "record inserted.")

sql_update = "UPDATE customers SET address='River Town' WHERE name='Kedama'"
dbcursor.execute(sql_update)
mydb.commit()

sql_delete = "DELETE FROM customers WHERE address='Mountain 21'"
dbcursor.execute(sql_delete)
mydb.commit()

print(dbcursor.rowcount, "record(s) deleted")

dbcursor.execute("SELECT * FROM customers")
myresult = dbcursor.fetchall()

for x in myresult:
    print(x)

mydb.close()