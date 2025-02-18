import sqlite3
from flask import Flask # type: ignore
import os

app = Flask(__name__)

# Configuração do banco de dados
DATABASE_PATH = '/data/example.db'

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/data')
def read_data():
    conn = sqlite3.connect(DATABASE_PATH)
    cursor = conn.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, message TEXT)')
    cursor.execute('INSERT INTO messages (message) VALUES ("Hello from SQLite!")')
    conn.commit()

    cursor.execute('SELECT * FROM messages')
    data = cursor.fetchall()

    conn.close()
    return str(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)