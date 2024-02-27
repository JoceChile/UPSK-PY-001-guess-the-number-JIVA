import random
from colorama import Fore, Style
import time

def generate_secret_number():
    return random.randint(1, 100)

def get_player_guess():
    while True:
        try:
            guess = int(input((Fore.CYAN + "Adivina el número secreto (entre 1 y 100): " + Style.RESET_ALL)))
            if guess < 1 or guess > 100:
                raise ValueError
            return guess
        except ValueError:
            print(Fore.RED + "Por favor, ingresa un número válido entre 1 y 100." + Style.RESET_ALL)

def player_turn(secret_number, player_name):
    while True:
        guess = get_player_guess()

        time.sleep(1)  # Espera 1 segundo antes de mostrar la respuesta
        print()  # Espacio en blanco
        if guess == secret_number:
            print(Fore.GREEN + f"¡Felicidades, {player_name}! ¡Has adivinado el número secreto!" + Style.RESET_ALL)
            print()  # Espacio en blanco
            return True
        elif guess < secret_number:
            print(Fore.YELLOW + "El número secreto es MAYOR que tu suposición." + Style.RESET_ALL)
        else:
            print(Fore.YELLOW + "El número secreto es MENOR que tu suposición." + Style.RESET_ALL)



def get_computer_guess():
    return random.randint(1, 100)

def computer_turn(secret_number):
    guess = get_computer_guess()
    print((Fore.WHITE + "El ordenador hace una suposición:" + Style.RESET_ALL), guess)

    time.sleep(1)  # Espera 1 segundo antes de mostrar la respuesta
    print()  # Espacio en blanco
    if guess == secret_number:
        print(Fore.GREEN + "El ordenador ha adivinado el número secreto." + Style.RESET_ALL)
        return True
    elif guess < secret_number:
        print(Fore.WHITE + "El número secreto es MAYOR que la suposición del ordenador." + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "El número secreto es MENOR que la suposición del ordenador." + Style.RESET_ALL)
    time.sleep(1)  # Espera 1 segundo antes de continuar
    print()  # Espacio en blanco
    return False

def get_player_name():
    return input("Por favor, ingresa tu nombre: ")

def play_game():
    player_name = get_player_name()
    secret_number = generate_secret_number()
    print()  # Espacio en blanco
    print(Fore.CYAN + f"Bienvenid@ {player_name}!" + Style.RESET_ALL)
    print()  # Espacio en blanco
    while True:
        if player_turn(secret_number, player_name):
            break
        if computer_turn(secret_number):
            break

if __name__ == "__main__":
    play_game()
