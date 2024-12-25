import os
import sys
import time

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
sys.path.append(project_root)

def parse_input(file_path):
    with open(file_path, "r") as file:
        wires_section, gates_section = file.read().strip().split("\n\n")
    
    wires = {}
    for line in wires_section.splitlines():
        name, value = line.split(": ")
        wires[name] = int(value)
    
    gates = []
    for line in gates_section.splitlines():
        inputs, output = line.split(" -> ")
        a, op, b = inputs.split(" ")
        gates.append({"a": a, "op": op, "b": b, "output": output})
        
        if a not in wires:
            wires[a] = None
        if b not in wires:
            wires[b] = None
        if output not in wires:
            wires[output] = None

    return wires, gates

def process_circuit(wires, gates):
    wire_values = wires.copy()
    max_iterations = 1000
    iteration = 0
    
    while iteration < max_iterations:
        progress_made = False
        iteration += 1
        
        for gate in gates:
            if gate["output"] in wire_values and wire_values[gate["output"]] is not None:
                continue
                
            if wire_values[gate["a"]] is None or wire_values[gate["b"]] is None:
                continue
                
            value1 = wire_values[gate["a"]]
            value2 = wire_values[gate["b"]]
            
            if gate["op"] == "AND":
                wire_values[gate["output"]] = value1 & value2
            elif gate["op"] == "OR":
                wire_values[gate["output"]] = value1 | value2
            elif gate["op"] == "XOR":
                wire_values[gate["output"]] = value1 ^ value2
                
            progress_made = True
            
        if not progress_made:
            break
    
    return wire_values

# https://circuitdigest.com/tutorial/full-adder-circuit-theory-truth-table-construction
def check_gate_conditions(gate, condition_type, value=None):
    if condition_type == "is_sum_bit":
        return gate["a"].startswith("x") or gate["b"].startswith("x")
    elif condition_type == "is_z_output":
        return gate["output"].startswith("z")
    elif condition_type == "is_operation":
        return gate["op"] == value
    elif condition_type == "produces_output":
        return gate["output"] == value
    elif condition_type == "takes_input":
        return gate["a"] == value or gate["b"] == value
    return False

def compute_part1_result(wire_values):
    max_z = max(int(wire[1:]) for wire in wire_values if wire.startswith('z'))
    result = 0
    for i in range(max_z + 1):
        wire = f'z{i:02d}'
        if wire in wire_values and wire_values[wire] is not None:
            result |= (wire_values[wire] << i)
    return result

def identify_critical_gates(wires, gates):
    input_bit_count = len([w for w in wires if w.startswith("x")])
    flags = set()

    initial_gates = [gate for gate in gates if check_gate_conditions(gate, "is_sum_bit") and check_gate_conditions(gate, "is_operation", "XOR")]
    for gate in initial_gates:
        a, b, output = gate["a"], gate["b"], gate["output"]
        is_first = a == "x00" or b == "x00"
        if is_first:
            if output != "z00":
                flags.add(output)
            continue
        elif output == "z00":
            flags.add(output)
        if check_gate_conditions(gate, "is_z_output"):
            flags.add(output)

    intermediate_gates = [gate for gate in gates if check_gate_conditions(gate, "is_operation", "XOR") and not check_gate_conditions(gate, "is_sum_bit")]
    for gate in intermediate_gates:
        if not check_gate_conditions(gate, "is_z_output"):
            flags.add(gate["output"])

    final_gates = [gate for gate in gates if check_gate_conditions(gate, "is_z_output")]
    for gate in final_gates:
        is_last = gate["output"] == f"z{str(input_bit_count).zfill(2)}"
        if is_last:
            if gate["op"] != "OR":
                flags.add(gate["output"])
            continue
        elif gate["op"] != "XOR":
            flags.add(gate["output"])

    next_check = []
    for gate in initial_gates:
        output = gate["output"]
        if output in flags or output == "z00":
            continue

        matches = [g for g in intermediate_gates if check_gate_conditions(g, "takes_input", output)]
        if not matches:
            next_check.append(gate)
            flags.add(output)

    for gate in next_check:
        a, output = gate["a"], gate["output"]
        expected_output = f"z{a[1:]}"
        matching_gates = [g for g in intermediate_gates if check_gate_conditions(g, "produces_output", expected_output)]

        matching_gate = matching_gates[0]
        inputs_to_check = [matching_gate["a"], matching_gate["b"]]
        or_gates = [g for g in gates if check_gate_conditions(g, "is_operation", "OR") and g["output"] in inputs_to_check]

        or_gate_output = or_gates[0]["output"]
        correct_output = next(output for output in inputs_to_check if output != or_gate_output)
        flags.add(correct_output)

    return flags

def main():
    wires, gates = parse_input("input.txt")
    
    start_time = time.time()
    part1_result = compute_part1_result(process_circuit(wires, gates))
    end_time = time.time()
    print("Part 1:", part1_result)
    print("Part 1 Execution Time:", end_time - start_time, "seconds")
    print("Binary:", bin(part1_result)[2:])

    start_time = time.time()
    part2_result = ','.join(sorted(identify_critical_gates(wires, gates)))
    end_time = time.time()
    print("Part 2:", part2_result)
    print("Part 2 Execution Time:", end_time - start_time, "seconds")

if __name__ == "__main__":
    main()