# PUZZLEWORD
# Autora: Rojas Castañeda, Ruth Camila
# Este programa utiliza funcionalidades específicas de la terminal interactiva,
# por lo que no se ejecutará correctamente en Google Colab u otros entornos que carezcan de una
# terminal interactiva. Se recomienda ejecutar este programa en un entorno local de Python.

# NOTA PARA MI:
# Añadir funcionalidades
# - Que se muestres los aciertos y erores del jugador al final con los resultados

import itertools # Se utilizará para realizar las permutaciones
import os # Se utilizará para realizar operaciones relacionadas al sistema operativo
import random # Se utilizará para randomizar las opciones elegidas mostradas al jugador
import time # Se utilizará para dormir la pantalla tras el mensaje de error por tipo de input inválido
import sys 

def centrar_texto_en_pantalla(texto):
    espacios_en_blanco = int((os.get_terminal_size().columns - len(texto)) / 2)
    print(' ' * espacios_en_blanco + texto)

def imprimir_nombre_del_juego(): # Función que muestra el nombre del juego
    centrar_texto_en_pantalla("-------------------")
    centrar_texto_en_pantalla("|                 |")
    centrar_texto_en_pantalla("|   PUZZLEWORD    |")
    centrar_texto_en_pantalla("|                 |")
    centrar_texto_en_pantalla("-------------------")

def juego_con_palabras(): # Función principal 

    while True: 
        os.system('cls' if os.name == 'nt' else 'clear')  # Se limpia la consola

        # [PRIMERA PARTE] ----------------------------------------------------------------------------------------------
        # Esta parte será para que el game hosting ingrese los conjuntos de palabras y las respuestas correctas previas.

        while True: # Input consistenciado
            try: # Se solicita el número de conjuntos que se ingresarán
                imprimir_nombre_del_juego() 
                n = int(input("\nIngrese la cantidad de conjuntos de palabras: "))
                break  # Si se ingresa un número entero válido, salimos del bucle
            except ValueError: # Si se ingresa otro tipo de dato...
                print("Debe ingresar un número entero.") # Se muestra el mensaje de error
                time.sleep(1) # Se duerme la pantalla por un momento para que el usuario lea el mensaje
                os.system('cls' if os.name == 'nt' else 'clear')  # Se limpia la consola para resolicitar nuevamente

        conjuntos = [] # Se inicializa la lista vacía llamada "conjuntos"
        respuestas_correctas = [] # Se inicializa la lista vacía llamada "respuestas_correctas"

        for i in range(n): # Se solicitan las palabras de cada conjunto de los "n" conjuntos
            print(f"\n[CONJUNTO {i+1}]")
            # Se splitea el input por espacios y se guarda en la lista "conjunto" 
            conjunto = input(f"Ingrese las palabras a mezclar separadas por espacios: ").split() 
            # Ahora tendremos una lista de listas
            conjuntos.append(conjunto) # Se añade la lista "conjunto" como elemento de la lista "conjuntos"

        os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola

        for i, conjunto in enumerate(conjuntos):
            # Se establece las respuestas correctas para cada lista "conjunto" de la lista "conjuntos"
            os.system('cls' if os.name == 'nt' else 'clear') # Se limpia la consola
            imprimir_nombre_del_juego()
            print(f"\n¡ESTABLECE LAS RESPUESTAS CORRECTAS!") 
            # Se permutan los elementos (palabras) de cada lista "conjunto"
            # (que a su vez son elementos de la lista mayor "conjuntos")
            permutaciones = list(itertools.permutations(conjunto)) # Se guarda la lista de permutaciones en "permutaciones"
            print(f"\n>> [CONJUNTO {i + 1}]: {conjunto}") # Se imprime el número de lista "conjunto" y sus elementos
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

        # [SEGUNDA PARTE] ----------------------------------------------------------------------------
        # Esta parte será para que el jugador juegue y vea sus resultados.

        os.system('cls' if os.name == 'nt' else 'clear')  # Se limpia la consola

        aciertos = 0 # Se inicializa el número de aciertos en 0

        for i, conjunto in enumerate(conjuntos): # Para cada lista "conjunto" de los n conjuntos
            os.system('cls' if os.name == 'nt' else 'clear')  # Se limpia la consola
            imprimir_nombre_del_juego()
            print(f"\n¡EL JUEGO HA COMENZADO!")
            print(f"\nIngresa las permutaciones correctas separadas por comas. Ejemplo: 1,3,5")
            # Se guarda en la lista "respuesta_correcta" el elemento de índice [i] (lista) de la lista de "respuestas_correctas"
            # por ejemplo (la, paloma, vuela)
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
                print("\n   ¡Correcto!") # Se imprimirá correcto
                time.sleep(2)
                aciertos += 1 # Y se sumará un acierto
            else:
                print("\n   Incorrecto :(") # De lo contrario, se imprimirá desacierto y no se sumará nada
                time.sleep(2)

        os.system('cls' if os.name == 'nt' else 'clear')  # Se limpia la consola

        imprimir_nombre_del_juego()

        print("\n")
        centrar_texto_en_pantalla("RESULTADOS") # Se imprimen los resultados
        print("\n")
        centrar_texto_en_pantalla(f"Puntuación final: {aciertos}/{n}") # Se imprime la puntuación final
        
        if aciertos < n / 2: # Si se acertó menos de la mitad del total de preguntas (número de conjuntos)
            centrar_texto_en_pantalla("A seguir estudiando!")
            print("\n")
        elif aciertos == n / 2: # Si se acertó la mitad del total de preguntas (número de conjuntos)
            centrar_texto_en_pantalla("¡Casi lo logras!")
            print("\n")
        elif aciertos > n / 2 and aciertos < n: # Si se acertó más de la mitad del total de preguntas (número de conjuntos)
            centrar_texto_en_pantalla("¡Bien hecho!")
            print("\n")
        elif aciertos == n: # Si se acertaron todas las preguntas (número de conjuntos)
            centrar_texto_en_pantalla("¡Excelente!")
            print("\n")

        while True: # Se le pregunta al jugador si desea volver a jugar o salir
            eleccion = input("\n¿Desea volver a jugar? (Sí/No): ").strip().lower()
            if eleccion == "si" or eleccion == "sí":
                break # El jugador quiere volver a jugar, se sale del bucle
            elif eleccion == "no":
                print("\nSaliendo del programa...")
                time.sleep(1) # Pausa por un segundo antes de salir
                sys.exit(0) # Salir del programa
            else:
                print("\nOpción inválida. Por favor, ingrese 'Sí' o 'No'.")

if __name__ == "__main__": # Lanza el main
    juego_con_palabras()
