def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

input_file = readInput()

def get_fresh_ranges(ranges_file):
    temp_ranges = []
    for line in ranges_file:
        if line != "":
            start_end = line.split("-")
            temp_ranges.append(dict(range_start = int(start_end[0]),range_end = int(start_end[1])))
        else:
            return sorted(temp_ranges, key=lambda d: d['range_start'])
fresh_ranges = get_fresh_ranges(input_file)

total_fresh = 0
highest_end = 0
highest_start = 0

for fresh_range in fresh_ranges:    
    if fresh_range["range_end"] > highest_end:
        if fresh_range["range_start"] > highest_end:
            highest_start = fresh_range["range_start"]
        else:
            highest_start = highest_end + 1
        
        highest_end = fresh_range["range_end"]

        addition = highest_end - highest_start + 1
        total_fresh = total_fresh + addition   

print(total_fresh)