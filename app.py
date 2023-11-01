import sys

# Disable .pyc file generation
sys.dont_write_bytecode = True

from flask import Flask, render_template, request, redirect, url_for, session, flash, request
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import secrets
from config import DATABASE_CONFIG
from secret import SECRET_KEY
import mysql.connector
import datetime


app = Flask(__name__)
app.secret_key = SECRET_KEY

# Use the database configuration from the config file
db_connection = mysql.connector.connect(**DATABASE_CONFIG)

app.config['MYSQL_HOST'] = DATABASE_CONFIG['host']
app.config['MYSQL_USER'] = DATABASE_CONFIG['user']
app.config['MYSQL_PASSWORD'] = DATABASE_CONFIG['password']
app.config['MYSQL_DB'] = DATABASE_CONFIG['database']

mysql = MySQL(app)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account and account['password'] == password:
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            return redirect(url_for('dashboard'))
        else:
            flash('danger', 'Incorrect username or password!')

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form and 'name' in request.form and 'phone' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        name = request.form['name']
        phone = request.form['phone']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM users WHERE username = %s', (username,))
        account = cursor.fetchone()
        if account:
            flash('danger', 'Account already exists!')
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            flash('danger', 'Invalid email address!')
        elif not re.match(r'[A-Za-z0-9]+', username):
            flash('danger', 'Username must contain only characters and numbers!')
        elif not username or not password or not email or not name or not phone:
            flash('danger', 'Please fill out the form!')
        else:
            cursor.execute('INSERT INTO users (username, password, email, name, phone) VALUES (%s, %s, %s, %s, %s)',
                           (username, password, email, name, phone))
            mysql.connection.commit()
            flash('You have successfully registered!', 'You have successfully registered!')

    return render_template('register.html')

@app.route('/booking')
def booking():
    return render_template('booking.html')

@app.route('/dashboard')
def dashboard():
    return render_template('patient.html')

def generate_token():
    # Generate a random token (e.g., a 16-character alphanumeric string)
    return secrets.token_hex(8)

@app.route('/book_appointment', methods=['POST'])
def book_appointment():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        dob_str = request.form['dob']  # Get the date of birth as a string
        phone = request.form['phone']
        email = request.form['email']
        insurance_info = request.form['insurance']
        reason_for_visit = request.form['reason']
        medical_history = request.form['medical-history']

        if not name or not age or not dob_str or not phone or not email:
            flash('danger', 'All fields are required')
            return redirect(url_for('booking'))

        # Parse and convert the date string to the "YYYY-MM-DD" format
        formats = ["%d/%m/%Y", "%d-%m-%Y"]

        dob = None
        for format in formats:
            try:
                dob = datetime.datetime.strptime(dob_str, format).strftime("%Y-%m-%d")
                break
            except ValueError:
                continue

        if dob is None:
            flash('danger', 'Invalid date format')
            return redirect(url_for('booking'))

        # Generate the token with the format "HC0000"
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT MAX(token) AS max_token FROM appointments')
        max_token = cursor.fetchone()
        if max_token and max_token['max_token']:
            last_token_number = int(max_token['max_token'][2:])  # Extract the numeric part
            new_token_number = last_token_number + 1
            token = f'HC{new_token_number:04d}'  # Format the new token number
        else:
            # If there are no existing tokens, start from "HC0001"
            token = 'HC0001'

        # Insert data into the database, including the generated token
        cursor.execute('INSERT INTO appointments (token, name, age, dob, phone, email, insurance_info, reason_for_visit, medical_history) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)',
                       (token, name, age, dob, phone, email, insurance_info, reason_for_visit, medical_history))
        mysql.connection.commit()
        cursor.close()

        flash('success', f'Appointment booked successfully! Your appointment token is: {token}')
        return redirect(url_for('display_tokens'))

    return render_template('booking.html')


@app.route('/display_tokens')
def display_tokens():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute('SELECT token FROM appointments')
    tokens = cursor.fetchall()
    cursor.close()

    token_list = [token['token'] for token in tokens]

    return render_template('token.html', token_list=token_list)


if __name__ == '__main__':
    app.run(debug=True)
