# Utiliser une image Python officielle
FROM python:3.11-slim

# Installer ffmpeg (nécessaire pour audio/vidéo)
RUN apt-get update && apt-get install -y ffmpeg && rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail
WORKDIR /app

# Copier requirements et installer dépendances
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copier tout le projet
COPY . .

# Exposer le port Flask
EXPOSE 8021

# Lancer l'application
CMD ["python", "app.py"]
