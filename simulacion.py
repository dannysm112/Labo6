import time
import threading
from datamanager import RealTimeDataManager

def callback_imprimir_datos(data):
    # Imprime los datos actualizados
    print(f"Datos en tiempo real actualizados: {data}")

if __name__ == "__main__":
    # Crea una instancia de RealTimeDataManager y un EventManager
    real_time_data_manager = RealTimeDataManager()
    # Suscribe el callback a la actualización de datos
    real_time_data_manager.event_manager.subscribe("datos_actualizados", callback_imprimir_datos)

    # Crea un hilo para ejecutar la generación de los datos
    update_thread = threading.Thread(target=real_time_data_manager.start_real_time_updates)
    
    # Configura el hilo como demonio 
    # Esto es para que el programa se cierre al ingresar Ctrl + C
    update_thread.daemon = True     

    # Inicia el hilo
    update_thread.start()

    try:
        # Ejecuta el programa hasta que se ingrese Ctrl + C
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\nPrograma terminado.")
