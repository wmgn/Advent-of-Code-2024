with open("Day08.in") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]

chars_dict = {} # a dict of every unique char pointing to a list of grid coords where that char appears
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != ".":
            if char not in chars_dict:
                chars_dict[char] = []
            chars_dict[char].append((i,j))


unique_antinode_locations = set() #of 2d coords [i,j]
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
                    unique_antinode_locations.add(node)

    #print(f"\nunique_antinode_locations: {unique_antinode_locations}")
    #quit()

print(f"num of unique_antinode_locations: {len(unique_antinode_locations)}")




# Part 2
#print("\n\n\n----- part 2")

unique_antinode_locations_part2 = set() #of 2d coords [i,j]
for char in chars_dict:
    node_coords_arr = chars_dict[char]
    #print(f"node_coords_arr: {node_coords_arr}")

    if len(node_coords_arr) > 1:
        for node_coord in node_coords_arr:
            unique_antinode_locations_part2.add(node_coord)

    for i, node1 in enumerate(node_coords_arr):
        for j, node2 in enumerate(node_coords_arr[i+1:]): #iterate over every unique pair of 2 coords
            i1,j1 = node1
            i2,j2 = node2
            #print(f"node1_coords: ({i1},{j1}),   node2_coords: ({i2},{j2})")
            
            antinode1 = (i1+(i1-i2), j1+(j1-j2))
            #print(f"   antinode1: {antinode1}")
            while( 0 <= antinode1[0] and antinode1[0] < len(lines)
                    and 0 <= antinode1[1] and antinode1[1] < len(lines[0]) ): # ensure antinode indices are inbounds
                unique_antinode_locations_part2.add(antinode1)
                #print(f"   unique_antinode_locations_part2 added antinode1")
                antinode1 = (antinode1[0]+(i1-i2), antinode1[1]+(j1-j2))
                #print(f"   antinode1: {antinode1}")

            antinode2 = (i2+(i2-i1), j2+(j2-j1))
            #print(f"   antinode2: {antinode2}")
            while( 0 <= antinode2[0] and antinode2[0] < len(lines)
                    and 0 <= antinode2[1] and antinode2[1] < len(lines[0]) ): # ensure antinode indices are inbounds
                unique_antinode_locations_part2.add(antinode2)
                #print(f"   unique_antinode_locations_part2 added antinode2")
                antinode2 = (antinode2[0]+(i2-i1), antinode2[1]+(j2-j1))
                #print(f"   antinode2: {antinode2}")
                
    #quit()
    #print(f"\n unique_antinode_locations_part2: {unique_antinode_locations_part2}")
    #quit()

print(f"num of unique_antinode_locations_part2: {len(unique_antinode_locations_part2)}")

