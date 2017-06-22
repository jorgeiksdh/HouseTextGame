globalFlag = 1
points = []
area = []
doors = [(-2,3),(0,0)]
entrance = ()
out = ()

while globalFlag == 1:
    print("1. Obtener las coordenadas del muro y del área del cuarto")
    print("2. Salir")
    choice = int(input("Selección: "))

    if choice == 1:
        choiceFlag = 1
        while choiceFlag == 1:
            x1 = int(input("Introduzca el primer valor de x, el menor: "))
            x2 = int(input("Introduzca el segundo valor de x, el mayor: "))
            y1 = int(input("Introduzca el primer valor de y, el menor: "))
            y2 = int(input("Introduzca el segundo valor de y, el mayor: "))

            pointBuffer = [(x,y) for x in range(x1,x2+1) for y in range(y1,y2+1)]
            areaBuffer = [(x,y) for x in range(x1+1,x2) for y in range(y1+1,y2)]

            print("Area = ",areaBuffer)

            for i in pointBuffer[:]:
                if i in area:
                    pointBuffer.remove(i)

            points.append(pointBuffer)

            print("Walls: ",points)

            wallsFlag = 1
            while wallsFlag == 1:
                print("De la lista de coordenadas selecciona la o las puertas del cuarto")
                selectionX = int(input("Coordenada x: "))
                selectionY = int(input("Coordenada y: "))
                coord = (selectionX, selectionY)
                doors.append(coord)
                for i in points[:]:
                    if i in doors:
                        points.remove(i)
                print("Walls: ",points)
                print("\n1. Ingresar otra puerta\n2. Siguiente paso")
                option = int(input("Selección: "))
                if option == 1:
                    continue
                else:
                    wallsFlag = 0

            print("\n1. Ingresar otro cuarto\n2. Seleccionar entradas y salidas")
            selection = int(input("Selección: "))
            if selection == 1:
                continue
            else:
                choiceFlag = 0

        print("Walls: ",points)
        print("De la lista de coordenadas selecciona la entrada")
        selectionX = int(input("Coordenada x: "))
        selectionY = int(input("Coordenada y: "))
        coord = (selectionX, selectionY)
        entrance = coord
        print("De la lista de coordenadas selecciona la salida")
        selectionX = int(input("Coordenada x: "))
        selectionY = int(input("Coordenada y: "))
        coord = (selectionX, selectionY)
        out = coord

        for i in puntos[:]:
            if i in entrance or i in out:
                puntos.remove(i)

        print("walls = ",points)
        print("area = ",area)
        print("doors = ",doors)
        print("in = ",entrance)
        print("out = ",out)

    elif choice == 2:
        globalFlag = 0
