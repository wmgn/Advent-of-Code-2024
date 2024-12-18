
with open("Day5_page_ordering_rules.txt") as file:
    page_ordering_rules = file.readlines()

with open("Day5_pages.txt") as file:
    pages = file.readlines()

page_ordering_rules = [line.strip() for line in page_ordering_rules] # make sure to get rid of whitespace, like /n
pages = [line.strip() for line in pages] # make sure to get rid of whitespace, like /n

#print(pages)

# start by identifying which updates are already in the right order, conform to the rules already
# find all the MIDDLE page numbers and add them up

def check_conforms_to_rules(arr_to_check):
    #print(f"arr_to_check: {arr_to_check}")

    for i, num in enumerate(arr_to_check):
        #print(f"for i: {i}, num: {num}")
        for rule in page_ordering_rules:
            x = int(rule[0:2])
            y = int(rule[3:5])
            if y == num:
                for j in range(i+1,len(arr_to_check)):
                    if arr_to_check[j] == x:
                        #print(f"for rule: {rule}, \n num == y ({y})")
                        #print(f"for j: {j}, ")
                        #print(f"arr_to_check[j] ({arr_to_check[j]}) == x ({x}), return False")
                        return False

    #print(f"check_conforms_to_rules returning True!!!!")
    return True

middle_numbers_total = 0

for page in pages:
    page = [int(num) for num in page.split(",")]
    #print(f"---for page: {page}")
    if check_conforms_to_rules(page):
        #print(f"page CONFORMS: "); print(page)
        #print(f"page[len(page)/2]: {page[int(len(page)/2)]}")
        #print(f"middle_numbers_total += page[int(len(page)/2)]: {page[int(len(page)/2)]}")
        middle_numbers_total += int(page[int(len(page)/2)])

print(f"middle_numbers_total: {middle_numbers_total}")





# Part 2

def check_conforms_to_rules_and_fix(arr_to_check: list[int]):
    #print(f"arr_to_check: {arr_to_check}")
    doneFlag = False
    breakFlag = 0
    changedArr = False

    while not doneFlag:
        for i, num in enumerate(arr_to_check):
            if breakFlag: break
            #print(f"for i: {i}, num: {num}")
            for rule in page_ordering_rules:
                if breakFlag: break
                x = int(rule[0:2])
                y = int(rule[3:5])
                if y == num:
                    for j in range(i+1,len(arr_to_check)):
                        if breakFlag: break
                        if arr_to_check[j] == x:
                            changedArr = True
                            arr_to_check.pop(j)
                            arr_to_check.insert(i,x)
                            breakFlag = i-1
                            #print(f"for rule: {rule}, \n num == y ({y})")
                            #print(f"for j: {j}, ")
                            #print(f"arr_to_check[j] ({arr_to_check[j]}) == x ({x}), return False")
                            #return False
                            
        if breakFlag:
            breakFlag = 0
        else:
            doneFlag = True
    
    if changedArr:
        return True, arr_to_check
    else:
        return False, None
    #print(f"check_conforms_to_rules returning True!!!!")
    #return True

middle_numbers_total_part2 = 0

for page in pages:
    page = [int(num) for num in page.split(",")]

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