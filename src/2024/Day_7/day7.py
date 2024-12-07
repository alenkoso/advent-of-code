import os
import sys
import time

project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)
from helpers.parsing_utils import read_input_file_strip_lines

def eval_expr(nums, ops):
    res = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += nums[i+1]
        elif ops[i] == '*':
            res *= nums[i+1]
        else:  # concatenation operator ||
            res = int(str(res) + str(nums[i+1]))
    return res

def solve_equation(nums, target, part2=False):
    n = len(nums) - 1  # Number of operators needed
    max_ops = 3 if part2 else 2
    
    # Try all possible operator combinations
    for mask in range(max_ops ** n):
        ops = []
        temp = mask
        for _ in range(n):
            ops.append(['+', '*', '||'][temp % max_ops])
            temp //= max_ops
        
        try:
            if eval_expr(nums, ops) == target:
                return True
        except:
            continue
    
    return False

def solve_part1(lines):
    result = 0
    for line in lines:
        if not line:
            continue
        
        target, nums = line.split(':')
        target = int(target)
        nums = list(map(int, nums.split()))
        
        if solve_equation(nums, target):
            result += target
    
    return result

def solve_part2(lines):
    result = 0
    for line in lines:
        if not line:
            continue
        
        target, nums = line.split(':')
        target = int(target)
        nums = list(map(int, nums.split()))
        
        if solve_equation(nums, target, True):
            result += target
    
    return result

def main():
    # Read input
    lines = read_input_file_strip_lines("input.txt")
    
    # Part 1
    start_time = time.time()
    part1_result = solve_part1(lines)
    end_time = time.time()
    print(f"Part 1: {part1_result}")
    print(f"Part 1 Execution Time: {end_time - start_time} seconds")
    
    # Part 2
    start_time = time.time()
    part2_result = solve_part2(lines)
    end_time = time.time()
    print(f"Part 2: {part2_result}")
    print(f"Part 2 Execution Time: {end_time - start_time} seconds")

if __name__ == "__main__":
    main()