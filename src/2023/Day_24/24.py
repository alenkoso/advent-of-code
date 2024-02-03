import os
import sys
from sympy import symbols, solve_poly_system

# Adjusting the import path for parsing_utils
project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

def parse_input(file_path):
    hailstones = []
    with open(file_path, 'r') as file:
        for line in file:
            pos, vel = line.strip().split(" @ ")
            components = list(map(int, pos.split(", ") + vel.split(", ")))
            hailstones.append(tuple(components))
    return hailstones

hailstones = parse_input("input.txt")
intersection_count = 0

# Function to check if two lines are parallel
def are_parallel(vx1, vy1, vx2, vy2):
    return vx1 * vy2 == vx2 * vy1

for i, (px_a, py_a, _, vx_a, vy_a, _) in enumerate(hailstones[:-1]):
    for px_b, py_b, _, vx_b, vy_b, _ in hailstones[i + 1:]:
        # Skip if velocities are identical (parallel lines and stationary points)
        if are_parallel(vx_a, vy_a, vx_b, vy_b):
            continue

        # Calculate intersection using parametric equations of lines
        t_a = symbols(f't_a_{i}')
        t_b = symbols(f't_b_{i}')
        equations = [
            px_a + vx_a * t_a - (px_b + vx_b * t_b),
            py_a + vy_a * t_a - (py_b + vy_b * t_b)
        ]

        # Solve for t_a and t_b
        result = solve_poly_system(equations, t_a, t_b)

        # Check if any valid (positive) solution exists within the target area
        for res in result:
            if all(val.is_real and val >= 0 for val in res):
                ix = px_a + vx_a * res[0]
                iy = py_a + vy_a * res[0]
                if 200000000000000 <= ix <= 400000000000000 and 200000000000000 <= iy <= 400000000000000:
                    intersection_count += 1
                    break  # No need to check other solutions for this pair

print(f"Part 1: Number of intersections within target area: {intersection_count}")

# Part 2: Solve for initial position and velocity using SymPy
x, y, z, vx, vy, vz = symbols('x y z vx vy vz')
equations = []

# Pick the first three hailstones to set up equations
for idx, (px, py, pz, vx_h, vy_h, vz_h) in enumerate(hailstones[:3]):
    t = symbols(f't{idx}')
    equations.extend([
        x + vx * t - px - vx_h * t,
        y + vy * t - py - vy_h * t,
        z + vz * t - pz - vz_h * t,
    ])

# Solve the system of equations
result = solve_poly_system(equations, x, y, z, vx, vy, vz, *symbols(f't0:{len(hailstones[:3])}'))
print(f"Part 2: Sum of initial position coordinates: {sum(result[0][:3])}")
