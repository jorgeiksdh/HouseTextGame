"""
    *** House Text Game ***

    @author: Jorge Galindo
    @company: Dev.f

    Éste es un juego de texto que te permite entrar en una casa y recorrer sus
    habitaciones y obtener una descripción de cada una de ellas. El jugador
    deberá caminar hasta encontrar la salida; en su recorrido tendrá acceso a
    la descripción de cada cuarto en el que se encuentre.

"""

jugador = [0,0]
puertas = ((-2,3),(0,0))
sala1 = ((-1,1), (0,1), (1,1), (-1,2), (0,2), (1,2), (-1,3),(0,3),(1,3))
muros = ((-2,0),(-1,0),(1,0),(2,0),(-2,1),(2,1),(-2,2),(2,2),(2,3),(-2,4),(-1,4),(0,4),(1,4),(2,4))
flag = 1

def avanzar(a, b):
    """
        Esta función va a cambiar la posición del jugador de acuerdo a las
        instrucciones que le proporcione el usuario

    """
    if a == 1:
        for x in range(b):
            jugador[1] += 1
            posicion = tuple(jugador)
            if posicion in muros:
                jugador[1] -= 1
                print("Has topado con un muro")
                break
            elif posicion == (-2,3):
                print("¡Felicidades! ¡Encontraste la salida!")
                flag = 0
            else:
                continue
    elif a == 2:
        for x in range(b):
            jugador[1] -= 1
            posicion = tuple(jugador)
            if posicion in muros:
                jugador[1] += 1
                print("Has topado con un muro")
                break
            elif posicion == (-2,3):
                print("¡Felicidades! ¡Encontraste la salida!")
                flag = 0
            else:
                continue
    elif a == 3:
        for x in range(b):
            jugador[0] += 1
            posicion = tuple(jugador)
            if posicion in muros:
                jugador[0] -= 1
                print("Has topado con un muro")
                break
            elif posicion == (-2,3):
                print("¡Felicidades! ¡Encontraste la salida!")
                flag = 0
            else:
                continue
    elif a == 4:
        for x in range(b):
            jugador[0] -= 1
            posicion = tuple(jugador)
            if posicion in muros:
                jugador[0] += 1
                print("Has topado con un muro")
                break
            elif posicion == (-2,3):
                print("¡Felicidades! ¡Encontraste la salida!")
                flag = 0
            else:
                continue

def compararPosicion(a, b):
    """
        Esta función va a comparar la posición del jugador con la posición
        de la entrada y la salida de la casa, así como de las puertas de las
        habitaciones.

    """
    posicion = (a, b)
    if posicion == (0,0):
        print("Has regresado a tu punto de partida")

def informacion(a, b):
    """
        Esta función va a proporcionar información de la habitación de acuerdo
        a la posición del jugador.

    """
    posicion = (a, b)
    if posicion in sala1:
        print("Estás parado en la sala principal. Por el momento es una habitación vacía.")
    if posicion == (0,0):
        print("Estás en la puerta principal")

while flag == 1:
    print("")
    print("########################################")
    print("##                                    ##")
    print("##   ** Bienvenido a la Gran Casa **  ##")
    print("##                                    ##")
    print("##   Opciones:                        ##")
    print("##   1 -> Avanzar                     ##")
    print("##   2 -> Información del cuarto      ##")
    print("##   3 -> Debug: posición             ##")
    print("##   4 -> Salir                       ##")
    print("##                                    ##")
    print("########################################")
    print("")

    seleccion = int(input("Introduzca su selección: "))

    if seleccion == 1:
        print("")
        print("########################################")
        print("##                                    ##")
        print("##   Elige a dónde quieres moverte:   ##")
        print("##   1 -> Norte                       ##")
        print("##   2 -> Sur                         ##")
        print("##   3 -> Este                        ##")
        print("##   4 -> Oeste                       ##")
        print("##                                    ##")
        print("########################################")
        print("")
        a = int(input("Introduce tu seleccion: "))

        print("")
        print("########################################")
        print("##                                    ##")
        print("##    Elige cuantos pasos moverte:    ##")
        print("##       (tres pasos por turno)       ##")
        print("##                                    ##")
        print("########################################")
        print("")
        b = int(input("Introduce el número de pasos: "))

        avanzar(a, b)
        a, b = jugador[0], jugador[1]
        compararPosicion(a, b)

    elif seleccion == 2:
        a, b = jugador[0], jugador[1]
        informacion(a, b)

    elif seleccion == 3:
        print(jugador)

    elif seleccion == 4:
        flag = 0
