import aocd, sys

inp = r"""[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=10, year=2025)

### BEGIN SOLUTION

from collections import defaultdict
from itertools import combinations, starmap
from functools import cache
from math import inf
from z3 import *

sub = lambda t1, t2: tuple(starmap(lambda x, y: x - y, zip(t1, t2)))

part1 = part2 = 0
for i, line in enumerate(inp.split("\n")):
    lights, *buttons, joltages = line.split(" ")
    lights_target = tuple(1 if c == "#" else 0 for c in lights[1:-1])
    joltage_target = tuple(map(int, joltages[1:-1].split(",")))
    actions = [
        tuple(1 if n in map(int, button[1:-1].split(",")) else 0 for n in range(len(lights_target))) 
        for button in buttons
    ]

    part1 += min(n for n in range(1, len(actions) + 1)
                 for comb in combinations(actions, n)
                 if tuple(map(lambda *a: sum(a) % 2, *comb)) == lights_target)

    s = Solver()
    presses = [Int(f"p{i}") for i in range(len(actions))]
    s.add(p >= 0 for p in presses)

    joltages = [Int(f"j{i}") for i in range(len(joltage_target))]
    s.add(joltage == target for joltage, target in zip(joltages, joltage_target))

    s.add(joltage == Sum([p for p, action in zip(presses, actions) if action[i]]) 
          for i, joltage in enumerate(joltages))

    while s.check() == sat:
        m = s.model()
        n_presses = sum(m[p].as_long() for p in presses)
        s.push()
        s.add(Sum(presses) < n_presses)

    part2 += n_presses

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=10, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=10, year=2025)
