# Simulador de datos en tiempo real

Este programa en Python simula la generación de datos en tiempo real y notifica a los suscriptores cuando los datos están actualizados. Está conformado por lo siguiente tres archivos:

## datamanager.py

### Clase `RealTimeDataManager`:

- **Constructor `__init__`:**
  - Inicia el objeto llamado `RealTimeDataManager` con unos datos (iniciales) de temperatura y humedad.
  - Se crea una instancia de `EventManager` con el nombre de `self.event_manager`.

- **Método `start_real_time_updates`:**
  - Crea un bucle infinito que espera 3 segundos y luego genera datos utilizando `generate_real_time_data` y además notifica a los suscriptores utilizando `self.event_manager.notify`.

- **Método `generate_real_time_data`:**
  - Modifica los valores de temperatura y humedad aleatoriamente para simular los cambios en los datos.

## eventos.py

### Clase `EventManager`:

- **Constructor `__init__`:**
  - Inicia el objeto `EventManager` con un diccionario que almacena los eventos y los suscriptores de los mismos.

- **Método `subscribe`:**
  - Un suscriptor puede registrarse para un evento. Si el evento no existe, se crea una lista vacía.

- **Método `unsubscribe`:**
  - Un suscriptor puede anular su suscripción a un evento.

- **Método `notify`:**
  - Notifica a todos los suscriptores registrados para un evento específico utilizando sus callbacks con los datos indicados.

## simulacion.py

- **Función `callback_imprimir_datos`:**
  - Una función que imprime los datos en tiempo real (actualizados).

- **Código principal:**
  - Se crea una instancia de `RealTimeDataManager`.
  - Se suscribe la función `callback_imprimir_datos` al evento "datos_actualizados".
  - Se crea un hilo para ejecutar el método `start_real_time_updates`.
  - Se establece el hilo como demonio. Esto es para cerrar el programa completamente al ingresar `Ctrl + C`.
  - Se inicia el hilo.
  - El bucle infinito se usa para mantener el programa en ejecución hasta que se recibe una interrupción.
  - Se maneja la interrupción y se imprime un mensaje de cierre.

### Bloque `if __name__ == "__main__":`

Hace que la función `main` se ejecute cuando el script se ejecuta directamente y no cuando es importado como un módulo en otro script.

---

**Instrucciones de uso:**

1. Se debe ejecutar `simulacion.py` para iniciar la simulación.
2. El programa va a generar los datos en tiempo real y notificará a los suscriptores.

## Ejemplo de Salida del Programa

Al ejecutar el archivo `simulacion.py` se produce una salida similar a la siguiente:

Datos en tiempo real actualizados: {'temperatura': 24.8144788325153, 'humedad': 59.22656452432036}  
Datos en tiempo real actualizados: {'temperatura': 25.695321492733867, 'humedad': 61.59471649132475}  
Datos en tiempo real actualizados: {'temperatura': 24.85648409627055, 'humedad': 60.57975982047561}  


## Explicación de los resultados

- Cada línea representa una actualización de datos en tiempo real.
- Los valores de temperatura y humedad se generan de forma aleatoria y se modifican en cada actualización.
- Los datos actualizados se imprimen en la siguiente forma: `{'temperatura': valor, 'humedad': valor}`.
- La simulación continua hasta que se ingresa la interrupción `Ctrl + C`.

**Nota:** Los valores pueden variar en cada ejecución porque son aleatorios.
