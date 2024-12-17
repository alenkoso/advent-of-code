def parse_input(file_path):
    with open(file_path) as file:
        return [line.strip() for line in file]

def eval_equation(numbers, operators):
    result = numbers[0]
    for i in range(len(operators)):
        if operators[i] == '+':
            result += numbers[i + 1]
        elif operators[i] == '*':
            result *= numbers[i + 1]
        elif operators[i] == '||':
            result = int(str(result) + str(numbers[i + 1]))
    return result

def is_valid_combination(numbers, target, allow_concat):
    num_operators = len(numbers) - 1
    possible_ops = ['+', '*'] if not allow_concat else ['+', '*', '||']
    total_combinations = len(possible_ops) ** num_operators

    for combination in range(total_combinations):
        operators = []
        temp_comb = combination
        for _ in range(num_operators):
            operators.append(possible_ops[temp_comb % len(possible_ops)])
            temp_comb //= len(possible_ops)
        try:
            if eval_equation(numbers, operators) == target:
                return True
        except:
            pass
    return False

def part1(equations):
    total = 0
    for equation in equations:
        target, *numbers = equation.replace(':', '').split()
        target = int(target)
        numbers = list(map(int, numbers))
        if is_valid_combination(numbers, target, allow_concat=False):
            total += target
    return total

def part2(equations):
    total = 0
    for equation in equations:
        target, *numbers = equation.replace(':', '').split()
        target = int(target)
        numbers = list(map(int, numbers))
        if is_valid_combination(numbers, target, allow_concat=True):
            total += target
    return total

def main():
    equations = parse_input("input.txt")

    part_1 = part1(equations)
    print(part_1)

    part_2 = part2(equations)
    print(part_2)

if __name__ == "__main__":
    main()
