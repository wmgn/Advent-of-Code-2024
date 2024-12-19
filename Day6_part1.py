with open("Day6.in") as file:
    map = [[s for s in str.strip()] for str in file.readlines()]

coords = [None,None] #i,j
# find the one "^" character
for i in range(len(map)):
    if coords[0] is not None:
        break
    for j in range(len(map[0])):
        if map[i][j] == "^":
            coords = [i,j]
            break
#print(f"starting coord: {coords}")

up = [-1,0]
right = [0,1]
down = [1,0]
left = [0,-1]
dirs = [up,right,down,left]
dir = 0

try:
    while True:
        next_coord = [coords[0] + dirs[dir][0], coords[1] + dirs[dir][1]]
        #print(next_coord)
        if(map[next_coord[0]][next_coord[1]]) == "#":
            dir = (dir+1)%4 #increment dir
        else:
            map[coords[0]][coords[1]] = "X"
            coords = next_coord
except IndexError:
    map[coords[0]][coords[1]] = "X"


#with open("Day6.out", "w") as file:
#    file.writelines(["".join(arr)+"\n" for arr in map])


total_distinct_positions = sum(arr.count("X") for arr in map)
print(total_distinct_positions)



# Part 2
