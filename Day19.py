### Task/Problem Info/Notes
# arrange towels
# Every towel marked with a pattern of colored stripes
# only a few patterns
# for any particular pattern, can have as many towels as you want
# Each stripe can be white (w), blue (u), black (b), red (r), or green (g).

# E.g.
# towel with pattern ggr has a green stripe, a green stripe, and then a red stripe, in that order
# You can't reverse a pattern by flipping a towel upside-down

# list of designs
# can use any towels you want
# all of the towels' stripes must exactly match the desired design

# to display the design rgrgr, you could use:
# two rg towels and then an r towel, 
# an rgr towel and then a gr towel, 
# or even a single massive rgrgr towel (assuming such towel patterns were actually available).

# To start, collect together all of the available towel patterns and the list of desired designs (your puzzle input).



### Part 1 - How many designs are possible to be created with the available towel patterns?

# Process and format Input
with open("Day19.in") as file:
    towel_patterns, designs = file.read().split("\n\n")

towel_patterns = towel_patterns.split(", ")
designs = designs.split("\n")


from functools import lru_cache

@lru_cache(None)
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