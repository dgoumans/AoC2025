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

split_lasers = 0

print("".join(manifold_matrix[0]))
for index in range(len(manifold_matrix)-1):
    print("".join(manifold_matrix[index+1]),end='\r')
    for position in range(len(manifold_matrix[0])):
        char = manifold_matrix[index][position]
        if char == "S":
            manifold_matrix[index+1][position] = "|"
        elif char == "|":
            if manifold_matrix[index+1][position] == ".":
                manifold_matrix[index+1][position] = "|"
            elif manifold_matrix[index+1][position] == "^":
                manifold_matrix[index+1][position-1] = "|"
                manifold_matrix[index+1][position+1] = "|"
                split_lasers = split_lasers + 1
    time.sleep(0.1)
    print("".join(manifold_matrix[index+1]))
    time.sleep(0.1)
    
print("Total splits:",split_lasers)
