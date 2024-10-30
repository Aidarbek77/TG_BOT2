import sqlite3
from config import DB_PATH

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS homeworks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            name TEXT,
                            group_name TEXT,
                            homework_number INTEGER,
                            github_link TEXT
                          )''')
        conn.commit()

def save_homework(name, group_name, homework_number, github_link):
    with sqlite3.connect(DB_PATH) as conn:
        cursor = conn.cursor()
        cursor.execute('''INSERT INTO homeworks (name, group_name, homework_number, github_link)
                          VALUES (?, ?, ?, ?)''', (name, group_name, homework_number, github_link))
        conn.commit()
