import aocd, sys

inp = r"""123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=6, year=2025)

### BEGIN SOLUTION

from math import prod

part1 = part2 = 0
numbers = list(map(lambda line: line.split(), inp.split("\n")))
width = len(numbers[0])
for x in range(width):
    if numbers[-1][x] == "*":
        acc = 1
        for row in numbers[:-1]:
            acc *= int(row[x])
        part1 += acc
    if numbers[-1][x] == "+":
        acc = 0
        for row in numbers[:-1]:
            acc += int(row[x])
        part1 += acc

lines = inp.split("\n")
w = len(lines[0])
h = len(lines)
nums = []
for x in range(w - 1, -1, -1):
    num = ""
    for y in range(h):
        c = lines[y][x]
        if y == h - 1:
            if len(num.strip()) == 0:
                continue
            nums.append(int(num))
            if c == "+":
                part2 += sum(nums)
                nums = []
                continue
            if c == "*":
                part2 += prod(nums)
                nums = []
                continue
        num += c


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=6, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=6, year=2025)
