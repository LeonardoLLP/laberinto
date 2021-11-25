wall_coordinates = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

lab_dimensions = (5, 5)

lab = []

for row in range(lab_dimensions[0]):
    lab.append([])
    for column in range(lab_dimensions[1]):
        lab[row].append("")

print(lab)

# Using try-catch just to make sure no out-of-range index or invalid coordinates (like floats)
try:
    for coordinate in wall_coordinates:
        lab[coordinate[0]][coordinate[1]] = "X"
except:
    raise Exception("Had a problem setting up wall. Check the coordinates of @wall_coordinates")

print(lab)

# Code from stackoverflow:
#* print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in A]))

for row in lab:
    print("[", end="")
    for index in range(len(row)):
        if index != len(row) - 1:
            print("\'" + row[index] + "\', ", end="")
        else:
            print("\'" + row[index] + "\'", end="")
    print("]")