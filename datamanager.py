import time
import random
from eventos import EventManager

class RealTimeDataManager:
    def __init__(self):
        # Inicializa los valores iniciales de temperatura y humedad
        self.data = {"temperatura": 25.0, "humedad": 60.0}
        # Crea una instancia del EventManager
        self.event_manager = EventManager()

    def start_real_time_updates(self):
        # Inicia un bucle infinito para generar los datos
        while True:
            # Espera 3 segundos antes de nuevo los datos
            time.sleep(3)
            # Genera de nuevo los datos
            self.generate_real_time_data()
            # Notifica a los suscriptores que los datos se actualizaron
            self.event_manager.notify("datos_actualizados", self.data)

    def generate_real_time_data(self):
        # Genera datos aleatorios, lo cual simula los cambios en temperatura y humedad
        self.data["temperatura"] += random.uniform(-1.0, 1.0)
        self.data["humedad"] += random.uniform(-2.0, 2.0)
