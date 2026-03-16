import mysql.connector
import os

def get_connection():
    """Connexion à la base MySQL via variables Kubernetes."""

    conn = mysql.connector.connect(
        host=os.getenv("MYSQL_HOST", "mysql"),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", "password"),
        database=os.getenv("MYSQL_DATABASE", "imcdb")
    )

    return conn


def init_db():
    """Créer la table si elle n'existe pas."""

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS imc_records (
            id INT AUTO_INCREMENT PRIMARY KEY,
            taille FLOAT,
            poids FLOAT,
            imc FLOAT,
            categorie VARCHAR(50),
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()
    conn.close()


def insert_record(taille, poids, imc, categorie):
    """Enregistrer un calcul IMC."""

    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO imc_records (taille, poids, imc, categorie)
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (taille, poids, imc, categorie))

    conn.commit()
    conn.close()
