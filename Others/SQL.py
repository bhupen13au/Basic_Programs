import mysql.connector

mydb = mysql.connector.connect(host= "localhost", user= "root", password= "root")

mycursor = mydb.cursor()

mycursor.execute("USE mysqldb")

# mycursor.execute("CREATE TABLE students (name VARCHAR(20), age INTEGER(2), city VARCHAR(20))")

# for db in mycursor:
#     print(db)

sql = "INSERT INTO students (name,age,city) VALUES (%s,%s,%s)"
sds = [('Bivek',35,'pusat'),
       ('Jit',30,'akola'),
        ('Rahul',29,'pusat')]
mycursor.executemany(sql,sds)
mydb.commit()

# sql = "SELECT * FROM students WHERE age>26"
# mycursor.execute(sql)
#
# # for i in mycursor:
# #     print(i)
#
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)

# sql = "SELECT * FROM students WHERE name LIKE '%ra%'"
# mycursor.execute(sql)
#
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)

# sql = "SELECT * FROM students WHERE city = %s"
#
# mycursor.execute(sql,('pusat',))
#
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)

# sql = "SELECT * FROM students ORDER BY age DESC"
# mycursor.execute(sql)
#
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)

# sql = "UPDATE students SET age = 25 WHERE city = 'pusat' "
# mycursor.execute(sql)
# mydb.commit()
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)

# sql = "SELECT * FROM students LIMIT 5"
# mycursor.execute(sql)
#
# results = mycursor.fetchall()
#
# for result in results:
#     print(result)
