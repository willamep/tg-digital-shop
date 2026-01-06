import sqlite3

def get_categories():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, cat_name FROM categories ORDER BY id")
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_items(cat_id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("SELECT id, item_name, price FROM items WHERE cat_id = ?", (cat_id,))
    rows = cursor.fetchall()
    conn.close()
    return rows
