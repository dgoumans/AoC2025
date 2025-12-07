import time
import copy

start = time.time()

def readInput():
    lines = []
    file = open("test_input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

manifold = readInput()

base_manifold_matrix = []

for index in range(len(manifold)):
    temp_row = []
    for position in manifold[index]:
        temp_row.append(position)
    base_manifold_matrix.append(temp_row)

moving_patterns = []
binary_digits = (len(base_manifold_matrix)-2)/2

max_binary = ""
for i in range(int(binary_digits)):
    max_binary = max_binary + "1"

for binary in range(0,int(max_binary,2)):
    moving_patterns.append(str(bin(binary)[2:]))

laser_paths = 0
temp_matrix_for_count = []

for pattern in range(0, len(moving_patterns)):
    print(moving_patterns[pattern])
    manifold_matrix = copy.deepcopy(base_manifold_matrix)

    for index in range(len(manifold_matrix)-1):      
        for position in range(len(manifold_matrix[0])):
            char = manifold_matrix[index][position]
            if char == "S":
                manifold_matrix[index+1][position] = "|"
            elif char == "|":
                if manifold_matrix[index+1][position] == ".":
                    manifold_matrix[index+1][position] = "|"
                elif manifold_matrix[index+1][position] == "^":                                 
                    try:
                        if int(moving_patterns[pattern][int(index/2)]) == 1:
                            manifold_matrix[index+1][position+1] = "|" ## split right   
                    except Exception as e:
                        manifold_matrix[index+1][position-1] = "|" ## split left   
                    else:
                        if int(moving_patterns[pattern][int(index/2)]) == 0:
                            manifold_matrix[index+1][position-1] = "|" ## split left   
        time.sleep(0.05)
        print("".join(manifold_matrix[index+1]))
        time.sleep(0.05)       
        temp_matrix_for_count.append(manifold_matrix)
        
matrix_for_count = []
for manifold in temp_matrix_for_count:
    if manifold not in matrix_for_count:
        matrix_for_count.append(manifold)

end = time.time()

print(len(matrix_for_count))

execution_time = end - start
print("Total runtime of the program is", execution_time ,"seconds")
