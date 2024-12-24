from collections import defaultdict 
from itertools import combinations

with open("Day23.in") as file:
    input = [line.rstrip().split("-") for line in file.readlines()] # input is a 2d arr, e.g. [['ab', 'cd'], ['ut', 'ts'], ['dm', 'vh']]

#print(input)

'''
# option 2
# graph
# detect cycle(s) in undirected graph (each cycle of size 3) -- what algorithm? 

# option 3
# sets ?
'''

# option 1
# python dict (hashmap), where each key,value pair is an computer and an array of all the other computers its connected to
# could then brute force check every possible permutation/combination group of 3 unique computers, searching to see if those connections exist
# shortcomings: this method stores 2x data necessary. stores key,value pairs 'ab'=>['cd'] and 'cd'=>['ab'], redundant, since connections are not directional.

connections = defaultdict(list)

# for 1d arr, e.g. ['ab', 'cd'], in 2d arr
for c1,c2 in input:
    # e.g. 'ab','cd'
    connections[c1].append(c2)
    connections[c2].append(c1)
#print(f"connections: {connections}")



combos_size_3 = [] 
for c1,c2,c3 in combinations(connections.keys(), 3):
    #print(combination)
    #quit()
    if c2 in connections[c1] and c3 in connections[c1] and c3 in connections[c2]:
        combos_size_3.append((c1,c2,c3))
#print(f"combos_size_3: {combos_size_3}")



combos_size_3_begin_with_t = []
for c1,c2,c3 in combos_size_3:
    if c1[0] == "t" or c2[0] == "t" or c3[0] == "t":
        combos_size_3_begin_with_t.append((c1,c2,c3))
#print(f"combos_size_3_begin_with_t: {combos_size_3_begin_with_t}")

print(len(combos_size_3_begin_with_t))

# first answer attempt: 196. Too Low.
# Problem I didn't notice: I was only building my hashmap with 'ab'=>'cd', but I needed to also manually add in 'cd'=>'ab'


# Part 2. Find the largest set of computers that are all connected to each other. Largest cycle in the graph.

# Option 1. Brute force
# Doing option 1 here:
for i in range(len(connections.keys()), 0, -1):
    for combo in combinations(connections.keys(), i):
        print(combo)
        #print(combination)
        #quit()
        #if c2 in connections[c1] and c3 in connections[c1] and c3 in connections[c2]:
        #    combos_size_3.append((c1,c2,c3))


# Option 2. Something smarter.