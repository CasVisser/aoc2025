import aocd, sys

inp = r"""11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
1698522-1698528,446443-446449,38593856-38593862,565653-565659,
824824821-824824827,2121212118-2121212124"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=2, year=2025)

### BEGIN SOLUTION

from itertools import batched
from re import findall

ids = [str(i) for start, end in findall(r"(\d+)-(\d+)", inp) for i in range(int(start), int(end) + 1)]
part1 = sum(int(i) for i in ids if i[:len(i) // 2] == i[len(i) // 2:])
part2 = sum(int(i) for i in ids if any(len(set(batched(i, n))) == 1 for n in range(1, len(i) // 2 + 1)))

### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=2, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=2, year=2025)
