def readInput():
    lines = []
    file = open("input", "r")
    for line in file:
        lines.append(line.strip())
    file.close()
    return lines

for line in readInput():

    invalid_ID_list = []
    product_ranges = line.split(',')
    for product_range in product_ranges:
        range_start = int(product_range.split("-")[0])
        range_end = int(product_range.split("-")[1])

        for product_ID in range(range_start,range_end+1,1):
            for n in range(1,len(str(product_ID)),1):
                parts = []
                for i in range(0, len(str(product_ID)), n):
                    parts.append(str(product_ID)[i:i+n])
                
                check = True
                for part in parts:
                    if part != parts[0]:
                        check = False
                if check:
                    if product_ID not in invalid_ID_list:
                        invalid_ID_list.append(product_ID)

    print(sum(invalid_ID_list))
