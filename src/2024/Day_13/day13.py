import os
import sys
import time
from typing import List, Dict, Optional, Tuple
import sympy as sp
from sympy import symbols

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)

from helpers.parsing_utils import read_input_file_strip_lines

def parse_input(lines: List[str]) -> List[Dict]:
    machines = []
    current_machine = {}
    
    for line in lines:
        if not line:
            if current_machine:
                machines.append(current_machine)
                current_machine = {}
            continue
            
        if line.startswith("Button A:"):
            values = line.replace("Button A: ", "").split(", ")
            current_machine["a_x"] = int(values[0].replace("X+", ""))
            current_machine["a_y"] = int(values[1].replace("Y+", ""))
        elif line.startswith("Button B:"):
            values = line.replace("Button B: ", "").split(", ")
            current_machine["b_x"] = int(values[0].replace("X+", ""))
            current_machine["b_y"] = int(values[1].replace("Y+", ""))
        elif line.startswith("Prize:"):
            values = line.replace("Prize: ", "").split(", ")
            current_machine["prize_x"] = int(values[0].replace("X=", ""))
            current_machine["prize_y"] = int(values[1].replace("Y=", ""))
    
    if current_machine:
        machines.append(current_machine)
    
    return machines

def find_minimal_solution(machine: Dict, max_presses: Optional[int] = None) -> Optional[Tuple[int, int]]:
    # Create symbols for our variables
    x, y = symbols('x y')
    
    # Create the system of equations
    eq1 = sp.Eq(machine["a_x"] * x + machine["b_x"] * y, machine["prize_x"])
    eq2 = sp.Eq(machine["a_y"] * x + machine["b_y"] * y, machine["prize_y"])
    
    try:
        # Solve the system
        solution = sp.solve((eq1, eq2), (x, y))
        
        if not solution:
            return None
        
        # Convert solution to float for checking
        x_val = float(solution[x])
        y_val = float(solution[y])
        
        # Check if solution is integer and non-negative
        if not (x_val.is_integer() and y_val.is_integer()):
            return None
            
        x_int = int(x_val)
        y_int = int(y_val)
        
        if x_int < 0 or y_int < 0:
            return None
            
        # Check press limit if specified
        if max_presses is not None and (x_int > max_presses or y_int > max_presses):
            return None
            
        return (x_int, y_int)
        
    except:
        return None

def calculate_tokens(a_presses: int, b_presses: int) -> int:
    return 3 * a_presses + b_presses

def solve_part1(machines: List[Dict]) -> int:
    total_tokens = 0
    
    for machine in machines:
        result = find_minimal_solution(machine, max_presses=100)
        if result:
            a_presses, b_presses = result
            total_tokens += calculate_tokens(a_presses, b_presses)
    
    return total_tokens

def solve_part2(machines: List[Dict]) -> int:
    # Solve part 2: find minimum tokens needed with offset coordinates.
    offset = 10000000000000
    total_tokens = 0
    
    for machine in machines:
        adjusted = machine.copy()
        adjusted["prize_x"] += offset
        adjusted["prize_y"] += offset
        
        result = find_minimal_solution(adjusted)
        if result:
            a_presses, b_presses = result
            total_tokens += calculate_tokens(a_presses, b_presses)
    
    return total_tokens

def main():
    lines = read_input_file_strip_lines("input.txt")
    machines = parse_input(lines)
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(machines)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(machines)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()