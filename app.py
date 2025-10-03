# app.py
from flask import Flask
import sqlite3
import os

app = Flask(__name__) # Correction: __name__ au lieu de _name__

# Le chemin de la base de données dans le volume Docker
DB_PATH = '/data/app.db'

def init_db():
    # S'assure que le dossier /data existe
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    if not os.path.exists(DB_PATH):
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        # Crée la table pour les messages
        cursor.execute('CREATE TABLE IF NOT EXISTS messages (id INTEGER PRIMARY KEY, content TEXT)')
        conn.commit()
        conn.close()

@app.route('/')
def index():
    return "Bienvenue sur l'app Flask avec stockage persistant!"

@app.route('/messages', methods=['GET', 'POST'])
def messages():
    init_db()
    # Le reste de la logique pour afficher/ajouter des messages irait ici
    return "Gestion des messages."

if __name__ == '__main__':
    # Initialise la DB au premier lancement
    init_db()
    app.run(host='0.0.0.0', port=5000)
