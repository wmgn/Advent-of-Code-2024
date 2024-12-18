
with open("Day5_page_ordering_rules.txt") as file:
    page_ordering_rules = file.readlines()

with open("Day5_pages.txt") as file:
    pages = file.readlines()

page_ordering_rules = [line.strip() for line in page_ordering_rules] # make sure to get rid of whitespace, like /n

pages = [line.strip() for line in pages] # make sure to get rid of whitespace, like /n
pages = [[int(num) for num in page.split(",")] for page in pages] # turn strings of numbers "1,2,3" into arrays of int [1,2,3]

rules_arr = [[] for i in range(100)] # used as a double arr where rules_arr[Y] = [X1,X2,X3,...] which contains all possible X for all rules X|Y
for rule in page_ordering_rules:
    x = int(rule[0:2])
    y = int(rule[3:5])
    rules_arr[y].append(x)



def check_conforms_to_rules(page):
    for i in range(len(page)):
        y = page[i]
        for x in rules_arr[y]: # for every rule of X must come before Y, where Y=curr num in page
            for j in range(i+1,len(page)): # check if X is in the rest of the page's numbers
                if page[j] == x:
                    return False
    return True



middle_numbers_total_part1 = 0
for page in pages:
    if check_conforms_to_rules(page):
        middle_numbers_total_part1 += int(page[int(len(page)/2)])

print(f"middle_numbers_total_part1: {middle_numbers_total_part1}")




# Part 2

def check_conforms_to_rules_and_fix(arr_to_check: list[int]):
    doneFlag = False
    breakFlag = 0
    changedArr = False

    while not doneFlag:
        for i in range(breakFlag, len(arr_to_check)):
            if breakFlag: break
            y = page[i]
            for x in rules_arr[y]: # for every rule of X must come before Y, where Y=curr num in page
                if breakFlag: break
                for j in range(i+1,len(arr_to_check)):
                    if breakFlag: break
                    if arr_to_check[j] == x:
                        changedArr = True
                        arr_to_check.pop(j)
                        arr_to_check.insert(i,x)
                        breakFlag = i-1
        if breakFlag:
            breakFlag = 0
        else:
            doneFlag = True
    
    if changedArr:
        return True, arr_to_check
    else:
        return False, None
    

middle_numbers_total_part2 = 0
for page in pages:
    changedArr, page = check_conforms_to_rules_and_fix(page)
    if changedArr:
        middle_numbers_total_part2 += int(page[int(len(page)/2)])
        
print(f"middle_numbers_total_part2: {middle_numbers_total_part2}")







### Old Code, didn't end up working

'''
class Node:
    def __init__(self,val=None):
        self.value = val
        self.children = []

root_nodes = [] # could rename to forest
all_nodes = []

def search_tree(node:Node, value:int):
    if node is None:
        return None

    if node.value == value:
        return node
    
    for child in node.children:
        result = search_tree(child, value)
        if result:
            return result
        
    return None

for rule in page_ordering_rules:
    #print(f"Rule: {rule}")

    x = int(rule[0:2])
    y = int(rule[3:5])

    x_node = None
    y_node = None
    
    for node in all_nodes:
        if node.value == x:
            x_node = node
            continue
        if node.value == y:
            y_node = node
            continue
        if x_node is not None and y_node is not None:
            break

    if x_node is None:
        print(f"x_node {x} was None, creating x_node, appending to all_nodes")
        x_node = Node(x)
        all_nodes.append(x_node)
        root_nodes.append(x_node)
    if y_node is None:
        #print(f"y_node {y} was None, creating y_node, appending to all_nodes")
        y_node = Node(y)
        all_nodes.append(y_node)
    elif y_node in root_nodes:
        root_nodes.remove(y_node)

    x_node.children.append(y_node) 

    if x_node is None and y_node is None:
        x_node.children.append(y_node)
        root_nodes.append(x_node)
    elif x_node is None:
        x_node.children.append(y_node)
        root_nodes.append(x_node)
        if y_node in root_nodes:
            root_nodes.remove(y_node)
    elif y_node is None:
        x_node.children.append(y_node)
    else:
        x_node.children.append(y_node)
        if y_node in root_nodes:
            root_nodes.remove(y_node)


#all_nodes.sort(key=lambda node: node.value)
print(f"root_nodes: {[node.value for node in root_nodes]}" )
print(f"all_nodes (len: {len(all_nodes)}): {[node.value for node in all_nodes]}" )

'''

''' # for checking if rules are cyclical, (they seem to be)
all_x = {0}
all_y = {0}
for rule in page_ordering_rules:
    all_x.add(x)
    all_y.add(y)
print(f"all_x (len: {len(all_x)}): {all_x}")
print(f"all_y (len: {len(all_y)}): {all_y}")
print(f"difference x - y: {all_x.difference(all_y)}")'''

'''for root in root_nodes:
        if x_node is None:
            x_node = search_tree(root, x)
        if y_node is None:
            y_node = search_tree(root, y)
        if x_node is not None and y_node is not None:
            break'''

'''#old code that doesnt work
x_idx = -1
    y_idx = -1
    try:
        x_idx = priorities_list.index(x)
    except ValueError:
        pass
    try:
        y_idx = priorities_list.index(y)
    except ValueError:
        pass

    if x_idx==-1 and y_idx==-1:
        priorities_list.append(x)
        priorities_list.append(y)
    elif x_idx==-1:
        priorities_list.insert(y_idx, x)
    elif y_idx==-1:
        priorities_list.append(y)
    elif y_idx < x_idx: # x and y both are in list already, and x is not before y
        priorities_list.pop(x_idx)
        priorities_list.insert(y_idx, x) # doing this will probably break other rules'''