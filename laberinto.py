muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

lab_dimensions = (5, 5)

lab = []

for row in range(lab_dimensions[0]):
    lab.append([])
    for column in range(lab_dimensions[1]):
        lab[row].append("")

print(lab)

