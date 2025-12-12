import aocd, sys

inp = r"""svr: aaa bbb
aaa: fft
fft: ccc
bbb: tty
tty: ccc
ccc: ddd eee
ddd: hub
hub: fff
eee: dac
dac: fff
fff: ggg hhh
ggg: out
hhh: out
you: bbb ccc"""

# Get input from server if specified
if len(sys.argv) > 1 and (sys.argv[1] == "gd" or sys.argv[1] == "s1" or sys.argv[1] == "s2"):
    inp = aocd.get_data(day=11, year=2025)

### BEGIN SOLUTION

from functools import cache

neighbors = {label[:-1]: outputs for label, *outputs in map(str.split, inp.split("\n"))}
neighbors["out"] = []

@cache
def n_routes(src, dst):
    if src == dst:
        return 1
    return sum(n_routes(neighbor, dst) for neighbor in neighbors[src])

part1 = n_routes("you", "out")
part2 = n_routes("svr", "fft") * (
    n_routes("fft", "dac") * n_routes("dac", "out") + 
    n_routes("dac", "fft") * n_routes("fft", "out"))


# from collections import defaultdict
# 
# part1 = part2 = 0
# incoming = defaultdict(set)
# neighbors = defaultdict(set)
# for line in inp.split("\n"):
#     label, *outputs = line.replace(":", "").split()
#     for output in outputs:
#         incoming[output].add(label)
#     neighbors[label] = set(outputs)
# 
# reachable = set()
# q = ["you"]
# while q:
#     cur = q.pop(0)
#     if cur in reachable:
#         continue
#     reachable.add(cur)
#     for n in neighbors[cur]:
#         q.append(n)
# for label in incoming:
#     incoming[label] &= reachable
# 
# routes_from_you = defaultdict(int)
# routes_from_you["you"] = 1
# q = ["you"]
# while q:
#     cur = q.pop(0)
#     for neighbor in neighbors[cur]:
#         routes_from_you[neighbor] += routes_from_you[cur]
#         incoming[neighbor] -= {cur}
#         if len(incoming[neighbor]) == 0:
#             q.append(neighbor)
# 
# part1 = routes_from_you["out"]


### END SOLUTION

print(f"Part 1: {part1}")
print(f"Part 2: {part2}")

if len(sys.argv) > 1 and sys.argv[1] == "s1" and input("Submit part 1? (y/n) ").lower() == "y":
    aocd.submit(part1, part="a", day=11, year=2025)
if len(sys.argv) > 1 and sys.argv[1] == "s2" and input("Submit part 2? (y/n) ").lower() == "y":
    aocd.submit(part2, part="b", day=11, year=2025)
