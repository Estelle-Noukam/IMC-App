import sqlite3

DB_NAME = "imc.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imc_records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            taille_cm REAL,
            poids_kg REAL,
            imc REAL,
            categorie TEXT,
            created_at DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()
