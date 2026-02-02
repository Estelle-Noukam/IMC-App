# Application Web - Calculateur IMC

## Description
Application web permettant de calculer l'IMC (Indice de Masse Corporelle) et d'enregistrer un historique dans une base SQLite.

## Technologies
- Python / Flask
- SQLite
- HTML (templates Jinja2)
- CSS (static)

## Installation / Exécution (local)
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
flask --app app run --host=0.0.0.0 --port=5000

## Accès
- Application accessible en local via : http://localhost:5000

