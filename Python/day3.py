import aocd, sys

inp = r"""987654321111111
811111111111119
234234234234278
818181911112111"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=3, year=2025)

### BEGIN SOLUTION

part1 = part2 = 0

for line in inp.split("\n"):
    index = -1
    acc = 0
    for remaining_digits in range(12, 0, -1):
        index = max(range(index + 1, len(line) - remaining_digits + 1), key=line.__getitem__)
        part2 += int(line[index]) * 10 ** (remaining_digits - 1)

    i1 = max(range(len(line) - 1), key=line.__getitem__)
    i2 = max(range(i1 + 1, len(line)), key=line.__getitem__)
    part1 += 10 * int(line[i1]) + int(line[i2])

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=3, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=3, year=2025)
