#!/bin/python3

import re
from argparse import ArgumentParser


NEIGHBOR_DELTAS = [
     1 + 1j, # bottom right
     1 - 1j, # top right
     0 - 2j, # top
    -1 - 1j, # top left
    -1 + 1j, # bottom left
     0 + 2j, # bottom
]


parser = ArgumentParser()
parser.add_argument("input_file", help="path to file containing puzzle input")
parser.add_argument("--part2", action="store_true", help="compute solution for part 2")
args = parser.parse_args()

with open(args.input_file) as f:
    inp = f.read()

heights = {complex(2 * x + y % 2, y): int(height if height.isdigit() else -1)
           for y, line in enumerate(inp.split("\n")[1:-2])
           for x, height in enumerate(re.findall(r"/(.)", line))}

def get_neighbors(xy):
    return [heights[xy + d] for d in NEIGHBOR_DELTAS
            if xy + d in heights]

def spread_light(xy, light_height, light_d, lit):
    highest = 0
    while xy in heights and highest < light_height:
        if highest == 0 or heights[xy] > highest:
            lit.add(xy)
        highest = max(highest, heights[xy])
        xy += light_d

light_d = 2j
answer = 0
for day in range(256):
    lit = {xy for xy in heights if xy - light_d not in heights}
    for xy in list(lit):
        spread_light(xy, 4, light_d, lit)
    for xy in list(lit) * args.part2:
        height = heights[xy]
        fluorescent_light_d = .5 * light_d * (1 - 1j)
        spread_light(xy + fluorescent_light_d, heights[xy], fluorescent_light_d, lit)
        fluorescent_light_d *= 1j
        spread_light(xy + fluorescent_light_d, heights[xy], fluorescent_light_d, lit)

    new_heights = heights.copy()
    for xy, height in heights.items():
        if xy not in lit:
            continue
        if height == 4:
            answer += 1
            new_heights[xy] = -1
            continue
        neighbors = get_neighbors(xy)
        if height == -1 and len([n for n in neighbors if n >= 2]) >= 2:
            new_heights[xy] = 0
            continue
        if height >= 0:
            new_heights[xy] += 1

    heights = new_heights
    light_d *= 1j

print(answer)

