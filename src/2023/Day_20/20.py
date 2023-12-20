import re
from collections import defaultdict, deque
import math

def parse_input(input_lines):
    modules = {}
    for line in input_lines:
        parts = line.split(" -> ")
        name = parts[0].strip('%&')
        module_type = '%' if '%' in parts[0] else '&' if '&' in parts[0] else None
        destinations = parts[1].split(", ") if len(parts) > 1 else []
        modules[name] = {"type": module_type, "destinations": destinations, "state": False if module_type == '%' else defaultdict(lambda: False)}
    return modules

def simulate_pulse(modules, module_name, pulse_type):
    module = modules[module_name]
    if module["type"] == "%":
        if pulse_type == "high":
            return []
        else:
            module["state"] = not module["state"]
            new_pulse = "high" if module["state"] else "low"
            return [(dest, new_pulse) for dest in module["destinations"]]
    elif module["type"] == "&":
        module["state"][module_name] = (pulse_type == "high")
        all_high = all(module["state"].values())
        new_pulse = "low" if all_high else "high"
        return [(dest, new_pulse) for dest in module["destinations"]]
    else:
        return [(dest, pulse_type) for dest in module["destinations"]]

def lcm(numbers):
    def lcm_pair(x, y):
        return x * y // math.gcd(x, y)
    result = 1
    for number in numbers:
        result = lcm_pair(result, number)
    return result

def count_pulses(input_lines, num_pushes):
    modules = parse_input(input_lines)
    seen_states = {}
    low_count = high_count = 0

    # Track changes in state for each module
    state_changes = defaultdict(list)

    for push in range(num_pushes):
        queue = deque([("broadcaster", "low")])

        while queue:
            module_name, pulse_type = queue.popleft()
            low_count += pulse_type == "low"
            high_count += pulse_type == "high"
            new_pulses = simulate_pulse(modules, module_name, pulse_type)
            queue.extend(new_pulses)

            # Record state change timestamps
            if module_name in modules and modules[module_name]["type"] == "%":
                state_changes[module_name].append(push)

        # Detect cyclic patterns using LCM
        if push > 0 and all(len(changes) > 1 for changes in state_changes.values()):
            cycle_lengths = [changes[-1] - changes[-2] for changes in state_changes.values()]
            cycle_lcm = lcm(cycle_lengths)
            remaining_cycles = (num_pushes - push - 1) // cycle_lcm
            low_count += remaining_cycles * (low_count - seen_states["low"])
            high_count += remaining_cycles * (high_count - seen_states["high"])
            break

        seen_states["low"] = low_count
        seen_states["high"] = high_count

    return low_count, high_count

def main(file_path):
    with open(file_path, 'r') as file:
        input_lines = file.read().split("\n")
    low, high = count_pulses(input_lines, 1000)
    print(f"Low pulses: {low}, High pulses: {high}, Product: {low * high}")

if __name__ == "__main__":
    input_path = 'input.txt'  # Replace with your input file path
    main(input_path)
