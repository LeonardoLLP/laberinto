muro = ((0,1), (0,2), (0,3), (0,4), (1,1), (2,1), (2,3), (3,3), (4,0), (4,1), (4,2), (4,3))

lab_dimensions = (5, 5)

lab = []

for i in range(lab_dimensions[0]):
    row = lab.append([])
    for j in range(lab_dimensions[1]):
        row.append("")

print(lab)