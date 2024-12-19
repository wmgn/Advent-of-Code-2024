

with open("Day_1_data.txt") as file:    
    puzzle_input = file.read().strip()

puzzle_list = puzzle_input.split("\n")
puzzle_list = [s.split("   ") for s in puzzle_list]

l = [int(arr[0]) for arr in puzzle_list]
r = [int(arr[1]) for arr in puzzle_list]

l.sort()
r.sort()

total = 0
for i in range(len(l)):
    total += abs(r[i]-l[i])

print("total: " + str(total))


# part 2

similarity_score = 0
for num in l:
    similarity_score += num * r.count(num)

print(f"similarity_score: {similarity_score}")





''' # Old code
#print(l)
#print(r)

puzzle_list_ints = [int(i) for i in puzzle_list]

l = puzzle_list_ints[0::2]
r = puzzle_list_ints[1::2]
'''