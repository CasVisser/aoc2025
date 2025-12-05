import aocd, sys

inp = r"""3-5
10-14
16-20
12-18

1
5
8
11
17
32"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=5, year=2025)

### BEGIN SOLUTION

import re

part1 = part2 = 0
ranges, ids = inp.split("\n\n")
fresh_ranges = [tuple(map(int, fresh)) for fresh in re.findall(r"(\d+)-(\d+)", ranges)]
part1 = len([i for i in ids.split("\n") 
             if any(start <= int(i) <= end for start, end in fresh_ranges)])

intervals = [fresh_ranges[0]]
q = fresh_ranges[1:]
while q:
    cur_start, cur_end = q.pop()
    for i, (start, end) in enumerate(intervals):
        if cur_start > end:
            continue
        if cur_end < start:
            intervals.insert(i, (cur_start, cur_end))
            break
        if cur_start < start:
            intervals.insert(i, (cur_start, start - 1))
        if cur_end > end:
            q.append((end + 1, cur_end))
        break
    else:
        intervals.append((cur_start, cur_end))

part2 = sum(end - start + 1 for start, end in intervals)


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=5, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=5, year=2025)
