def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

bank_list = readInput()

battery_list = []

for bank in bank_list: 
    d1 = bank[0]
    d2 = bank[1]

    for index in range(1,len(bank),1):
        last = False
        if index == len(bank)-1:
            last = True
        
        if not last:
            if bank[index] > d1:
                d1 = bank[index]
                d2 = bank[index+1]
            else:
                if bank[index] > d2:
                    d2 = bank[index]
        if last:
            if bank[index] > d2:
                d2 = bank[index]
    battery_list.append(int(str(d1 + d2)))

print(sum(battery_list))
