import sqlite3
from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy


#function that creates database connection and returns it
##opens connection to db
def get_db_connection():
    #connection object
    conn = sqlite3.connect('database.db')
    #row factory creates a python dictionary
    conn.row_factory = sqlite3.Row
    return conn



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    #opens database connection and makes it an object
    conn = get_db_connection()
    #SQL query to fetch all
    posts = conn.execute('SELECT * FROM posts').fetchall()
    #close connection
    conn.close()
    #returns our posts so we can use them in index.html
    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(debug=True)