import random

### Definimos las categorias posibles
categorias = {
    "programacion": [
        "python",
        "programa",
        "variable",
        "funcion",
        "bucle",
        "cadena",
        "entero",
        "lista",
    ],
    "comida": ["fideos", "carne", "tarta", "pizza", "hamburguesa"],
    "deportes": ["futbol", "basquet", "tenis", "hockey", "handball"],
}

print("¡Bienvenido al Ahorcado!\n")
print("Jugaremos 3 rondas.\n")

# CAMBIO 1: Bucle de rondas. Movi la eleccion de categoria aca adentro.
for ronda in range(1, 4):
    print(f"--- INICIANDO RONDA {ronda} ---")

    while True:
        # Mostramos solo los nombres de las categorias
        print(f"Categorias posibles: {', '.join(categorias)}")
        categoria_elegida = input("Ingrese la categoria a elegir: ").lower()

        # Verificamos que la categoria exista y que todavia tenga palabras
        if categoria_elegida in categorias and len(categorias[categoria_elegida]) > 0:
            break

        print("Categoria no valida o ya no tiene palabras. Intente de nuevo.\n")

    # Elegimos 1 palabra con random.sample y la borramos de la lista
    word = random.sample(categorias[categoria_elegida], 1)[0]
    categorias[categoria_elegida].remove(word)

    print(f"\nCategoria seleccionada: {categoria_elegida}")
    print()

    guessed = []
    attempts = 6

    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)

        # Verificar si el jugador ya adivino la palabra completa
        if "_" not in progress:
            print(f"!Ganaste!, tu puntaje fue de {attempts}")
            break

        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")

        # Utilizamos un bucle while para verificar la entrada del usuario
        while True:
            letter = input("Ingresa una letra: ").lower()

            # Verificamos que sea 1 solo caracter y que sea una letra
            if len(letter) == 1 and letter.isalpha():
                break  # Rompe el bucle si la entrada es valida

            print("Entrada no valida")

        if letter in guessed:
            print("Ya usaste esa letra.")
        elif letter in word:
            guessed.append(letter)
            print("!Bien! Esa letra esta en la palabra.")
        else:
            guessed.append(letter)
            attempts -= 1
            print("Esa letra no esta en la palabra.")

        print()
    else:
        print(f"!Perdiste! La palabra era: {word}, tu puntaje fue de: 0")
