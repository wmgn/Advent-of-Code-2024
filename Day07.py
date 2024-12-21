with open("Day07.in") as file:
    lines = file.readlines()

lines = [[[int(s) for s in string.strip().split()] for string in line.split(":")] for line in lines]

def eval_operators(testval, nums, curr_result=None) -> bool:
    if len(nums) == 0 and curr_result == testval:
        return True
    elif len(nums) == 0:
        return False
    
    if curr_result is None:
        curr_result_add = nums[0]
        curr_result_multiply = nums[0]
    else:
        curr_result_add = curr_result+nums[0]
        curr_result_multiply = curr_result*nums[0]

    return ( eval_operators(testval, nums[1:], curr_result_add)
            or eval_operators(testval, nums[1:], curr_result_multiply) )

total_calibration_result = 0
for line in lines:
    testval = line[0][0]    # int e.g.   25056746772
    nums = line[1]          # array e.g. [4, 47, 136, 21, 79, 49]
    
    total_calibration_result += testval if eval_operators(testval, nums) is True else 0

print(f"total_calibration_result: {total_calibration_result}")



# Part 2

def eval_operators_part2(testval, nums, curr_result=None) -> bool:
    if len(nums) == 0 and curr_result == testval:
        return True
    elif len(nums) == 0:
        return False
    
    if curr_result is None:
        curr_result_add = nums[0]
        curr_result_multiply = nums[0]
        curr_result_concat = nums[0]
    else:
        curr_result_add = curr_result+nums[0]
        curr_result_multiply = curr_result*nums[0]
        curr_result_concat = int(str(curr_result)+str(nums[0]))

    return ( eval_operators_part2(testval, nums[1:], curr_result_add)
            or eval_operators_part2(testval, nums[1:], curr_result_multiply) 
            or eval_operators_part2(testval, nums[1:], curr_result_concat) )

total_calibration_result_part2 = 0
for line in lines:
    testval = line[0][0]    # int e.g.   25056746772
    nums = line[1]          # array e.g. [4, 47, 136, 21, 79, 49]
    
    total_calibration_result_part2 += testval if eval_operators_part2(testval, nums) is True else 0

print(f"total_calibration_result_part2: {total_calibration_result_part2}")