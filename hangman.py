from words import palabras
import random

print("Bienvenido al juego del ahorcado")

def get_valid_palabra(palabras):
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    
    return palabra

mi_palabra = get_valid_palabra(palabras)
espacios_vacios = ' _ ' * len(mi_palabra)
print(espacios_vacios)

    