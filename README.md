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

# Calculadora

Este programa en Python es una calculadora sencilla con operaciones básicas. Permite al usuario realizar operaciones como suma, resta, multiplicación y división. Está conformado solo por un archivo.

## calculadora.py

### Función `get_user_input`:

Esta función obtiene la entrada del usuario. Utiliza un bloque `try-except` para manejar errores en caso de que el usuario ingrese algo inválido (que no sea un número). Pide al usuario que ingrese dos números y la operación que desea realizar (+, -, *, /). También, permite ingresar 'exit' para salir. Si hay un error al intentar convertir la entrada a un `float` se imprime un mensaje de error y se solicita la entrada nuevamente.

### Función `ejecutar_operacion`:

Recibe como argumentos la entrada del usuario y una función de callback. Se llama a la función de callback con los dos números ingresados por el usuario y se muestra el resultado.

### Función `main`:

Se definen funciones lambda para ejecutar las operaciones de suma, resta, multiplicación y división. Se crea un diccionario llamado `operations` que relaciona los operadores (+, -, *, /) a las funciones lambda. Utiliza un bucle infinito (`while True`) para pedir la entrada del usuario y realizar las operaciones. Dentro del bucle, se obtiene la entrada del usuario utilizando `get_user_input`. Si el operador ingresado es 'exit' se imprime un mensaje y sale del bucle. Si el operador está en el diccionario `operations` se llama a la función `ejecutar_operacion` con la entrada del usuario y la función lambda que corresponda. Si el operador no está en el diccionario, imprime el mensaje de "Operación inválida". Se previene que el usuario intente usar la operación de división entre cero, en ese caso se imprime un mensaje de "Error: División entre cero".

### Bloque `if __name__ == "__main__":`

Hace que la función `main` se ejecute cuando el script se ejecuta directamente y no cuando es importado como un módulo en otro script.

---

**Instrucciones de uso:**

1. Se debe ejecutar `calculadora.py` para iniciar la calculadora.
2. El programa va a solicitar dos números y la operación que se desea realizar.

## Ejemplo de Salida del Programa

Al ejecutar el archivo `calculadora.py` se produce una salida similar a la siguiente:

Ingrese un numero: 10  
Ingrese otro numero: 5  
Elija una operacion (+, -, *, /) o escriba 'exit' para salir: +  
Calculando...  
Resultado: 15.0  

Ingrese un numero: 8  
Ingrese otro numero: 2  
Elija una operacion (+, -, *, /) o escriba 'exit' para salir: *  
Calculando...  
Resultado: 16.0  

Ingrese un numero: 12  
Ingrese otro numero: 0  
Elija una operacion (+, -, *, /) o escriba 'exit' para salir: /  
Calculando...  
Resultado: Error: División entre cero  

Ingrese un numero: abc  
Input invalido. Por favor ingrese numeros.  

Ingrese un numero: 4  
Ingrese otro numero: 3  
Elija una operacion (+, -, *, /) o escriba 'exit' para salir: -  
Calculando...  
Resultado: 1.0  

Ingrese un numero: 3  
Ingrese otro numero: 4  
Elija una operacion (+, -, *, /) o escriba 'exit' para salir: exit  
Salir.  

## Explicación de los resultados

- **Suma (Operación `+`):** El usuario ingresó 10 y 5 y eligió la suma. El resultado es 15.
- **Multiplicación (Operación `*`):** El usuario ingresó 8 y 2 y eligió la multiplicación. El resultado es 16.
- **División entre Cero (`Error: División entre cero`):** El usuario intentó dividir 12 entre 0, por lo cual se muestra un mensaje de error.
- **Valor inválido (`Operación inválida`):** El usuario intentó ingresar algo que no es un número, por lo cual se imprime un mensaje de error.
- **Resta (Operación `-`):** El usuario ingresó 4 y 3 y eligió la resta. El resultado es 1.
- **Salir (`exit`):** El usuario ingresó "exit" y se termina el programa.
