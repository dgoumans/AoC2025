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

            half = len(str(product_ID))/2
            
            if half.is_integer():
                seq1 = str(product_ID)[:int(half)]
                seq2 = str(product_ID)[-int(half):]

                if seq1 == seq2:
                    invalid_ID_list.append(product_ID)

    print(sum(invalid_ID_list))
