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

def get_ingredients(ingredients_file):
    temp_ranges = []
    ingredients_file.reverse()
    for line in ingredients_file:
        if line != "":
            temp_ranges.append(int(line))
        else:
            temp_ranges.sort()
            return temp_ranges

fresh_ranges = get_fresh_ranges(input_file)
ingredients = get_ingredients(input_file)

fresh_item_count = 0
for ingredient in ingredients:
    for fresh_range in fresh_ranges:
        if fresh_range["range_start"] < ingredient:
            if ingredient < fresh_range["range_end"]:
                fresh_item_count = fresh_item_count + 1
                break
print(fresh_item_count)