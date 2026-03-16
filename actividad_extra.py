# Creamos un dict vacio para agregar equipos luego
equipos = dict()

# Funcion que imprime la tabla de los equipos por posiciones
def tabla():
    # Ordenamos el diccionario por puntos de mayor a menor (reverse=True)
    posiciones_ordenadas = dict(sorted(equipos.items(), key=lambda item: item[1], reverse=True))

    # Luego imprimimos la tabla
    print("\n---TABLA DE POSICIONES---\n   EQUIPO   PUNTOS")
    for equipo, puntos in posiciones_ordenadas.items():
        print(f"   {equipo}   {puntos}")
    print() # Espacio extra para prolijidad

# Funcion que registra partidos y agrega los puntos a los equipos
def registrar_partido():
    print("\n--- REGISTRO DE PARTIDO ---")
    equipo1 = input("Ingrese el nombre del equipo local: ").lower()
    equipo2 = input("Ingrese el nombre del equipo visitante: ").lower()

    # Validacion: si alguno no esta en la tabla, salimos de la funcion
    if (equipo1 not in equipos) or (equipo2 not in equipos):
        print("Error: Uno o ambos equipos no estan registrados.")
        return

    # Pedimos los goles y validamos que sean numeros
    # En caso de no serlo volvemos al bucle principal
    try:
        goles1 = int(input(f"Goles de {equipo1}: "))
        goles2 = int(input(f"Goles de {equipo2}: "))
    except ValueError:
        print("Error: Debes ingresar numeros enteros para los goles.")
        return

    # Evaluamos el resultado con match
    match (goles1, goles2):
        case (g1, g2) if g1 > g2:
            equipos[equipo1] += 3
            print(f"Gano {equipo1}. Se sumaron 3 puntos.")
        case (g1, g2) if g1 == g2:
            equipos[equipo1] += 1
            equipos[equipo2] += 1
            print("Empate. Se sumo 1 punto a cada equipo.")
        case (g1, g2) if g1 < g2:
            equipos[equipo2] += 3
            print(f"Gano {equipo2}. Se sumaron 3 puntos.")
        case _:
            print("Datos ingresados incorrectos.")

def agregar_equipo():
    equipo_agregar = input("Por favor ingrese el nombre del equipo a agregar: ").lower()
    if equipo_agregar not in equipos:
        print(f"Agregando el equipo {equipo_agregar} al torneo.")
        equipos[equipo_agregar] = 0
        return
    print("El equipo ingresado ya esta dentro del torneo.")

def eliminar_equipo():
    # Imprimimos los equipos posibles
    if not equipos:
        print("No hay equipos registrados aun.")
        return
        
    print("Listado de equipos:")
    for eq in equipos.keys():
        print(eq)

    # Chequeamos que el equipo ingresado este registrado
    equipo_eliminar = input("Ingrese un equipo a eliminar: ").lower()
    if equipo_eliminar not in equipos:
        print("El equipo ingresado no esta en la tabla.")
        return
    
    # En caso de que el equipo este en la tabla lo eliminamos usando del
    print(f"Eliminando al equipo {equipo_eliminar}.")
    del equipos[equipo_eliminar]

# Definimos un dict con los comandos posibles
comandos = {
    "tabla": lambda: tabla(),
    "partido": lambda: registrar_partido(),
    "agregar": lambda: agregar_equipo(),
    "eliminar": lambda: eliminar_equipo(),
}

while True:
    # Mostramos la tabla de comandos
    print(f"Comandos posibles: {', '.join(comandos).upper()}. En caso de querer cerrar la interfaz ingrese SALIR")
    comando_ingresado = input("Ingrese uno de los comandos por favor: ").lower()

    # Verificamos que el comando ingresado sea correcto
    if comando_ingresado in comandos:
        comandos[comando_ingresado]()
    elif comando_ingresado == "salir":
        print("\nSaliendo de la interfaz...")
        break
    else:
        print(f"Comando ({comando_ingresado}) no reconocido.")

print("\nPosiciones finales del torneo:")
tabla()