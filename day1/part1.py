def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

rotations = readInput()

dial_position = 50
zero_count = 0

for rotation in rotations:
    rotation_direction = rotation[0]
    rotation_amount = int(rotation[1:][-2:])

    if rotation_direction == "L":
        dial_position = dial_position - rotation_amount
    if rotation_direction == "R":
        dial_position = dial_position + rotation_amount
    
    if dial_position > 99:
        dial_position = dial_position - 100
    if dial_position < 0:
        dial_position = dial_position + 100

    if dial_position == 0:
        zero_count = zero_count + 1
        
print(zero_count)
