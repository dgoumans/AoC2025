def readInput():
    lines = []
    file = open("test_input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

input = readInput()

roll_matrix = []
reachable_matrix = []

for row in range(0,len(input)):
    temp_row = []
    for position in input[row]:
        temp_row.append(position)
    roll_matrix.append(temp_row)
    print(roll_matrix[row])

for row in range(0,len(input)):
    temp_row = []
    for position in input[row]:
        temp_row.append(position)
    reachable_matrix.append(temp_row)

reachable_roll_count = 0

for row in range(len(roll_matrix)):
    for position in range(len(roll_matrix[row])):
        if roll_matrix[row][position] == "@":
            adjecent_rolls = 0        
            for pos_y in range(row-1,row+2,1):
                for pos_x in range(position-1,position+2,1):
                    if pos_y == row and pos_x == position:
                        continue
                    if 0 <= pos_y <= (len(roll_matrix)-1):
                        if 0 <= pos_x <= (len(roll_matrix[row])-1):
                            if roll_matrix[pos_y][pos_x] == "@":
                                adjecent_rolls = adjecent_rolls + 1
            if adjecent_rolls < 4:
                reachable_roll_count = reachable_roll_count + 1
print("Reachable rolls: ", reachable_roll_count)
