a = [-2,0]
b = [2,0]
c = [-2,4]
d = [2, 4]
doors = [(-2,3),(0,0),(-5,6),(-2,9)]
puntos = [(x,y) for x in range(-6,-1) for y in range(6,11)]
area = [(x,y) for x in range(-5,-2) for y in range(7,10)]

print("Área: ",area)
print("Walls: ",puntos)

for i in puntos[:]:
    if i in area:
        puntos.remove(i)
    elif i in doors:
        puntos.remove(i)

print("Walls: ",puntos[:])
