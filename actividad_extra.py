# Creamos un dict vacio para agregar equipos luego
equipos = dict()

# Funcion que imprime la tabla de los equipos por posiciones
def tabla():
    # primero ordenamos el diccionario de equipos por puntos
    posiciones_ordenadas = dict(sorted(equipos.items(), key=lambda item: item[1]))
    
    # luego imprimos la tabla
    print("---TABLA DE POSICIONES---\n   EQUIPO   PUNTOS")
    for euqipo, puntos in posiciones_ordenadas.items():
        print(f"\n   {euqipo}   {puntos}")

# Funcion que registra partidos y agrega los puntos a los euqipos    
def registrar_partido():
    print("\n--- REGISTRO DE PARTIDO ---")
    equipo1 = input("Ingrese el nombre del equipo local: ")
    equipo2 = input("Ingrese el nombre del equipo visitante: ")

    # Validacion: si alguno no esta en la tabla, salimos de la funcion
    if (equipo1 not in equipos) or (equipo2 not in equipos):
        print("Error: Uno o ambos equipos no estan registrados.")
        return 

    ## Pedimos los goles y validamos que sean numeros
    # En caso de no serlo volvemos al bucle
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
    return


def eliminar_equipo():
    return

def salir():
    return




## Definimos un dict con los comandos posibles
comandos = {
    "tabla" : tabla(),
    "partido" : registrar_partido(),
    "agregar" : agregar_equipo(),
    "eliminar" : eliminar_equipo(),
    "salir" : salir()
    }


while True:
    ## 1 Mostramos la tabla de comandos \
    print(f"Comandos posibles: {', '.join(comandos).upper()}")
    comando_ingresado = input("Ingrese uno de los comandos porfavor").lower()
    comandos[comando_ingresado]