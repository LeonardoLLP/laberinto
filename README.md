# Laberinto

Dirección del respositorio: [laberinto.git](https://github.com/LeonardoLLP/laberinto)

El código se divide en dos partes. En primer lugar, creamos el laberinto con muros en las coordenadas dadas.
Por otro lado, programamos un "personaje", un referente que va a ir moviéndose por el laberinto y probando los distintos caminos hasta llegar al final.
Una vez hecho esto, solo queda convertir los distintos movimientos del "personaje" y traducirlos a lenguaje comprensible.

Por otro lado, el diagrama de flujo es el siguiente:

<br>
<img height="800" src="https://github.com/LeonardoLLP/laberinto/blob/main/laberinth_true.drawio.png" />
<br>

Antes de mostrar el código, queda relatar un defecto que no me ha dado tiempo a resolver. Aunque el código actual consigue llegar al final, no muestra el camino más corto siempre. He reflexionado un poco acerca de ello y he llegado a dos soluciones. La primera, solución propia, consiste en realizar otra lista junto a las direcciones de las casilas de las coordenadas por las que va pasando el personaje. Cuando el jugador pase otra vez por la misma casilla, significará que el recorrido que ha hecho hasta entonces ha sido en vano, por lo que se podrá borrar todas las instrucciones hechas hasta esa casilla.

El segundo método, fruto de la investigación, consiste en utilizar un método de "pathfinding", usado hoy en día para controlar IAs en videojuegos y simulaciones. Este método encontraría directamente el camino más corto, y podría resolver también "laberintos dentro de laberinto", problema comentado en el código. Aquí dejo un vídeo que me llamó mucho la atención en referencia al pathfinding.
https://www.youtube.com/watch?v=-L-WgKMFuhE&t=501s&ab_channel=SebastianLague

Ambos métodos podrían implementarse en el código, y el primero con mucha facilidad (el segundo requeriría de un poco de investigación), pero con motivos de tiempo no se ha hecho (y el laberinto a resolver es muy sencillo).

A continuación, el código completo.

```python
#! Generación del laberinto

wall_coordinates = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))


lab_dimensions = (5, 5)

lab = []

for row in range(lab_dimensions[0]):
    lab.append([])
    for column in range(lab_dimensions[1]):
        lab[row].append("")


# Using try-catch just to make sure no out-of-range index or invalid coordinates (like floats)
try:
    for coordinate in wall_coordinates:
        lab[coordinate[0]][coordinate[1]] = "X"
except:
    raise Exception("Had a problem setting up wall. Check the coordinates of @wall_coordinates")

# Creation of start/end
#* Como S es en función de las dimensiones del laberinto, [-1] siempre se ajustará a las dimensiones del laberinto
lab[0][0] = "E"
lab[-1][-1] = "S"


# Code from stackoverflow:
#* print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))

for row in lab:
    print("[", end="")
    for index in range(len(row)):
        if index != len(row) - 1:
            print("{:6}".format("\'" + row[index] + "\', "), end="")
        else:
            print("{:6}".format("\'" + row[index] + "\'"), end="")
    print("]")

#! Solution to laberinth:
#! Usamos el método "mantenerse siempre a la derecha"

position = [0, 0]
directions = ((0, 1), (1, 0), (0, -1), (-1, 0))
solution = []

#* Variables de control-flow
try_right = True
rotation_index = 0


#! Método 1
""" while lab[position[0]][position[1]] != "S":  # Mientras no esté en el final:
    print(position)
    print(directions[rotation_index])
    coor_to_go = [position[coor] + directions[rotation_index][coor] for coor in range(2)]  # Posición a la que voy

    try:
        place_to_go = lab[coor_to_go[0]][coor_to_go[1]]
    except:
        place_to_go = "X"

    if place_to_go != "X" and tuple(coor_to_go) in valid_coordinates :  # If there is no wall:
        position = coor_to_go
        solution.append(directions[rotation_index])
        try_right = True

    else:
        if try_right == True:
            rotation_index += 1  # Rotating right
            try_right = False
        else:
            rotation_index -= 1  # Rotating left

        # Mantenerse en rotaciones permitidas
        if rotation_index >= len(directions):
            rotation_index -= len(directions)
        elif rotation_index < 0:
            rotation_index += len(directions) """

        # Resumiendo mucho: este código no funciona para otro laberinto.
        # Si el jugador puede girar a la derecha, TIENE que girar a la derecha para mantenerse en la prueba de todos los caminos.
        # En el código, si puede seguir al frente, seguirá al frente. Hay que cambiar eso
        # El código se rompe en cruces de cuatro caminos

#! Método 2 (mejor): mantenerse siempre a la derecha
while lab[position[0]][position[1]] != "S":  # Mientras no esté en el final:
    #* ROTAMOS ANTES DE SEGUIR HACIA DELANTE
    if try_right == True:
        rotation_index += 1  # Rotating right
        try_right = False
    else:
        rotation_index -= 1  # Rotating left

    #* Mantenerse en rotaciones permitidas
    if rotation_index >= len(directions):
        rotation_index -= len(directions)
    elif rotation_index < 0:
        rotation_index += len(directions)

    # Coordenadas adónde vamos
    coor_to_go = [position[coor] + directions[rotation_index][coor] for coor in range(2)]  # Posición a la que voy

    is_valid = not (False in [0 <= coor_to_go[i] < lab_dimensions[i] for i in range(2)])

    try:
        place_to_go = lab[coor_to_go[0]][coor_to_go[1]]
    except:
        place_to_go = "X"

    if place_to_go != "X" and is_valid :  # If there is no wall:
        position = coor_to_go
        solution.append(directions[rotation_index])
        try_right = True


# print(solution)

directions_to_follow = []

for instruction in solution:
    if instruction == (0, 1):
        directions_to_follow.append("Right")
    elif instruction == (1, 0):
        directions_to_follow.append("Down")
    elif instruction == (0, -1):
        directions_to_follow.append("Left")
    elif instruction == (-1, 0):
        directions_to_follow.append("Up")

# print(directions_to_follow)

directions_str = ""
for direction in directions_to_follow:
    directions_str += str(direction).casefold() + ", "

#* Remove last comma with slices and add final dot
directions_str = directions_str[:-2] + "."


print("The directions needed to reach the end are: " + directions_str)





# Solución: gira hacia la derecha, y luego prueba hacia la izquierda hasta que halles un camino
# Para este laberinto, no debería de afectar

# Este código no funciona para laberintos complejos: laberintos dentro de laberintos
# Sin embargo, como las entrada y salida siempre está en esquinas del laberinto "inicial", no hay problema. No hace falta implementar este código
```