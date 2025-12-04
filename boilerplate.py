def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

REPLACE_ME = readInput()