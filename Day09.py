with open("Day09.in") as file:
    input = file.read()

#print(input)
# example disk map (puzzle input)
# 2333133121414131402

# create string based on input

#input = "12345"

disk_map = []

for i in range(len(input)):
    #print(f"i: {i}")
    if i%2 == 0:
        for j in range(int(input[i])):
            disk_map.append(int(i/2))
    else:
        for j in range(int(input[i])):
            disk_map.append(".")

    #print(f"    disk_map: {disk_map}")

#print(f"disk_map: {disk_map}")
#quit()
#disk_map = [char for char in disk_map]

try:
    while idx := disk_map.index("."):
        disk_map[idx] = disk_map.pop(-1)
except ValueError:
    print("ValueError: ('.' is not in list?)") #therefore filesystem is compacted, we are done?
except IndexError:
    print("IndexError")

#print(f"disk_map: {disk_map}")

total_checksum = sum([i*num for i, num in enumerate(disk_map)])
print(total_checksum)

# 88,881,734,731 was also too low ???
# 5,561,233,379 was too low
# 6,242,766,523,059 or 6242766523059