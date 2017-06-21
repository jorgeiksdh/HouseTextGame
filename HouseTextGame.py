"""
    *** House Text Game ***

    @author: Jorge Galindo
    @company: Dev.f

    Éste es un juego de texto que te permite entrar en una casa y recorrer sus
    habitaciones y obtener una descripción de cada una de ellas. El jugador
    deberá caminar hasta encontrar la salida; en su recorrido tendrá acceso a
    la descripción de cada cuarto en el que se encuentre.

"""

player = [0,0]
doors = ((-2,3),(0,0))
room1 = ((-1,1), (0,1), (1,1), (-1,2), (0,2), (1,2), (-1,3),(0,3),(1,3))
walls = ((-2,0),(-1,0),(1,0),(2,0),(-2,1),(2,1),(-2,2),(2,2),(2,3),(-2,4),(-1,4),(0,4),(1,4),(2,4))
flag = 1

def move(a, b):
    """
        Esta función va a cambiar la posición del jugador de acuerdo a las
        instrucciones que le proporcione el usuario

    """
    status = 1
    if a == 1:
        for x in range(b):
            player[1] += 1
            position = tuple(player)
            if position in walls:
                player[1] -= 1
                print("\nHas topado con un muro\n")
                break
            elif position == (-2,3):
                print("\n¡Felicidades! ¡Encontraste la salida!\n")
                status = 0
                break
            else:
                continue
    elif a == 2:
        for x in range(b):
            player[1] -= 1
            position = tuple(player)
            if position in walls:
                player[1] += 1
                print("\nHas topado con un muro\n")
                break
            elif position == (-2,3):
                print("\n¡Felicidades! ¡Encontraste la salida!\n")
                status = 0
                break
            else:
                continue
    elif a == 3:
        for x in range(b):
            player[0] += 1
            position = tuple(player)
            if position in walls:
                player[0] -= 1
                print("\nHas topado con un muro\n")
                break
            elif position == (-2,3):
                print("\n¡Felicidades! ¡Encontraste la salida!\n")
                status = 0
                break
            else:
                continue
    elif a == 4:
        for x in range(b):
            player[0] -= 1
            position = tuple(player)
            if position in walls:
                player[0] += 1
                print("\nHas topado con un muro\n")
                break
            elif position == (-2,3):
                print("\n¡Felicidades! ¡Encontraste la salida!\n")
                status = 0
                break
            else:
                continue
    return status

def comparePosition(a):
    """
        Esta función va a comparar la posición del jugador con la posición
        de la entrada y la salida de la casa, así como de las puertas de las
        habitaciones.

    """
    position = tuple(a)
    if position == (0,0):
        print("\nHas regresado a tu punto de partida\n")

def info(a):
    """
        Esta función va a proporcionar información de la habitación de acuerdo
        a la posición del jugador.

    """
    position = tuple(a)
    if position in room1:
        print("\nEstás parado en la sala principal. Por el momento es una habitación vacía.\n")
    if position == (0,0):
        print("\nEstás en la puerta principal\n")

while flag == 1:
    mainMenu = open("menus/main.txt", "r")
    display = mainMenu.read()
    print("\n"+display+"\n")
    mainMenu.close()
    selection = int(input("\nIntroduzca su selección: "))
    print("")

    if selection == 1:
        directionMenu = open("menus/direction.txt", "r")
        display = directionMenu.read()
        print("\n"+display+"\n")
        directionMenu.close()
        a = int(input("\nIntroduce tu seleccion: "))
        print("")

        stepsMenu = open("menus/steps.txt", "r")
        display = stepsMenu.read()
        print("\n"+display+"\n")
        b = int(input("\nIntroduce el número de pasos: "))
        print("")

        flag = (move(a, b))
        comparePosition(player)

    elif selection == 2:
        info(player)

    elif selection == 3:
        print(player)
        print(flag)

    elif selection == 4:
        flag = 0
