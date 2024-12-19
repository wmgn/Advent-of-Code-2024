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
start_coord = coords

        # up,   right,  down,  left
dirs = [(-1,0), (0,1), (1,0), (0,-1)]
dir = 0

coords_on_path = set()

while True:
    next_coord = [coords[0] + dirs[dir][0], coords[1] + dirs[dir][1]]
    if (0 <= next_coord[0] < len(map) and
        0 <= next_coord[1] < len(map[0])):
        #print(next_coord)
        if(map[next_coord[0]][next_coord[1]]) == "#":
            dir = (dir+1)%4 #increment dir
        else:
            coords_on_path.add((coords[0],coords[1]))
            coords = next_coord
    else:
        coords_on_path.add((coords[0],coords[1]))
        break

#The new obstruction can't be placed at the guard's starting position - the guard is there right now and would notice
print(f"len(coords_on_path): {len(coords_on_path)} (answer to Part 1)")
coords_on_path.remove((start_coord[0],start_coord[1])) 
#print(f"len(coords_on_path): {len(coords_on_path)}")

loops_found_count = 0

for coord in coords_on_path:
    #print(f"Checking coord: {coord}")
    i = coord[0]
    j = coord[1]

    store_old = map[i][j]
    if store_old != ".": # shouldnt need this anymore
        continue
    map[i][j] = "#"

    coords = start_coord
    dir = 0
    visited_states = set() # State is (position, direction), e.g. (coords[0], coords[1], dir)
    while True:
        next_coord = [coords[0] + dirs[dir][0], coords[1] + dirs[dir][1]]
        if (0 <= next_coord[0] < len(map) and
            0 <= next_coord[1] < len(map[0])):
            if(map[next_coord[0]][next_coord[1]]) == "#":
                state = (coords[0], coords[1], dir)
                if state in visited_states:
                    loops_found_count += 1
                    break
                else:
                    visited_states.add(state)
                dir = (dir+1)%4 # guard turns 90 degrees
            else:
                coords = next_coord
        else:
            break


    map[i][j] = store_old


print(f"loops_found_count: {loops_found_count} (answer to Part 2)")





# Old code, didn't end up working 
'''

for i in range(len(coords_preceding_a_turn)-3):
    t1 = coords_preceding_a_turn[i]     # turn 1 coords
    t2 = coords_preceding_a_turn[i+1]   # etc...
    t3 = coords_preceding_a_turn[i+2]
    t4 = coords_preceding_a_turn[i+3]
    print(f"Coords, t1: {t1}, t2: {t2}, t3: {t3}, t4: {t4}")

    # we want to compare t3, t4, and t1, to see if t4 overshoots t1 and is capable of making a loop
    # t4 will have 1 coord (i or j) in common with t3, with the other being different
    iOrj = 0            # we will compare i coordinate
    if t3[0] == t4[0]:  # but if the i coordinates are the same
        iOrj = 1        # we will compare j coordinate

    print(f"iOrj = {iOrj}")

    t3_t4_span = sorted([t3[iOrj],t4[iOrj]]) # from low to high
    print(f"t3_t4_span = {t3_t4_span}") # from low to high

    if t1[iOrj] > t3_t4_span[0] and t1[iOrj] <= t3_t4_span[1]:
        #t1 is inside the iOrj span of t3 and t4, which means that it is possible it can make a loop
        iOrj = abs(iOrj-1)
        lower = min(t1[iOrj], t4[iOrj])
        higher = max(t1[iOrj], t4[iOrj])
        print(f"iOrj = {iOrj}")
        print(f"lower = {lower}")
        print(f"higher = {higher}")
        breakFlag = False
        for k in range(lower,higher+1):
            if iOrj == 0:
                print(f"checking map[k][t1[1]] == '#', map[{k}][{t1[1]}]: {map[k][t1[1]]}")
                if map[k][t1[1]] == "#":
                    breakFlag = True
                    break
            else:
                print(f"checking map[t1[0]][k] == '#', map[{t1[0]}][{k}]: {map[t1[0]][k]}")
                if map[t1[0]][k] == "#":
                    breakFlag = True
                    break
        if not breakFlag:
            loops_found_count += 1
            print("loops_found_count +1")
         
    else: # otherwise, it cannot make a loop, continue on
        continue

print(f"loops_found_count: {loops_found_count}")
'''