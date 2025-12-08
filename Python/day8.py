import aocd, sys

inp = r"""162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689"""
n_connections = 10

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=8, year=2025)
    n_connections = 1000

### BEGIN SOLUTION

from collections import defaultdict
from itertools import combinations
from heapq import heappush, heappop
from math import inf, prod, sqrt

part1 = part2 = 0
boxes = list(map(lambda line: tuple(map(int, line.split(","))), inp.split("\n")))
pairs = []
for b1, b2 in combinations(boxes, 2):
    dist = sqrt(sum(map(lambda x, y: (y - x)**2, b1, b2)))
    heappush(pairs, (dist, b1, b2))

neighbors = defaultdict(set)
for _ in range(n_connections):
    d, b1, b2 = heappop(pairs)
    neighbors[b1].add(b2)
    neighbors[b2].add(b1)

networks = []
seen = set()
for box in boxes:
    if box in seen:
        continue
    seen.add(box)
    network = set()
    q = {box}
    while q:
        cur = q.pop()
        network |= neighbors[cur]
        q |= neighbors[cur] - seen
        seen |= neighbors[cur]
    networks.append(network)

part1 = prod(sorted(list(map(len, networks)))[-3:])


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=8, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=8, year=2025)
