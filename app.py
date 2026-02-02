from flask import Flask, request, render_template
import sqlite3
from database import init_db

app = Flask(__name__)

# Initialisation de la base au démarrage
init_db()

def save_record(taille, poids, imc, categorie):
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO imc_records (taille_cm, poids_kg, imc, categorie) VALUES (?, ?, ?, ?)",
        (taille, poids, imc, categorie)
    )
    conn.commit()
    conn.close()

@app.route("/", methods=["GET", "POST"])
def imc():
    imc_value = None
    categorie = None
    taille_cm = ""
    poids_kg = ""

    if request.method == "POST":
        taille_cm = request.form.get("taille", "")
        poids_kg = request.form.get("poids", "")

        try:
            t = float(taille_cm)
            p = float(poids_kg)

            taille_m = t / 100
            imc_value = round(p / (taille_m ** 2), 2)

            if imc_value < 18.5:
                categorie = "Insuffisance pondérale"
            elif imc_value < 25:
                categorie = "Corpulence normale"
            elif imc_value < 30:
                categorie = "Surpoids"
            else:
                categorie = "Obésité"

            # 🔹 Sauvegarde en base
            save_record(t, p, imc_value, categorie)

        except:
            categorie = "Erreur dans les valeurs saisies"

    return render_template(
        "index.html",
        taille_cm=taille_cm,
        poids_kg=poids_kg,
        imc_value=imc_value,
        categorie=categorie
    )

@app.route("/historique")
def historique():
    conn = sqlite3.connect("imc.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM imc_records ORDER BY created_at DESC")
    records = cursor.fetchall()
    conn.close()

    return render_template("historique.html", records=records)
