import os,sys
from collections import defaultdict

# quick path hack
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
from helpers.parsing_utils import read_input_file_strip_lines

# read data
lines = read_input_file_strip_lines("input.txt")

# parse robots into simple lists
robots = []
for l in lines:
    pos, vel = l.split()
    x,y = map(int, pos.replace('p=','').split(','))
    dx,dy = map(int, vel.replace('v=','').split(','))
    robots.append([x,y,dx,dy])

# hardcode grid size and steps
W,H = 101,103
steps = 100

# simulate movement
for _ in range(steps):
    for r in robots:
        # update pos using modulo for wrapping
        r[0] = (r[0] + r[2]) % W
        r[1] = (r[1] + r[3]) % H

# count robots per position
pos = defaultdict(int)
for r in robots:
    pos[(r[0],r[1])] += 1

# calc quadrant counts
q = [0]*4
mx,my = W//2,H//2

for (x,y),c in pos.items():
    if x == mx or y == my:
        continue
    idx = (1 if x > mx else 0) + (2 if y > my else 0)
    q[idx] += c

# multiply quadrants for result 
ans = 1
for n in q:
    ans *= n

print(f"Part 1: {ans}")