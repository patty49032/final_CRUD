import pymysql
import bcrypt

conn = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='school_db',
                             cursorclass=pymysql.cursors.DictCursor)

if conn:
    print("db connect")
else:
    print("error")

# with conn:
#    with conn.cursor() as cursor:
#         # Read a single record
#         sql = "SELECT * FROM test"
#         cursor.execute(sql)
#         result = cursor.fetchone()
#         print(result)

#register admins
with conn:
   with conn.cursor() as cursor:
        username = "admin"
        password = "12345678".encode('utf-8')
        hash_pass = bcrypt.hashpw(password, bcrypt.gensalt())

        sql = "INSERT INTO admin (username, password) VALUES (%s,%s)"
        cursor.execute(sql, (username, hash_pass,))
        conn.commit()
        print("success")
