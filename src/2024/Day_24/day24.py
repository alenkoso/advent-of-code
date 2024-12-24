def parse_input(lines):
    initial_values = {}
    gates = []
    max_z = 0

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if ":" in line:
            wire, value = line.split(": ")
            initial_values[wire] = int(value)
        elif "->" in line:
            inputs, outputs = line.split(" -> ")
            gate_parts = inputs.split()
            if len(gate_parts) == 3:
                input1, operator, input2 = gate_parts
                gates.append((input1, operator, input2, outputs.strip()))
                if outputs.startswith('z'):
                    num = int(outputs[1:])
                    max_z = max(max_z, num)
    
    return initial_values, gates, max_z

def simulate_circuit(initial_values, gates):
    wire_values = initial_values.copy()
    max_iterations = 1000
    iteration = 0
    
    while iteration < max_iterations:
        made_progress = False
        iteration += 1
        
        for input1, operator, input2, outputs in gates:
            if outputs in wire_values:
                continue
                
            if input1 not in wire_values or input2 not in wire_values:
                continue
                
            value1 = wire_values[input1]
            value2 = wire_values[input2]
            
            if operator == "AND":
                wire_values[outputs] = value1 & value2
            elif operator == "OR":
                wire_values[outputs] = value1 | value2
            elif operator == "XOR":
                wire_values[outputs] = value1 ^ value2
                
            made_progress = True
            
        if not made_progress:
            break
    
    return wire_values

def part1(wire_values, max_z):
    part_1 = 0
    print("\nZ-wire values:")
    for i in range(max_z + 1):
        wire = f'z{i:02d}'
        if wire in wire_values:
            print(f"{wire}: {wire_values[wire]}")
            part_1 |= (wire_values[wire] << i)
    
    return part_1

def main():
    with open('input.txt', 'r') as file:
        lines = file.readlines()
    
    initial_values, gates, max_z = parse_input(lines)
    
    for wire, value in sorted(initial_values.items()):
        print(wire, " : ", value)
    
    print(len(gates))
    wire_values = simulate_circuit(initial_values, gates)
    
    part_1 = part1(wire_values, max_z)
    print("Part 1: ", part_1)
    # print("Binary: ", bin(part_1)[2:].zfill(max_z + 1))

if __name__ == "__main__":
    main()