"""
    *** House Text Game ***

    @author: Jorge Galindo & Nelly Desu
    @company: Dev.f

    Éste es un juego de texto que te permite entrar en una casa y recorrer sus
    habitaciones y obtener una descripción de cada una de ellas. El jugador
    deberá caminar hasta encontrar la salida; en su recorrido tendrá acceso a
    la descripción de cada cuarto en el que se encuentre.

"""

player = [0,0]
start = (0,0)
end = (-5,6)
doors = ((-2,3))
room1 = ((-1, 1), (-1, 2), (-1, 3), (0, 1), (0, 2), (0, 3), (1, 1), (1, 2), (1, 3))
room2 = ((-5, 3), (-5, 4), (-5, 5), (-4, 3), (-4, 4), (-4, 5), (-3, 3), (-3, 4), (-3, 5))
room3 = ((-5, 7), (-5, 8), (-5, 9), (-4, 7), (-4, 8), (-4, 9), (-3, 7), (-3, 8), (-3, 9))
walls = ((-2, 0), (-2, 1), (-2, 2), (-2, 4), (-1, 0), (-1, 4), (0, 4), (1, 0), (1, 4), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),(-6, 2), (-6, 3), (-6, 4), (-6, 5), (-6, 6), (-5, 2), (-4, 2), (-4, 6), (-3, 2), (-3, 6), (-2, 5), (-2, 6), (-6, 7), (-6, 8), (-6, 9), (-6, 10), (-5, 10), (-4, 10), (-3, 10), (-2, 7), (-2, 8), (-2, 10))
messages = {"WALL":"\n¡Has topado con un muro!\n", "WIN":"\n*** ¡Felicidades! ¡Encontraste la salida! ***\n", "CHECKPOINT":"\nAcabas de cruzar una puerta: checkpoint\n", "POSITION_START":"\nEstás en el punto de partida\n", "POSITION_DOORS":"\nEstás en una puerta, entre dos habitaciones\n", "POSITION_CHECKPOINT":"\nEstás en la puerta de tu último check point\n", "INFO_START":"\nEstás en la puerta principal\n", "CHECKP_WARNING":"\nEstás en la puerta principal\n", "CHECKP_SPENT":"\nAcabas de agotar tus retornos al checkpoint\n", "CHECKP_NONE":"\nAún no has registrado ningún chechkpoint\n", "INPUT_SELEC":"\nIntroduce tu seleccion: ", "INPUT_STEPS":"\nIntroduce el número de pasos: ", "CHECKP_EMPTY":"\nSólo puedes regresar al último check point cuatro veces\n", "INPUT_OPTION":"[1] Continuar\n[2] Cancelar\n[ ]: ", "CHECKP_SPENT2":"\nAgotaste tus retornos al checkpoint\n"}
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
                print(messages["WALL"])
                break
            elif position == end:
                print(messages["WIN"])
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print(messages["CHECKPOINT"])
            else:
                continue
    elif a == 2:
        for x in range(b):
            player[1] -= 1
            position = tuple(player)
            if position in walls:
                player[1] += 1
                print(messages["WALL"])
                break
            elif position == end:
                print(messages["WIN"])
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print(messages["CHECKPOINT"])
            else:
                continue
    elif a == 3:
        for x in range(b):
            player[0] += 1
            position = tuple(player)
            if position in walls:
                player[0] -= 1
                print(messages["WALL"])
                break
            elif position == end:
                print(messages["WIN"])
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print(messages["CHECKPOINT"])
            else:
                continue
    elif a == 4:
        for x in range(b):
            player[0] -= 1
            position = tuple(player)
            if position in walls:
                player[0] += 1
                print(messages["WALL"])
                break
            elif position == end:
                print(messages["WIN"])
                status = 0
                break
            elif position in doors:
                checkpoint = list(position)
                print(messages["CHECKPOINT"])
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
        print(messages["POSITION_START"])
    if position in doors:
        print(messages["POSITION_DOORS"])
    if position == checkpoint:
        print(messages["POSITION_CHECKPOINT"])

def info(a):
    """
        Esta función va a proporcionar información de la habitación de acuerdo
        a la posición del jugador.

    """
    position = tuple(a)
    if position in room1:
        infoRoom1 = open("messages/infoRoom1.txt", "r")
        display = infoRoom1.read()
        print("\n"+display+"\n")
        infoRoom1.close()
    elif position in room2:
        infoRoom2 = open("messages/infoRoom2.txt", "r")
        display = infoRoom2.read()
        print("\n"+display+"\n")
        infoRoom2.close()
    elif position in room3:
        infoRoom3 = open("messages/infoRoom3.txt", "r")
        display = infoRoom3.read()
        print("\n"+display+"\n")
        infoRoom3.close()
    elif position == start:
        print(messages["INFO_START"])

def callCheckpoint(a):
    """
        Esta función actualiza las coordenadas del checkpoint y el contador
        de usos del checkpoint.

    """
    checkpointCounter = a
    checkpointCounter -= 1
    if checkpointCounter == 1:
        print(messages["CHECKP_WARNING"])
    elif checkpointCounter == 0:
        print(messages["CHECKP_SPENT"])
    return checkpointCounter


while flag == 1:

    if checkpointCounter == 0:
        flag == 0

    mainMenu = open("menus/main.txt", "r")
    display = mainMenu.read()
    print("\n"+display+"\n")
    mainMenu.close()
    selection = int(input(messages["INPUT_SELEC"]))
    print("")

    if selection == 1:
        directionMenu = open("menus/direction.txt", "r")
        display = directionMenu.read()
        print("\n"+display+"\n")
        directionMenu.close()
        a = int(input(messages["INPUT_SELEC"]))
        print("")

        stepsMenu = open("menus/steps.txt", "r")
        display = stepsMenu.read()
        print("\n"+display+"\n")
        b = int(input(messages["INPUT_STEPS"]))
        print("")

        #flag = (move(a, b))
        result = move(a, b)
        flag = result[0]
        checkpoint = result[1]
        comparePosition(player)

    elif selection == 2:
        info(player)

    elif selection == 3:
        if checkpoint == None:
            print(messages["CHECKP_NONE"])
        elif checkpointCounter > 0:
            print(messages["CHECKP_EMPTY"])
            h = int(input(messages["INPUT_OPTION"]))
            if h == 1:
                player = checkpoint
                checkpointCounter = callCheckpoint(checkpointCounter)
        else:
            print(messages["CHECKP_SPENT2"])

    elif selection == 4:
        print(player)
        print(flag)

    elif selection == 5:
        flag = 0
