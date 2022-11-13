from flask import Flask, render_template, url_for, request, redirect, session, flash
import pymysql
import bcrypt

app = Flask(__name__)

conn = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        db='school_db',
        cursorclass=pymysql.cursors.DictCursor
)

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/index')
def index():
    return render_template("index.html")

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        if len(request.form['username']) > 0 and len(request.form['password']) > 0 :
            username = request.form['username']
            password = request.form['password'].encode('utf-8')

            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM admin WHERE username=%s", (username))
                conn.commit()
                result = cursor.fetchone() 
                if result == None:
                    error = "Invalid credentials"
                    return render_template("login.html", error=error)
                elif len(result) > 0:
                    if bcrypt.hashpw(password, result['password'].encode('utf-8')) == result['password'].encode('utf-8'):
                        session['username'] = result['username']
                        return render_template("index.html")
                    else:
                        error = "Invalid credentials"
                        return render_template("login.html", error=error)
                else:
                    error = "Invalid credentials"
                    return render_template("login.html", error=error)
    else:
        return render_template("login.html")

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route("/bb1")
def bb1():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM bb1"
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchall()
    return render_template('bb1.html', datas=result)

@app.route('/bb1-add-view')
def bb1addview():
    return render_template('bb1-add.html')

@app.route('/bb1add',methods=["POST"])
def bb1add():
    if request.method=="POST":
        bid = request.form['bid']
        name = request.form['name']
        with conn.cursor() as cursor:
            sql1 = "INSERT INTO bb1 (bid,name) VALUES (%s,%s)"
            cursor.execute(sql1,(bid,name))
            conn.commit()
        return redirect(url_for('bb1'))

@app.route('/bb1-edit/<string:id_data>',methods=['GET'])
def bb1edit(id_data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bb1 WHERE id=%s",(id_data))
        conn.commit()
        result = cursor.fetchall()
    return render_template('bb1-edit.html',datas=result)

@app.route('/bb1update',methods=["POST"])
def bb1update():
    if request.method=="POST":
        id_update = request.form['id']
        bid=request.form['bid']
        name=request.form['name']
        with conn.cursor() as cursor:
            sql1 = "UPDATE bb1 SET bid=%s, name=%s WHERE id=%s"
            cursor.execute(sql1,(bid,name,id_update))
            conn.commit()
        return redirect(url_for('bb1'))

@app.route('/bb1-delete/<string:id_data>',methods=['GET'])
def bb1delete(id_data):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM bb1 WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('bb1'))

@app.route("/bb2")
def bb2():
    with conn.cursor() as cursor:
        sql = "SELECT * FROM bb2"
        cursor.execute(sql)
        conn.commit()
        result = cursor.fetchall()
    return render_template('bb2.html', datas=result)

@app.route('/bb2-add-view')
def bb2addview():
    return render_template('bb2-add.html')

@app.route('/bb2add',methods=["POST"])
def bb2add():
    if request.method=="POST":
        bid = request.form['bid']
        name = request.form['name']
        with conn.cursor() as cursor:
            sql1 = "INSERT INTO bb2 (bid,name) VALUES (%s,%s)"
            cursor.execute(sql1,(bid,name))
            conn.commit()
        return redirect(url_for('bb2'))

@app.route('/bb2-edit/<string:id_data>',methods=['GET'])
def bb2edit(id_data):
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM bb2 WHERE id=%s",(id_data))
        conn.commit()
        result = cursor.fetchall()
    return render_template('bb2-edit.html',datas=result)

@app.route('/bb2update',methods=["POST"])
def bb2update():
    if request.method=="POST":
        id_update = request.form['id']
        bid=request.form['bid']
        name=request.form['name']
        with conn.cursor() as cursor:
            sql1 = "UPDATE bb2 SET bid=%s, name=%s WHERE id=%s"
            cursor.execute(sql1,(bid,name,id_update))
            conn.commit()
        return redirect(url_for('bb2'))

@app.route('/bb2-delete/<string:id_data>',methods=['GET'])
def bb2delete(id_data):
    with conn.cursor() as cursor:
        cursor.execute("DELETE FROM bb2 WHERE id=%s",(id_data))
        conn.commit()
    return redirect(url_for('bb2'))

if __name__ == "__main__":
    app.secret_key = "abc#123()%"
    app.run(debug=True)