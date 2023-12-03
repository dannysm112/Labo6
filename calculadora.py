# Obtener la entrada del usuario y manejar errores
def get_user_input():
    try:
        num1 = float(input("Ingrese un numero: "))
        num2 = float(input("Ingrese otro numero: "))
        operation = input("Elija una operacion (+, -, *, /) o escriba 'exit' para salir: ")
        return num1, num2, operation
    except ValueError:
        print("Input invalido. Por favor ingrese numeros.")
        # En caso de error pide la entrada de nuevo
        return get_user_input()

# Ejecutar la operación indicada por el usuario utilizando un callback
def ejecutar_operacion(user_input, callback):
    num1, num2, operation = user_input
    result = callback(num1, num2)
    print("Resultado:", result)

def main():
    # Funciones lambda para cada operación
    suma = lambda x, y: x + y
    resta = lambda x, y: x - y
    multiplicacion = lambda x, y: x * y
    # Error de división entre cero
    division = lambda x, y: x / y if y != 0 else "Error: División entre cero"

    # Diccionario de operadores a funciones lambda
    operations = {
        '+': suma,
        '-': resta,
        '*': multiplicacion,
        '/': division
    }

    # Bucle que pide la entrada del usuario y realiza las operaciones
    while True:
        user_input = get_user_input()

        # Verifica si el usuario ya quiere salir
        if user_input[2].lower() == 'exit':
            print("Salir.")
            break

        print("\nCalculando...")

        # Verifica si el operador está en el diccionario y lo ejecuta
        if user_input[2] in operations:
            ejecutar_operacion(user_input, operations[user_input[2]])
        else:
            #En caso de error imprime un mensaje de "Operación inválida"
            print("Operacion invalida. Seleccione (+, -, *, /) o escriba 'exit' para salir.")

if __name__ == "__main__":
    main()
