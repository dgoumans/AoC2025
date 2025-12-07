import time

def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

manifold = readInput()

manifold_matrix = []
for index in range(len(manifold)):
    temp_row = []
    for position in manifold[index]:
        temp_row.append(position)
    manifold_matrix.append(temp_row)

print("".join(manifold_matrix[0]))

for index in range(len(manifold_matrix)-1):
    for position in range(len(manifold_matrix[0])):
        char = manifold_matrix[index][position]

        if char == "S":
            manifold_matrix[index+1][position] = 1
            continue
        if char == ".":
            continue
        if char == "^":
            continue

        if manifold_matrix[index+1][position] == "^":
            if manifold_matrix[index+1][position-1] == ".":
                manifold_matrix[index+1][position-1] = int(manifold_matrix[index][position])
            else:
                temp = int(manifold_matrix[index][position])
                manifold_matrix[index+1][position-1] = int(manifold_matrix[index+1][position-1]) + int(manifold_matrix[index][position])

            if manifold_matrix[index+1][position+1] == ".":
                manifold_matrix[index+1][position+1] = int(manifold_matrix[index][position])
        elif manifold_matrix[index+1][position] == ".":
            manifold_matrix[index+1][position] = int(manifold_matrix[index][position])
        else:
             manifold_matrix[index+1][position] = int(manifold_matrix[index+1][position]) + int(manifold_matrix[index][position])

    time.sleep(0.1)
    temp_s = ""
    for item in manifold_matrix[index+1]:
        temp_s = temp_s + str(item)
    print(temp_s)
    time.sleep(0.1)

count = 0
for item in manifold_matrix[-1]:
    if item != ".":
        count = count + int(item)
print(count)