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
start = (0,0)
end = (-5,6)
doors = ((-4,5),(-2,3))
room1 = ((-1, 1), (-1, 2), (-1, 3), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3))
room2 = ((-5, 3), (-5, 4), (-5, 5), (-4, 3), (-4, 4), (-4, 5), (-3, 3), (-3, 4), (-3, 5))
walls = ((-2, 0), (-2, 1), (-2, 2), (-2, 4), (-1, 0), (-1, 4), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),(-6, 2), (-6, 3), (-6, 4), (-6, 5), (-6, 6), (-5, 2), (-4, 2), (-4, 6), (-3, 2), (-3, 6), (-2, 5), (-2, 6))
checkpoint = None
checkpointCounter = 4
flag = 1

def move(a, b):
    """
        Esta función va a cambiar la posición del jugador de acuerdo a las
        instrucciones que le proporcione el usuario

    """
    checkpoint = None
    status = 1
    if a == 1:
        for x in range(b):
            player[1] += 1
            position = tuple(player)
            if position in walls:
                player[1] -= 1
                print("\nHas topado con un muro\n")
                break
            elif position == end:
                print("\n¡Felicidades! ¡Encontraste la salida!\n",player)
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print("\nAcabas de cruzar una puerta",checkpoint)
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
            elif position == end:
                print("\n¡Felicidades! ¡Encontraste la salida!\n",player)
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print("\nAcabas de cruzar una puerta",checkpoint)
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
            elif position == end:
                print("\n¡Felicidades! ¡Encontraste la salida!\n",player)
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print("\nAcabas de cruzar una puerta",checkpoint)
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
            elif position == end:
                print("\n¡Felicidades! ¡Encontraste la salida!\n",player)
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print("\nAcabas de cruzar una puerta",checkpoint)
            else:
                continue
    return [status, checkpoint]

def comparePosition(a):
    """
        Esta función va a comparar la posición del jugador con la posición
        de la entrada y la salida de la casa, así como de las puertas de las
        habitaciones.

    """
    position = tuple(a)
    if position == start:
        print("\nEstás en el punto de partida\n")
    if position in doors:
        print("\nEstás en una puerta, entre dos habitaciones\n")
    if position == checkpoint:
        print("\nEstás en la puerta de tu último check point\n")

def info(a):
    """
        Esta función va a proporcionar información de la habitación de acuerdo
        a la posición del jugador.

    """
    position = tuple(a)
    if position in room1:
        print("\nEstás en la sala principal. Por el momento es una habitación vacía.\n")
    elif position in room2:
        print("\nEstás en el salón de música. Por el momento está vacío\n")
    elif position == start:
        print("\nEstás en la puerta principal\n")

def callCheckpoint(a):
    """
        Esta función actualiza las coordenadas del checkpoint y el contador
        de usos del checkpoint.

    """
    checkpointCounter = a
    checkpointCounter -= 1
    if checkpointCounter == 1:
        print("\nCUIDADO: sólo dispones de un retorno más al checkpoint\n")
    elif checkpointCounter == 0:
        print("\nAcabas de agotar tus retornos al checkpoint\n")
    return checkpointCounter


while flag == 1:

    if checkpointCounter == 0:
        flag == 0

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

        #flag = (move(a, b))
        result = move(a, b)
        flag = result[0]
        checkpoint = result[1]
        print(checkpoint)
        comparePosition(player)

    elif selection == 2:
        info(player)

    elif selection == 3:
        if checkpoint == None:
            print("\nAún no has registrado ningún chechkpoint\n")
        elif checkpointCounter > 0:
            print("\nSólo puedes regresar al último check point cuatro veces\n")
            h = int(input("[1] Continuar\n[2] Cancelar\n[ ]: "))
            if h == 1:
                player = checkpoint
                checkpointCounter = callCheckpoint(checkpointCounter)
        else:
            print("Agotaste tus retornos al checkpoint")

    elif selection == 4:
        print(player)
        print(flag)

    elif selection == 5:
        flag = 0
