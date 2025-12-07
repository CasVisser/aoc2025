import aocd, sys

inp = r""".......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
..............."""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=7, year=2025)

### BEGIN SOLUTION

from collections import defaultdict

grid = {complex(x, y): c for y, line in enumerate(inp.split("\n"))
                         for x, c in enumerate(line)}

part2 = 0
hit = set()
beams = defaultdict(int)
beams[inp.find("S") + 0j] = 1
for xy in grid:
    if beams[xy] == 0:
        continue
    succ = xy + 1j
    if succ not in grid:
        part2 += beams[xy]
        continue
    if grid[succ] == ".":
        beams[succ] += beams[xy]
        continue
    hit.add(succ)
    beams[succ + 1] += beams[xy]
    beams[succ - 1] += beams[xy]

part1 = len(hit)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=7, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=7, year=2025)
