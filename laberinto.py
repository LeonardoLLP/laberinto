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
print(len(directions))

try_right = True
rotation_index = 0

while lab[position[0]][position[1]] != "S":  # Mientras no esté en el final:
    place_to_go = [position[coor] + directions[rotation_index][coor] for coor in range(2)]  # Posición a la que voy

    if lab[place_to_go[0]][place_to_go[1]] != "X":  # If there is no wall:
        position = place_to_go
        solution.append(directions[rotation_index])

    else:
        if try_right == True:
            rotation_index += 1  # Rotating right
        else:
            rotation_index -= 1  # Rotating left

        if rotation_index >= len(directions):
            rotation_index -= len(directions)
        elif rotation_index < 0:
            rotation_index += len(directions)

print(solution)

