#from colorama import Fore, Back, Style, init
from words import palabras
import random
import string
#init()

print("Bienvenido al juego del ahorcado")

def get_valid_palabra(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra.upper()

def hangman():
    mi_palabra = get_valid_palabra(palabras)
    palabra_separada = list(mi_palabra)
    alphabet = set(string.ascii_uppercase)
    used_letter = set()
    lives = 6

    while len(palabra_separada) > 0 and lives > 0:
        print("Intentos",lives)
        user_letter = input('Introduce una letra: ').upper()
        if user_letter in alphabet - used_letter:
            used_letter.add(user_letter)
            if user_letter in palabra_separada:        
                palabra_separada.remove(user_letter)
            else:
                lives = lives - 1
                print("Menos un intento")
        elif user_letter in used_letter:
            print("Repetiste una letra")
        else:
            print("Caracter invalido")
    
    if(lives > 0):
        print("Ganaste")
    else:
        print(f"Tu palabra era {mi_palabra}\n","Perdistes")

hangman()