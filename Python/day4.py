import aocd, sys

inp = r"""..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@."""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=4, year=2025)

### BEGIN SOLUTION

part1 = part2 = 0
grid = {complex(x, y): c 
        for y, line in enumerate(inp.split("\n"))
        for x, c in enumerate(line)
        if c == "@"}
directions = [1, 1 + 1j, 1j, -1 + 1j, -1, -1 - 1j, -1j, 1 - 1j] 
neighbors = lambda xy: [xy + d for d in directions if xy + d in grid]

while True:
    removable = [xy for xy in grid if len(neighbors(xy)) < 4]

    if len(removable) == 0:
        break
    for xy in removable:
        del grid[xy]

    if part1 == 0:
        part1 = len(removable)
    part2 += len(removable)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=4, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=4, year=2025)
