from flask import g
import sqlite3

DATABASE = 'leads.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db(app):
    with app.app_context():
        db = get_db()
        db.execute('''CREATE TABLE IF NOT EXISTS leads
                      (id INTEGER PRIMARY KEY AUTOINCREMENT,
                       isim TEXT NOT NULL,
                       telefon TEXT NOT NULL,
                       mesaj TEXT,
                       tarih TIMESTAMP DEFAULT CURRENT_TIMESTAMP)''')
        db.commit()

def lead_ekle(isim, telefon, mesaj):
    db = get_db()
    db.execute("INSERT INTO leads (isim, telefon, mesaj) VALUES (?, ?, ?)",
                 (isim, telefon, mesaj))
    db.commit()

def tum_leadler():
    db = get_db()
    cursor = db.execute("SELECT * FROM leads ORDER BY tarih DESC")
    return cursor.fetchall()