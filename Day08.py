from collections import defaultdict # learned about defaultdict, using type list, avoids KeyErrors by providing a default value for the key that does not exist

with open("Day08.in") as file:
    lines = [line.rstrip() for line in file]

chars_dict = defaultdict(list) # a dict of every unique char pointing to a list of grid coords where that char appears
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != ".":
            chars_dict[char].append((i,j))


antinode_set = set() #of 2d coords [i,j]
for char in chars_dict:
    node_coords_arr = chars_dict[char]
    #print(node_coords_arr)

    for i in range(len(node_coords_arr)):
        for j in range(i+1,len(node_coords_arr)): #iterate over every unique pair of 2 coords
            i1,j1 = node_coords_arr[i]
            i2,j2 = node_coords_arr[j]
            #print(f"node1_coords: ({i1},{j1}),   node2_coords: ({i2},{j2})")

            antinode1_coords = (i1+(i1-i2), j1+(j1-j2))
            antinode2_coords = (i2+(i2-i1), j2+(j2-j1))
            #print(f"   antinode1_coords: {antinode1_coords},   antinode2_coords: {antinode2_coords}")

            # check if antinode indices are inbounds or not
            for node in antinode1_coords,antinode2_coords:
                if ( 0 <= node[0] and node[0] < len(lines) 
                    and 0 <= node[1] and node[1] < len(lines[0]) ):
                    antinode_set.add(node)

    #print(f"\nantinode_set: {antinode_set}")
    #quit()

print(f"num of antinode_set: {len(antinode_set)}")




# Part 2
#print("\n\n\n----- part 2")

antinode_set_part2 = set() #of 2d coords [i,j]
for char in chars_dict:
    node_coords_arr = chars_dict[char]
    #print(f"node_coords_arr: {node_coords_arr}")

    if len(node_coords_arr) > 1:
        for node_coord in node_coords_arr:
            antinode_set_part2.add(node_coord)

    for i, node1 in enumerate(node_coords_arr):
        for j, node2 in enumerate(node_coords_arr[i+1:]): #iterate over every unique pair of 2 coords
            i1,j1 = node1
            i2,j2 = node2
            #print(f"node1_coords: ({i1},{j1}),   node2_coords: ({i2},{j2})")
            
            antinode1 = (i1+(i1-i2), j1+(j1-j2))
            #print(f"   antinode1: {antinode1}")
            while( 0 <= antinode1[0] and antinode1[0] < len(lines)
                    and 0 <= antinode1[1] and antinode1[1] < len(lines[0]) ): # ensure antinode indices are inbounds
                antinode_set_part2.add(antinode1)
                #print(f"   antinode_set_part2 added antinode1")
                antinode1 = (antinode1[0]+(i1-i2), antinode1[1]+(j1-j2))
                #print(f"   antinode1: {antinode1}")

            antinode2 = (i2+(i2-i1), j2+(j2-j1))
            #print(f"   antinode2: {antinode2}")
            while( 0 <= antinode2[0] and antinode2[0] < len(lines)
                    and 0 <= antinode2[1] and antinode2[1] < len(lines[0]) ): # ensure antinode indices are inbounds
                antinode_set_part2.add(antinode2)
                #print(f"   antinode_set_part2 added antinode2")
                antinode2 = (antinode2[0]+(i2-i1), antinode2[1]+(j2-j1))
                #print(f"   antinode2: {antinode2}")
                
    #quit()
    #print(f"\n antinode_set_part2: {antinode_set_part2}")
    #quit()

print(f"num of antinode_set_part2: {len(antinode_set_part2)}")

