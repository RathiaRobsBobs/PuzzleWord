# PUZZLEWORD
# Autora: Rojas Castañeda, Ruth Camila
# Este programa utiliza funcionalidades específicas de la terminal interactiva,
# por lo que no se ejecutará correctamente en Google Colab u otros entornos que carezcan de una
# terminal interactiva. Se recomienda ejecutar este programa en un entorno local de Python.

import itertools # Se utilizará para realizar las permutaciones
import os # Se utilizará para realizar operaciones relacionadas al sistema operativo
import random # Se utilizará para randomizar las opciones elegidas mostradas al jugador
import time # Se utilizará para dormir la pantalla tras el mensaje de error por tipo de input inválido
import sys # salir del programa usando sys.exit(0) en el caso en que el usuario lo desee

def centrar_texto_en_pantalla(texto):
    espacios_en_blanco = int((os.get_terminal_size().columns - len(texto)) / 2)
    print(' ' * espacios_en_blanco + texto)

def imprimir_nombre_del_juego(): # Función que muestra el nombre del juego
    centrar_texto_en_pantalla(" ▄▄▄ ▄  ▄ ▄▄▄▄ ▄▄▄▄ ▄   ▄▄▄ ▄   ▄ ▄▄▄ ▄▄▄ ▄▄▄  ")
    centrar_texto_en_pantalla(" █▄█ █  █  ▄▀   ▄▀  █   █─  █ ▄ █ █ █ █▄█ █  █ ")
    centrar_texto_en_pantalla(" █   █▄▄█ █▄▄▄ █▄▄▄ █▄▄ █▄▄ █▄█▄█ █▄█ █▀▄ █▄▄▀ ")

def menu_principal(): # Muestra el menú principal del juego

    conjuntos = [] # Se inicializa la lista vacía llamada "conjuntos"
    respuestas_correctas = [] # Se inicializa la lista vacía llamada "respuestas_correctas"

    while True:

        os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

        # Zona de impresión
        imprimir_nombre_del_juego()
        print("\n")
        centrar_texto_en_pantalla("╭─────────────────╮")
        centrar_texto_en_pantalla("|  MENU PRINCIPAL |")
        centrar_texto_en_pantalla("╰─────────────────╯")
        print("\n")
        centrar_texto_en_pantalla("     ╭─────╮             ╭─────╮           ╭─────╮      ")
        centrar_texto_en_pantalla("     |  1  |             |  2  |           |  3  |      ")
        centrar_texto_en_pantalla("╭────╯     ╰───────╮─────╯     ╰─────╮─────╯     ╰─────╮")
        centrar_texto_en_pantalla("|              ╭───╯             ╭───╯                 |")
        centrar_texto_en_pantalla("|    Hosting   |       Jugador   |         Salir       |")
        centrar_texto_en_pantalla("|              ╰───╮             ╰───╮                 |")
        centrar_texto_en_pantalla("|    ╭─────╮       ╰─────╮     ╭─────╯     ╭─────╮     |")
        centrar_texto_en_pantalla("|    |     |       |     |     |     |     |     |     |")
        centrar_texto_en_pantalla("╰────╯     ╰───────╯     ╰─────╯     ╰─────╯     ╰─────╯")

        # Se le solicita al usuario el número correspondiente a su rol
        while True: # Input consistenciado
            try:
                eleccion = input("\nIngrese su rol (1, 2 o 3) >> ").strip()
                break  # Si se ingresa un número entero válido, salimos del bucle
            except ValueError: # Si se ingresa otro tipo de dato...
                print("\nDebe ingresar un número entero.") # Se muestra el mensaje de error
                time.sleep(1) # Se duerme la pantalla por un momento para que el usuario lea el mensaje
                os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola para resolicitar nuevamente
        
        if eleccion == "1": # Si es hosting, le permite el registro de conjuntos y establecimiento de rptas correctas
            conjuntos, respuestas_correctas = realizar_hosting(conjuntos, respuestas_correctas)
        elif eleccion == "2": # Si es jugador le permite jugar con los conjuntos registrados
            jugar_como_jugador(conjuntos, respuestas_correctas)
        elif eleccion == "3": # Sino, se saldrá del programa
            print("\nSaliendo del programa...") # Mensaje de cierre
            time.sleep(1) # Duermo la pantalla por un segundo para que el usuario lea el mensaje de cierre
            sys.exit(0)

