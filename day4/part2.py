def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

input = readInput()

roll_matrix = []

for row in range(0,len(input)):
    temp_row = []
    for position in input[row]:
        temp_row.append(position)
    roll_matrix.append(temp_row)

reachable_roll_count = 0
count = 0

def remove_rolls(matrix):
    global count
    global reachable_roll_count
    reachable_matrix = []

    for row in range(len(matrix)):
        reachable_matrix.append([])
        for position in range(len(matrix[row])):
            if matrix[row][position] == "@":
                reachable_matrix[row].append("@")
                adjecent_rolls = 0        
                for pos_y in range(row-1,row+2,1):
                    for pos_x in range(position-1,position+2,1):
                        if pos_y == row and pos_x == position:
                            continue
                        if 0 <= pos_y <= (len(matrix)-1):
                            if 0 <= pos_x <= (len(matrix[row])-1):
                                if matrix[pos_y][pos_x] == "@":
                                    adjecent_rolls = adjecent_rolls + 1
                if adjecent_rolls < 4:
                    reachable_matrix[row][position] = "X"
                    reachable_roll_count = reachable_roll_count + 1
            else:
                reachable_matrix[row].append(".")
    
    if matrix == reachable_matrix:
        return reachable_matrix
    else:
        return remove_rolls(reachable_matrix)

final_matrix = remove_rolls(roll_matrix)

for row in final_matrix:
    row_string = ""
    for char in row:
        row_string = row_string + char
    print(row_string)

print("Reachable rolls: ", reachable_roll_count)
