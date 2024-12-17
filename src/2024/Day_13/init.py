import sympy as sp
from sympy import symbols, Eq

def parse_input(file_path):
    machines = []
    with open(file_path, 'r') as file:
        machine = {}
        for line in file:
            line = line.strip()
            if not line:
                machines.append(machine)
                machine = {}
            elif line.startswith("Button A:"):
                a_x, a_y = [int(v.split("+")[1]) for v in line.split(", ")]
                machine['a_x'], machine['a_y'] = a_x, a_y
            elif line.startswith("Button B:"):
                b_x, b_y = [int(v.split("+")[1]) for v in line.split(", ")]
                machine['b_x'], machine['b_y'] = b_x, b_y
            elif line.startswith("Prize:"):
                p_x, p_y = [int(v.split("=")[1]) for v in line.split(", ")]
                machine['p_x'], machine['p_y'] = p_x, p_y
        if machine:
            machines.append(machine)
    return machines

def minimal_tokens_to_win(machine, offset=0):
    x, y = symbols('x y', integer=True, nonnegative=True)
    eq1 = Eq(machine['a_x'] * x + machine['b_x'] * y, machine['p_x'] + offset)
    eq2 = Eq(machine['a_y'] * x + machine['b_y'] * y, machine['p_y'] + offset)
    solution = sp.solve((eq1, eq2), (x, y), dict=True)
    
    if not solution:
        return None
    for s in solution:
        if s[x] >= 0 and s[y] >= 0:
            return 3 * s[x] + s[y]
    return None

def solve(machines, part_two=False):
    offset = 10**13 if part_two else 0
    total_tokens = 0
    for machine in machines:
        tokens = minimal_tokens_to_win(machine, offset)
        if tokens:
            total_tokens += tokens
    return total_tokens

if __name__ == "__main__":
    machines = parse_input("input.txt")
    print(f"Part 1: {solve(machines)}")
    print(f"Part 2: {solve(machines, part_two=True)}")
