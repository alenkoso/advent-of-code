def evaluate_expression(line):
    # if slicing, add 1 to end
    outer_parens = []
    paren_count = 0
    paren_start = None

    # Find top-level parens
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

    # Evaluate all remaining operations
    i = 1
    previous_value = int(parts[0])
    # Skip the loop if all we have left is a single value
    while i < len(parts):
        next_value = int(parts[i + 1])
        op = parts[i]
        if op == '+':
            previous_value += next_value
        elif op == '*':
            previous_value *= next_value
        else:
            print("ERROR", op, i)
            raise ValueError
        i += 2

    return previous_value


with open("../Inputs/InputDay18.txt") as input:
    raw = input.read()

    print(evaluate_expression("(5 * 7 * 5) * 6 * 5 + 7 + 6 * 4"))

    lines = [line for line in raw.split('\n') if line.strip()]

    part_one = 0
    for line in lines:
        part_one += evaluate_expression(line)

    print(part_one)
