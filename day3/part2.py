def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

bank_list = readInput()

max_max_banks = []
for bank in bank_list: 
    max_bank = []
    bank_lenght_left = len(bank)
    for battery in bank:
        if max_bank == []:
            max_bank.append(battery)
        else:
            if bank_lenght_left >= 12-len(max_bank):
                if bank_lenght_left >= 12:
                    to_check_range = 12
                else:
                    to_check_range = bank_lenght_left
                for check in range(12,12-to_check_range,-1):
                    if len(max_bank) > check-1:
                        if battery > max_bank[check-1]:
                            max_bank.pop()
            if len(max_bank) < 12:                
                max_bank.append(battery)
        bank_lenght_left = bank_lenght_left - 1
    max_max_banks.append(max_bank)

max_joltages = 0
for item in max_max_banks:
    item_value = ""
    for temp_battery in item:
        item_value = item_value + temp_battery
    max_joltages = max_joltages + int(item_value)
print(max_joltages)