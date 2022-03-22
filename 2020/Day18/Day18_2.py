# Meaning of the expression parens: http://iconicmath.com/arithmetic/parens/


def evaluate_expression(line):
    # if slicing, add 1 to end
    outer_parens = []
    paren_count = 0
    paren_start = None
    # Find outer parens
    for i, char in enumerate(line):
        if char == '(':
            paren_count += 1
            if paren_start is None:
                paren_start = i
        elif char == ')':
            paren_count -= 1
            if paren_count == 0:
                outer_parens.append((paren_start, i))
                paren_start = None

    # Recursively evaluate all top-level parens
    if outer_parens:
        startend_values = {}
        for start, end in outer_parens:
            # Recursively evaluate expr in parens
            value = evaluate_expression(line[start + 1:end])
            startend_values[(start, end)] = value

        current = 0
        # if slicing, add 1 to end
        parts = []
        for start, end in outer_parens:
            if start != 0:
                parts.append(line[current: start])
            parts.append(str(startend_values[(start, end)]))
            if (current := end + 1) >= len(line):
                break

        if current < len(line):
            parts.append(line[current:])

        new_line = ''.join(parts)
        parts = new_line.split(' ')
    else:
        # If there are no parens, just split normally
        parts = line.split(' ')

    # Evaluate and consume all '+' ops first, if any
    # If we just have a single operation, skip this step
    if len(parts) > 3:
        new_parts = []
        # eval + first
        i = 0
        previous_value = None
        while i + 2 < len(parts):
            left_hand_side = int(parts[i]) if previous_value is None else previous_value
            operation = parts[i + 1]
            right_hand_side = int(parts[i + 2])

            if operation == '+':
                previous_value = left_hand_side + right_hand_side
            else:
                new_parts.append(str(left_hand_side))
                new_parts.append(operation)
                previous_value = None
            i += 2
        if previous_value is not None:
            new_parts.append(str(previous_value))
        if operation == '*':
            new_parts.append(parts[-1])
        old_parts = parts
        parts = new_parts

    # Evaluate remaining operations
    i = 1
    previous_value = int(parts[0])
    # Skip the loop if all we have left is a single value
    while i < len(parts):
        next_value = int(parts[i + 1])
        operation = parts[i]
        if operation == '+':
            previous_value += next_value
        elif operation == '*':
            previous_value *= next_value
        else:
            print("ERROR", operation, i)
            raise ValueError
        i += 2

    return previous_value


with open("../Inputs/InputDay18.txt") as input:
    raw = input.read()

    print(evaluate_expression("9 + (8 * 5 * 5 * 4 * (3 * 5) * 2) + 4 + 4"))

    lines = [line for line in raw.split('\n') if line.strip()]

    part_two = 0
    for line in lines:
        part_two += evaluate_expression(line)

    print(part_two)
