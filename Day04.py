with open("Day4.txt") as file:
    lines = file.readlines()
    #file.seek(0)
    #input = file.read()

lines = [line.strip() for line in lines] # make sure to get rid of whitespace, like /n

total_XMAS_occurances = 0

for i in range(len(lines)): # i = rows, up and down
    for j in range(len(lines[i])): # j = columns, across left and right

        # horizontal (rows)
        if j+3 < len(lines[i]):
            letter_group = lines[i][j] + lines[i][j+1] + lines[i][j+2] + lines[i][j+3]
            if letter_group == "XMAS" or letter_group == "SAMX":
                total_XMAS_occurances += 1
        
        # vertical (columns)
        if i+3 < len(lines):
            letter_group = lines[i][j] + lines[i+1][j] + lines[i+2][j] + lines[i+3][j]
            if letter_group == "XMAS" or letter_group == "SAMX":
                total_XMAS_occurances += 1

        # diagonal (checks Southeast ↘ and the reverse, Northwest ↖ diagonals)
        if i+3 < len(lines) and j+3 < len(lines[i]):
            letter_group = lines[i][j] + lines[i+1][j+1] + lines[i+2][j+2] + lines[i+3][j+3]
            if letter_group == "XMAS" or letter_group == "SAMX":
                total_XMAS_occurances += 1
        
        # diagonal (checks Southwest ↙ and the reverse, Northeast ↗ diagonals)
        if i+3 < len(lines) and j-3 >= 0:
            letter_group = lines[i][j] + lines[i+1][j-1] + lines[i+2][j-2] + lines[i+3][j-3]
            if letter_group == "XMAS" or letter_group == "SAMX":
                total_XMAS_occurances += 1

print(f"total_XMAS_occurances: {total_XMAS_occurances}")


# Part 2

# could either 
# 1. check diagonals for 2 MAS's
# 2. use a 3x3 sliding-window type approach over the 2d array

total_X_MAS_occurances = 0

for i in range(len(lines) - 2): # i = rows, up and down
    for j in range(len(lines[i]) - 2): # j = columns, across left and right

        if lines[i+1][j+1] == 'A' and \
            ((lines[i][j]=="M" and lines[i][j+2]=="M" and lines[i+2][j]=="S" and lines[i+2][j+2]=="S") or
            (lines[i][j]=="M" and lines[i][j+2]=="S" and lines[i+2][j]=="M" and lines[i+2][j+2]=="S") or
            (lines[i][j]=="S" and lines[i][j+2]=="S" and lines[i+2][j]=="M" and lines[i+2][j+2]=="M") or
            (lines[i][j]=="S" and lines[i][j+2]=="M" and lines[i+2][j]=="S" and lines[i+2][j+2]=="M")):
            total_X_MAS_occurances += 1

print(f"total_X_MAS_occurances: {total_X_MAS_occurances}")
