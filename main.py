import random

# Generar un número aleatorio entre 1 y 100
numero_secreto = random.randint(1, 100)

# Bucle para solicitar al jugador/ora que adivine el número
while True:
    # Obtener la entrada del jugador/ora
    intento = input("Adivina el número (entre 1 y 100): ")

    # Verificar si la entrada es un número válido
    if intento.isdigit():
        intento = int(intento)
        # Comparar el intento con el número secreto
        if intento == numero_secreto:
            print("¡Felicidades! ¡Has adivinado el número!")
            break  # Salir del bucle si jugador/ora adivina el número
        elif intento < numero_secreto:
            print("El número secreto es mayor.")
        else:
            print("El número secreto es menor.")
    else:
        print("Por favor, ingresa un número entero válido.")
