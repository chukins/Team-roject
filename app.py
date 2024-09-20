from flask import Flask, request, render_template
import sqlite3


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        print(username, password)
        conn = sqlite3.connect('database.db')
        c = conn.cursor()
        c.execute('''
            INSERT INTO LoginDetails (Username, Password)
            VALUES (?, ?)
            ''', (username, password))
        conn.commit()
        conn.close()
    return render_template('login.html')
    


@app.route('/workplan')
def workplan():
    return render_template('WorkPlans.html')

@app.route('/about', methods=['POST', 'GET'])
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)