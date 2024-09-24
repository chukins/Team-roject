from flask import Flask, request, render_template
import sqlite3
import hashlib
import string
acceptedChars = [x for x in string.punctuation+string.ascii_letters+string.digits]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        if len(username) <= 5 or len(username) >= 13:
            return render_template('error.html', error='Username must be between 6 and 12 characters')
        for letter in username:
            if letter not in acceptedChars:
                return render_template('error.html', error='Username contains invalid characters')
            
        password = request.form.get('password')
        if len(password) <= 7:
            return render_template('error.html', error='Password must be at least 8 characters, including a number and a special character')
        for letter in password:
            if letter not in acceptedChars:
                return render_template('error.html', error='Password contains invalid characters')
            
        hashed = hashlib.sha512(password.encode()).hexdigest()
        print(hashed)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO LoginDetails (Username, Password)
            VALUES (?, ?)
            ''', (username, hashed))
        conn.commit()
        conn.close()
    return render_template('login.html')
    


@app.route('/workplan')
def workplan():
    return render_template('WorkPlans.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

@app.route('/bmi', methods=['POST', 'GET'])
def bmi():
    return render_template('bmi.html')

if __name__ == '__main__':
    app.run(debug=True)