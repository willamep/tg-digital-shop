import sqlite3

def get_categories():
    conn = sqlite3.conect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, cat_name FROM categories ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows