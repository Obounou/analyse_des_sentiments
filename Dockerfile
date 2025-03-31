# 1️⃣ Utiliser une image de base légère avec Python
FROM python:3.9-slim

# 2️⃣ Définir le répertoire de travail dans le conteneur
WORKDIR /app

# 3️⃣ Copier le fichier des dépendances dans l’image Docker
COPY requirements.txt .

# 4️⃣ Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Copier tout le projet dans le conteneur
COPY . .

# 6️⃣ Exposer le port si on utilise une API Flask (optionnel)
EXPOSE 5000

# 7️⃣ Définir le point d'entrée (commande à exécuter quand le conteneur démarre)
CMD ["python", "inference.py"]

