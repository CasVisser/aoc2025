import aocd, sys

inp = r"""L68
L30
R48
L5
R60
L55
L1
L99
R14
L82"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=1, year=2025)

### BEGIN SOLUTION

part1 = part2 = 0

dial = 50
for direction, amount in map(lambda x: (x[0], int(x[1:])), inp.split("\n")):
    if direction == "R":
        part2 += (dial + amount) // 100
    if direction == "L":
        part2 += ((100 - dial) % 100 + amount) // 100
    dial = (dial + amount * (1 if direction == "R" else -1)) % 100
    part1 += 1 if dial == 0 else 0

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=1, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=1, year=2025)
