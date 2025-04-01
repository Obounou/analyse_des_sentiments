from prometheus_client import start_http_server, Gauge
import psutil
import time

# Création des métriques pour le CPU et la RAM
cpu_usage = Gauge("cpu_usage", "CPU usage in percentage")
ram_usage = Gauge("ram_usage", "RAM usage in MB")

def monitor():
    start_http_server(8000)  # Démarrer un serveur HTTP sur le port 8000 pour exposer les métriques
    while True:
        cpu_usage.set(psutil.cpu_percent())  # Capture l'utilisation du CPU
        ram_usage.set(psutil.virtual_memory().used / (1024 * 1024))  # Capture la RAM utilisée en Mo
        time.sleep(5)  # Rafraîchit toutes les 5 secondes

if __name__ == "__main__":
    monitor()
