import aocd, sys

inp = r"""7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=9, year=2025)

### BEGIN SOLUTION

from itertools import combinations, pairwise, product

rectangles = sorted(((abs(t1[0] - t2[0]) + 1) * (abs(t1[1] - t2[1]) + 1), t1, t2)
                    for t1, t2 in combinations(map(lambda line:tuple(map(int, line.split(","))), inp.split("\n")), 2))
part1 = rectangles[-1][0]

def range_incl(x, y):
    return range(min(x, y), max(x, y) + 1)

corners = [tuple(map(int, line.split(","))) for line in inp.split("\n")]
reds = set()
for r1, r2 in pairwise(corners + [corners[0]]):
    reds |= set(product(range_incl(r1[0], r2[0]), range_incl(r1[1], r2[1])))
corners = set(corners)

part1 = part2 = 0
for i, (t1, t2) in enumerate(combinations(corners, 2)):
    xs = sorted([t1[0], t2[0]])
    ys = sorted([t1[1], t2[1]])
    n_tiles = (xs[1] - xs[0] + 1) * (ys[1] - ys[0] + 1)
    part1 = max(part1, n_tiles)

    if n_tiles <= part2:
        continue

    for r in reds:
        if xs[0] < r[0] < xs[1] and ys[0] < r[1] < ys[1]:
            break
    else:
        part2 = max(part2, n_tiles)

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=9, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=9, year=2025)
