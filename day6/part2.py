def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.rstrip())
    file.close()
    return lines

puzzle_input = readInput()
worksheet = []

max_lenght = 0
for row in puzzle_input:
    if len(row) > max_lenght:
        max_lenght = len(row)

previous_operator = max_lenght

for index in range(max_lenght-3,-1,-1):
    if puzzle_input[-1][index] == "+" or puzzle_input[-1][index] == "*":
        problem = []
        for sweep in range(previous_operator, index, -1):
            value = ""
            for row in range(0,len(puzzle_input)-1):
                if sweep > len(puzzle_input[row]):
                    value = value + " "
                else:
                    value = value + puzzle_input[row][sweep-1]
            value = value.strip()
            if value != "":
                problem.append(value)
        
        if puzzle_input[-1][index] == "+":
            problem.append("+") 
        if puzzle_input[-1][index] == "*":
            problem.append("*")
        worksheet.append(problem)        
        previous_operator = index

for problem_row in range(len(worksheet)):
    for item in range(len(worksheet[problem_row])):
        worksheet[problem_row][item] = worksheet[problem_row][item].strip()

problem_total = 0
for problem in worksheet:
    solution = problem[0]
    for item in problem[1:-1]:
        if problem[-1] == "*":
            solution = int(solution) * int(item)
        elif problem[-1] == "+":
            solution = int(solution) + int(item)
    problem_total = problem_total + solution

print(problem_total)