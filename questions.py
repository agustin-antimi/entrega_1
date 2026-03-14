import random

### Definimos las categorias posibles
categorias = {
    "programacion": [
        "python", "programa", "variable", "funcion", 
        "bucle", "cadena", "entero", "lista"
    ],
    "comida": [
        "fideos", "carne", "tarta", "pizza", "hamburguesa"
    ],
    "deportes": [
        "futbol", "basquet", "tenis", "hockey", "handball"
    ]
}

print("¡Bienvenido al Ahorcado!\n")

while True:
    # Mostramos solo los nombres de las categorias
    print(f"Categorias posibles: {', '.join(categorias)}")
    categoria_elegida = input("Ingrese la categoria a elegir: ").lower()
    if categoria_elegida in categorias:
        break
    print("La categoria ingresada no existe. Por favor, intente de nuevo.\n")

# Accedemos a las palabras de la lista seleccionada por el usuario
word = random.choice(categorias[categoria_elegida])
guessed = []
attempts = 6

print(f"\nCategoria seleccionada: {categoria_elegida}")
print()

while attempts > 0:
    # Mostrar progreso: letras adivinadas y guiones para las que faltan
    progress = ""
    for letter in word:
        if letter in guessed:
            progress += letter + " "
        else:
            progress += "_ "
    print(progress)

    # Verificar si el jugador ya adivinó la palabra completa
    if "_" not in progress:
        print(f"¡Ganaste!, tu puntaje fue de {attempts}")
        break
    print(f"Intentos restantes: {attempts}")
    print(f"Letras usadas: {', '.join(guessed)}")

    ### Utilizamos un bucle while para verificar la entrada del ususario
    while True:
        letter = input("Ingresá una letra: ").lower()

        # Verificamos que sea 1 solo caracter y que sea una letra
        if len(letter) == 1 and letter.isalpha():
            break # Romepe el bucle si la entrada es valida  
        
        print("Entrada no válida")

    if letter in guessed:
        print("Ya usaste esa letra.")
    elif letter in word:
        guessed.append(letter)
        print("¡Bien! Esa letra está en la palabra.")
    else:
        guessed.append(letter)
        attempts -= 1
        print("Esa letra no está en la palabra.")

    print()
else:
    print(f"¡Perdiste! La palabra era: {word}, tu puntaje fue de: 0")
