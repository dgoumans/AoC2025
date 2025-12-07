def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

puzzle_input = readInput()

horizontal_worksheet = []

for i in range(len(puzzle_input)):
    items = puzzle_input[i].split()
    horizontal_worksheet.append([])
    for y in range(len(items)):
        horizontal_worksheet[i].append(items[y])

vertical_worksheet = []

for i in range(len(horizontal_worksheet[0])):
    column = []
    for y in range(len(horizontal_worksheet)):
        column.append(horizontal_worksheet[y][i])
    vertical_worksheet.append(column)

problem_total = 0
for problem in vertical_worksheet:
    solution = problem[0]
    for item in problem[1:-1]:
        if problem[-1] == "*":
            solution = int(solution) * int(item)
        elif problem[-1] == "+":
            solution = int(solution) + int(item)
    problem_total = problem_total + solution
print(problem_total)