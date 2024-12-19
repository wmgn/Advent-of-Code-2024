### Part 1 - How many designs are possible to be created with the available towel patterns?
from functools import cache

# Process and format Input
towel_patterns, designs = open('Day19.in').read().split("\n\n")
towel_patterns, designs = towel_patterns.split(', '), designs.split("\n")

@cache
def check_design_possible(design:str) -> bool:
    """Recursively checks if a design can be constructed using the towel patterns."""
    
    #print(f"Curr check_design_possible on design: {design}")

    if design == "":
        return True
    
    for pattern in towel_patterns: # for EVERY single pattern possible
        if design.startswith(pattern):
            if check_design_possible(design[len(pattern):]): # chop
                return True

    return False
    

total_designs_possible = sum(check_design_possible(design) for design in designs)
print(f"total_designs_possible: {total_designs_possible}")


# First answer was 317, too low. But Correct answer for someone else.
# Implemented memoization, got 360

# --- Part Two ---

@cache
def check_design_ways(design: str) -> int:
    """Returns the total number of ways to construct a design."""
    if design == "":
        return 1
    
    total_ways = 0
    for pattern in towel_patterns:
        if design.startswith(pattern):
            total_ways += check_design_ways(design[len(pattern):])
    
    return total_ways

total_design_ways = sum(check_design_ways(design) for design in designs)
print(f"total_design_ways: {total_design_ways}")




'''
great solution from r/4HbQ:

def count(d):
    return d == '' or sum(count(d.removeprefix(p))
        for p in P.split(', ') if d.startswith(p))


results = list(map(count, designs))

for type in bool, int:
    print(sum(map(type, results)))
'''

