# Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
# Crée un point de montage pour le volume des données persistantes
VOLUME /data
# Expose le port sur lequel l'application tourne
EXPOSE 5000
# Commande pour lancer l'application
CMD ["python", "app.py"]
