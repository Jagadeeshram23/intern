from . import app,table_no
from flask import render_template, request
import pymysql as ps
import sqlite3
import os.path





@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')


@app.route('/menu')
def menu():
    return render_template('menu.html')


@app.route('/book', methods=['GET', 'POST'])
def book():
    suc = -1
    if request.method == 'POST':
        try:
            # Connect to SQLite3 database and execute the INSERT
            

            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "database.db")
            with sqlite3.connect(db_path) as cn:
                customer = request.form.get("customer")
                ph_no = request.form.get("mobile")
                email = request.form.get("email")
                count = request.form.get("count")
                date = request.form.get("date")
                time_slot = request.form.get("time_slot")
                tableno = 0
                for i in table_no:
                    if table_no[i]==0:
                        tableno = i
                        table_no[i] = 1
                        suc = i
                        break
                else:
                    suc = 0
                if tableno:
                    cmd = cn.cursor()
                    query = "INSERT INTO restaurant(table_no, customer, ph_no, email, count, date, time_slot) VALUES(?, ?, ?, ?, ?, ?, ?);"
                    cmd.execute(query, (tableno, customer, ph_no, email, count, date, time_slot))
                    cmd.connection.commit()
                    cmd.close()
        finally:
            cn.close()
        return render_template('result.html',suc=suc)
    return render_template('book.html')


@app.route('/cancel', methods=['GET', 'POST'])
def cancel():
    suc = -1
    if request.method == 'POST':
        try:
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "database.db")
            with sqlite3.connect(db_path) as cn:
                customer = request.form.get("customer")
                ph_no = request.form.get("mobile")
                if customer and ph_no:
                    cmd = cn.cursor()
                    query = "DELETE FROM RESTAURANT WHERE customer=? and ph_no=?;"
                    cmd.execute(query, (customer, ph_no))
                    cmd.connection.commit()
                    cmd.close()
        finally:
            cn.close()
        return render_template('result.html',suc=suc, res=1)
    return render_template('cancel.html')


@app.route('/admin', methods=['Get', 'POST'])
def admin():
    if request.method == 'POST':
        password = request.form.get("password")
        if password == 'admin@1234':
            try:
            # Connect to SQLite3 database and execute the INSERT
                BASE_DIR = os.path.dirname(os.path.abspath(__file__))
                db_path = os.path.join(BASE_DIR, "database.db")
                with sqlite3.connect(db_path) as cn:
                    cmd = cn.cursor()
                    query = "SELECT * FROM RESTAURANT;"
                    cmd.execute(query)
                    cmd.connection.commit()
                    tables = cmd.fetchall()
                    cmd.close()
                    
            finally:
                cn.close()
            st = []
            for i in range(len(tables)):
                s = f'{tables[i][1]} has booked table {tables[i][0]} on {tables[i][4]} at {tables[i][5]}'
                st.append(s)
            return render_template('bookings.html', n=len(tables), st= st)
    return render_template('admin.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/allocate', methods=['Get', 'POST'])
def allocate():
    suc = -1
    admin = True
    if request.method == 'POST':
        for i in table_no:
            if table_no[i]==0:
                table_no[i] = 1
                suc = i
                break
    
    try:
        # Connect to SQLite3 database and execute the INSERT
        BASE_DIR = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(BASE_DIR, "database.db")
        with sqlite3.connect(db_path) as cn:
            cmd = cn.cursor()
            query = "SELECT * FROM RESTAURANT;"
            cmd.execute(query)
            cmd.connection.commit()
            tables = cmd.fetchall()
            cmd.close()                 
    finally:
        cn.close()
    st = []
    for i in range(len(tables)):
        s = f'{tables[i][1]} has booked table {tables[i][0]} on {tables[i][4]} at {tables[i][5]}'
        st.append(s)
    return render_template('bookings.html', n=len(tables), st= st)



@app.route('/bookings', methods=['Get', 'POST'])
def bookings():
    if request.method == 'POST':
        tbno = request.form['tbno']
        try:
        # Connect to SQLite3 database and execute the INSERT
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "database.db")
            with sqlite3.connect(db_path) as cn:
                table_no[int(tbno)]=0
                cmd = cn.cursor()
                query = "DELETE FROM RESTAURANT WHERE table_no=?;"
                cmd.execute(query,(tbno,))
                cmd.connection.commit()
                query = "SELECT * FROM RESTAURANT;"
                cmd.execute(query)
                cmd.connection.commit()
                tables = cmd.fetchall()
                cmd.close()
                    
        finally:
            cn.close()
        st = []
        for i in range(len(tables)):
            s = f'{tables[i][0]} has booked table {i+1} on {tables[i][4]} at {tables[i][5]}'
            st.append(s)
        return render_template('bookings.html', n=len(tables), st= st)
    if request.method == 'POST':
        
        try:
        # Connect to SQLite3 database and execute the INSERT
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "database.db")
            with sqlite3.connect(db_path) as cn:
                cmd = cn.cursor()
                query = "SELECT * FROM RESTAURANT;"
                cmd.execute(query)
                cmd.connection.commit()
                tables = cmd.fetchall()
                cmd.close()
                    
        finally:
            cn.close()
        st = []
        for i in range(len(tables)):
            s = f'{tables[i][0]} has booked table {i+1} on {tables[i][4]} at {tables[i][5]}'
            st.append(s)
        return render_template('bookings.html', n=len(tables), st= st)
    

@app.route('/closing', methods=['Get', 'POST'])
def closing():
    if request.method == 'POST':
        try:
        # Connect to SQLite3 database and execute the INSERT
            BASE_DIR = os.path.dirname(os.path.abspath(__file__))
            db_path = os.path.join(BASE_DIR, "database.db")
            with sqlite3.connect(db_path) as cn:
                for i in table_no:
                    table_no[i]=0
                cmd = cn.cursor()
                query = "DELETE FROM RESTAURANT;"
                cmd.execute(query)
                cmd.connection.commit()
                query = "SELECT * FROM RESTAURANT;"
                cmd.execute(query)
                cmd.connection.commit()
                tables = cmd.fetchall()
                cmd.close()
                    
        finally:
            cn.close()
        st = []
        for i in range(len(tables)):
            s = f'{tables[i][0]} has booked table {i+1} on {tables[i][4]} at {tables[i][5]}'
            st.append(s)
        return render_template('bookings.html', n=len(tables), st= st)