def realizar_hosting(conjuntos, respuestas_correctas): # Función para el hosting

    while True:

        os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

        # Zona de impresión
        imprimir_nombre_del_juego() 
        print("\n")
        centrar_texto_en_pantalla("╭──────────────────────────────────────────────╮")
        centrar_texto_en_pantalla("|    ESTABLEZCAMOS LAS RESPUESTAS CORRECTAS    |")
        centrar_texto_en_pantalla("╰──────────────────────────────────────────────╯")
        print("\n")

        # Se le solicita al hosting ingresar las palabras de un primer conjunto y se splitean por espacios
        conjunto = input("\nIngrese un conjuntos de palabras separadas por espacios: ").split()
        conjuntos.append(conjunto) # Se añade la lista "conjunto" como elemento de la lista "conjuntos"

        os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

        # Zona de impresión
        imprimir_nombre_del_juego() 
        print("\n")
        centrar_texto_en_pantalla("╭──────────────────────────────────────────────╮")
        centrar_texto_en_pantalla("|    ESTABLEZCAMOS LAS RESPUESTAS CORRECTAS    |")
        centrar_texto_en_pantalla("╰──────────────────────────────────────────────╯")
        print("\n")

        # Se establecen las respuestas correctas para el conjunto de palabras ingresado
        permutaciones = list(itertools.permutations(conjunto)) # Se guarda la lista de permutaciones en "permutaciones"
        print(f"\n>> [CONJUNTO {len(conjuntos)}]: {conjunto}") # Se imprimen los elementos del conjunto
        print("\n   Estas son todas las permutaciones posibles con las palabras del conjunto.")
        print("   Por favor, seleccione las permutaciones correctas separadas por comas:\n")
        # Se recorre la lista "permutaciones" y se obtiene su índice y elemento 
        for idx, permutacion in enumerate(permutaciones):
            oracion = list(permutacion) # El elemento de la lista "permutaciones" se guarda en la lista "oracion"
            print(f"   [{idx + 1}]: {' '.join(oracion)}") # Se imprime la lista "oracion" concatenada por espacios
        # Se splitea el input por comas y se guarda en la lista "respuestas"
        respuestas = input("\n   >> RESPUESTA (Ejemplo: 1,3,5): ").split(',')
        # Se convierte en entero un elemento (número ingresado como cadena de texto) de la lista "respuestas"
        # y se le resta 1 para llegar al índice, y se repite el procedimiento para toda la lista "respuestas"
        respuestas = [int(r) - 1 for r in respuestas]
        # "respuestas" es una comprensión de lista que itera a través de los índices r en la lista "respuestas" 
        # Para cada índice r, selecciona la permutación de palabras correspondiente de la lista "permutaciones"
        # Se añade a la lista "respuestas_correctas"
        respuestas_correctas.append([permutaciones[r] for r in respuestas])

        # Se le pregunta al hosting si quiere añadir otro conjunto, para repetir el proceso
        continuar = input("\n¿Desea añadir otro conjunto? (Sí/No): ").strip().lower()
        if continuar != "si" and continuar != "sí": 
            return conjuntos, respuestas_correctas

