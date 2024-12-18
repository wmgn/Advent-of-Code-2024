

def check_all_inc_or_dec(arr):
    if arr[1] == arr[0]:
        return False
    elif arr[1] > arr[0]:
        inc = True
    else:
        inc = False

    for i in range(2,len(arr)):
        if inc:
            if arr[i] <= arr[i-1]:
                return False
        else: #dec
            if arr[i] >= arr[i-1]:
                return False
            
    return True


def check_adj_levels_differ(arr):
    for i in range(1,len(arr)):
        diff = abs(arr[i] - arr[i-1])
        if diff == 0 or diff > 3:
            return False

    return True



with open("Day_2_data.txt") as file:
    inputData = file.readlines()

#print(data)

# TODO clean up data for useage

# Strip all strings in the array
arr2d = [[int(s) for s in line.strip().split()] for line in inputData]
#print(arr2d)

safe = 0
for arr in arr2d:
    if check_all_inc_or_dec(arr) and check_adj_levels_differ(arr):
        safe += 1

print(f"num safe: {safe}")

# The levels are either all increasing or all decreasing.
# Any two adjacent levels differ by at least one and at most three.
# both of these have to be true ^^


# part 2
safe_2 = 0
for arr in arr2d:
    for idx in range(len(arr)):
        arrNew = []

        for j in range(len(arr)):
            if j != idx:
                arrNew.append(arr[j])
                
        if check_all_inc_or_dec(arrNew) and check_adj_levels_differ(arrNew):
            safe_2 += 1
            break

print(f"num safe_2: {safe_2}")