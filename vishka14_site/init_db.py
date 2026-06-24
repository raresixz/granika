import sqlite3
import os

DB_NAME = "clients.db"

# если база уже есть — просто выходим
if os.path.exists(DB_NAME):
    print("База уже существует")
    exit()

conn = sqlite3.connect(DB_NAME)
cur = conn.cursor()

cur.execute("""
CREATE TABLE clients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    phone TEXT,
    service TEXT,
    status TEXT DEFAULT 'Новая'
)
""")

conn.commit()
conn.close()

print("База создана")