def jugar_como_jugador(conjuntos, respuestas_correctas): # Función para el jugador

    if not conjuntos: # Si no hay conjuntos registrados, se informa ello
        print("\nNo se han registrado conjuntos para jugar. Regrese al menú principal y realice el hosting primero.")
        input("\nPresione Enter para continuar...")
        menu_principal()

    aciertos = 0 # Se inicializa el número de aciertos en 0

    for i, conjunto in enumerate(conjuntos): # Para cada lista "conjunto" de los n conjuntos registrados

        os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

        # Zona de impresión
        imprimir_nombre_del_juego() 
        print("\n")
        centrar_texto_en_pantalla("╭──────────────────────────────────────────────╮")
        centrar_texto_en_pantalla("|           ¡EL JUEGO HA COMENZADO!            |")
        centrar_texto_en_pantalla("╰──────────────────────────────────────────────╯")
        print("\n")

        # Se guarda en la lista temporal "respuesta_correcta" el elemento de índice [i] (lista) de la lista de 
        # "respuestas_correctas" por ejemplo (la, paloma, vuela)
        respuesta_correcta = respuestas_correctas[i] 
        # Luego, esa lista "respuesta_correcta" se guarda en una lista "opciones_correctas"
        opciones_correctas = respuesta_correcta 
        # Se guarda en la lista "permutaciones_posibles", todas las permutaciones (minilistas) de la minilista "conjunto"
        permutaciones_posibles = list(itertools.permutations(conjunto))
        # Se guarda en la lista "opciones_incorrectas" todas las permutaciones (minilistas) de la minilista "permutaciones_posibles" 
        # (que es como la inicial "permutaciones")  que no estén en la lista "respuesta_correcta" (que es el elemento de la lista
        # "respuestas_correctas" de índice [i], es decir, para el conjunto de índica [i])
        opciones_incorrectas = [p for p in permutaciones_posibles if p not in respuesta_correcta]
        # Luego, se guarda en la lista "opciones" la lista "opciones_correctas" + un número random >=5 de la lista "opciones_incorrectas"
        opciones = opciones_correctas + random.sample(opciones_incorrectas, min(5, len(opciones_incorrectas)))
        
        # Se shufflea los elementos (las permutaciones) de la lista "opciones"
        random.shuffle(opciones)

        print(f"\n\n   PREGUNTA [{i + 1}]\n")

        for idx, opcion in enumerate(opciones): # Para cada elemento (minilista) de la lista "opciones"
            oracion = list(opcion) # Se guarda en una lista "oracion"
            print(f"   {idx + 1}: {' '.join(oracion)}") # Se concatenan los elementos de esa lista con espacio en blanco

        # Se splitea el input por comas
        respuestas_usuario = input("\n   >> RESPUESTA: ").split(',')
        # Se convierte en entero un elemento (número ingresado como cadena de texto) de la lista "respuestas_usuario"
        # y se le resta 1 para llegar al índice, y se repite el procedimiento para toda la lista "respuestas_usuario"
        respuestas_usuario = [int(r) - 1 for r in respuestas_usuario]
        # Si el elemento r de la lista "opciones" está en la lista "opciones correctas" (y este proceso se repetirá 
        # para todos los elementos de la lista "respuestas_usuario")
        if all([opciones[r] in opciones_correctas for r in respuestas_usuario]):
            print("\n   ¡Correcto!") # Se imprimirá "¡Correcto!"
            time.sleep(2)
            aciertos += 1 # Y se sumará un acierto
        else:
            print("\n   Incorrecto :(") # De lo contrario, se imprimirá "Incorrecto :(" y no se sumará nada
            time.sleep(2)

    os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

    # Zona de impresión
    imprimir_nombre_del_juego()
    print("\n")
    centrar_texto_en_pantalla("╭─────────────────╮")
    centrar_texto_en_pantalla("|   RESULTADOS    |")
    centrar_texto_en_pantalla("╰─────────────────╯")
    print("\n")
    centrar_texto_en_pantalla(f"Puntuación final: {aciertos}/{len(conjuntos)}") # Se imprime la puntuación final

    if aciertos < len(conjuntos) / 2: # Si se acertó menos de la mitad del total de preguntas (número de conjuntos)
        centrar_texto_en_pantalla("A seguir estudiando!")
        print("\n")
    elif aciertos == len(conjuntos) / 2: # Si se acertó la mitad del total de preguntas (número de conjuntos)
        centrar_texto_en_pantalla("¡Casi lo logras!")
        print("\n")
    elif aciertos > len(conjuntos) / 2 and aciertos < len(conjuntos): # Si se acertó más de la mitad del total de preguntas (número de conjuntos)
        centrar_texto_en_pantalla("¡Bien hecho!")
        print("\n")
    elif aciertos == len(conjuntos): # Si se acertaron todas las preguntas (número de conjuntos)
        centrar_texto_en_pantalla("¡Excelente!")
        print("\n")

    while True: # Se le pregunta al jugador si desea volver a jugar o salir
        eleccion = input("\n¿Desea volver a jugar? (Sí/No): ").strip().lower()
        if eleccion == "si" or eleccion == "sí":
            print("\n¡A intentarlo de nuevo entonces!...")
            time.sleep(1)
            jugar_como_jugador(conjuntos, respuestas_correctas)
        elif eleccion == "no":
            menu_principal() # El jugador quiere no volver a jugar, se sale del bucle
        else:
            print("\nOpción inválida. Por favor, ingrese 'Sí' o 'No'.")

if __name__ == "__main__":
    menu_principal()