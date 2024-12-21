with open("Day08.in") as file:
    lines = file.readlines()

lines = [line.strip() for line in lines]
#print(lines)

'''unique_char_set = set()
for line in lines:
    for char in line:
        unique_char_set.add(char)
unique_char_set.remove(".")
#print(unique_char_set)
'''

chars_dict = {}
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char != ".":
            if char not in chars_dict:
                chars_dict[char] = []
            chars_dict[char].append((i,j))


unique_antinode_locations = set() #of 2d coords [i,j]

for char in chars_dict:
    #print(chars_dict[char])
    #quit()
    existing_node_locations = chars_dict[char]

    '''
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char != ".":
                existing_node_locations.append((i,j))'''
    print(existing_node_locations)

    for i in range(len(existing_node_locations)):
        for j in range(i+1,len(existing_node_locations)):
            i1,j1 = existing_node_locations[i]
            i2,j2 = existing_node_locations[j]
            print(f"node1_coords: ({i1},{j1}),   node2_coords: ({i2},{j2})")

            antinode1_coords = (i1+(i1-i2), j1+(j1-j2))
            antinode2_coords = (i2+(i2-i1), j2+(j2-j1))
            print(f"   antinode1_coords: {antinode1_coords},   antinode2_coords: {antinode2_coords}")


            for node in antinode1_coords,antinode2_coords:
                # check if antinode indices are inbounds or not
                if ( 0 <= node[0] and node[0] < len(lines) 
                    and 0 <= node[1] and node[1] < len(lines[0]) ):
                    unique_antinode_locations.add(node)

    #print(f"\nunique_antinode_locations: {unique_antinode_locations}")
    #quit()

'''
for char in unique_char_set:
    new_lines = []
    for line in lines:
        new_line = ""
        for c in line:
            if c == char:
                new_line += c
            else:
                new_line += "."
        new_lines.append(new_line)
    find_unique_antinode_locations(new_lines)
    #print(new_lines)
'''

print(len(unique_antinode_locations))