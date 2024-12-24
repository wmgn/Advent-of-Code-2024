from collections import defaultdict 
from itertools import combinations

with open("Day23.in") as file:
    input = [line.rstrip().split("-") for line in file.readlines()] # input is a 2d arr, e.g. [['ab', 'cd'], ['ut', 'ts'], ['dm', 'vh']]
#print(input)


connections = defaultdict(set)
for a,b in input:
    connections[a].add(b) # e.g. 'wx'=>['yz']
    connections[b].add(a) # e.g. 'yz'=>['wx']
#print(f"connections: {connections}")


networks = set()
for a,b in combinations(connections.keys(), 2):
    intersection = connections[a].intersection(connections[b])
    #print(intersection)

    if len(intersection) == 11:
        networks.add(tuple(sorted([a,b,*intersection])))
print(f"networks: {networks}")
print(f"len(networks): {len(networks)}")


# CHECKING
for network in networks: # e.g. network = ('bd', 'bu', 'dv', 'gl', 'qc', 'rn', 'so', 'tm', 'wf', 'yl', 'ys', 'ze', 'zr')
    if all(d in connections[computer] for d in network for computer in network if d != computer):
        print(*network, sep=",")
        break












''' # solution from u/4HbQ
# computers = connections.keys() # could do this line
networks = [{c} for c in connections.keys()] # create an array of singleton sets
for n in networks:
    for c in connections.keys():
        if all(d in connections[c] for d in n): n.add(c)
print(*sorted(max(networks, key=len)), sep=',')
quit()


# Old code for brute force solution attempt that might have worked, but would've taken possibly years to execute
combos_tried = 0
finalCombo = []
for i in range(4, 13):
    print(f"trying subset size i = {i}")

    for combo in combinations(connections.keys(), i):
        combos_tried += 1
        if combos_tried % 1000000 == 0:
            print(f"combos_tried: {combos_tried} / ")
        #print(f"    trying combo: {combo}")

        failFlag = False
        for a,b in combinations(combo, 2):
            if b not in connections[a]:
                failFlag = True
                break
        if failFlag:
            continue
        else: # succeeded
            finalCombo = combo
            break
        #print(combo)

        #print(combination) 
        #quit()
        #if c2 in connections[c1] and c3 in connections[c1] and c3 in connections[c2]:
        #    combos_size_3.append((c1,c2,c3))

finalComboSorted = sorted(finalCombo)
print(len(finalComboSorted))
print(finalComboSorted)
print(",".join(finalComboSorted))
'''


### Brainstorming Solutions
'''
# option 2
# graph
# find cycle works because a fully connected graph of size 3 is a cycle, even if it wouldn't be for size 4 or higher
# detect complete/connected subgraphs(s) in undirected graph (each complete/connected subgraph of size 3) -- what algorithm? Googled: Bron–Kerbosch algorithm
# adjacency list
# adjacency matrix

# option 3
# sets ? use sets that have the greatest intersections with eachother?
'''

# option 1
# python dict (hashmap), where each key,value pair is an computer and an array of all the other computers its connected to
# could then brute force check every possible permutation/combination group of 3 unique computers, searching to see if those connections exist
# shortcomings: this method stores 2x data necessary. stores key,value pairs 'ab'=>['cd'] and 'cd'=>['ab'], redundant, since connections are not directional.

# Part 2. Find the largest set of computers that are all connected to each other.

# instead of trying to come up with every possible combination,
# use the connections that are already there, to try to create/assemble a connected set
# every single key has 13 connections
'''keys_and_sizes = []
for tup in connections.items():
    keys_and_sizes.append((tup[0],len(tup[1])))
print(keys_and_sizes)'''