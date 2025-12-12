import aocd, sys

inp = r"""0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=12, year=2025)

### BEGIN SOLUTION

from math import prod

part1 = part2 = 0
*shapes, regions = inp.split("\n\n")
shape_sizes = [shape.count("#") for shape in shapes]
for region in regions.split("\n"):
    wl, *quantities = region.split(" ")
    region_size = prod(map(int, wl[:-1].split("x")))
    min_packing = sum(prod(t) for t in zip(map(int, quantities), shape_sizes))
    max_packing = sum(q * 9 for q in map(int, quantities))
    part1 += max_packing <= region_size
    

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=12, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=12, year=2025)
