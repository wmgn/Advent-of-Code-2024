import re

with open("Day3data.txt") as file:
    input = file.read()

matches = re.findall('mul\\((\\d+),(\\d+)\\)', input)

#print(matches)

total = 0
for match in matches:
    total += int(match[0]) * int(match[1])

print(f"total: {total}")



# Part 2
matches_2 = re.findall("mul\\((\\d+),(\\d+)\\)|(don't)\\(\\)|(do)\\(\\)", input)

print(matches_2)

total_2 = 0
isDo = True
for match in matches_2:
    if match[2] == "don't":
        isDo = False
        continue
    if match[3] == "do":
        isDo = True
        continue

    if isDo:
        total_2 += int(match[0]) * int(match[1])

print(f"part 2 total: {total_2}")
