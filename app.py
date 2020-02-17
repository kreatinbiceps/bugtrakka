from flask import Flask, redirect, url_for, request, render_template, g
import random
import string
import sqlite3 as lite

DATABASE = "./tasks.db"

if not os.path.exists(DATABASE):
    con = lite.connect(DATABASE)
    cursor = con.cursor()
    cursor.execute("CREATE TABLE url (ID INTEGER PRIMARY KEY AUTOINCREMENT, HEAD TEXT, DESC TEXT, CAT TEXT);")
    con.commit()
    cursor.execute("INSERT INTO url VALUES('1', 'Short text about bug');")
    con.commit()
    con.close()


@app.route('/')
def index():
    

    return render_template('index.html')




if __name__ == '__main__':
    app.run(host='192.168.1.5', port=42099, debug=True)

