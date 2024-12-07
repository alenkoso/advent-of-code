import re


def parse_workflows(workflow_lines):
    return {line.split("{")[0]: line.split("{")[1][:-1] for line in workflow_lines}

def parse_part(part_line):
    return list(map(int, re.findall(r'\d+', part_line)))

def process_part(part, workflows, current_workflow):
    w = workflows[current_workflow]
    for it in w.split(","):
        if it == "R":
            return False
        if it == "A":
            return True
        if ":" not in it:
            return process_part(part, workflows, it)
        cond, next_workflow = it.split(":")
        if evaluate_condition(part, cond):
            if next_workflow in ["R", "A"]:
                return next_workflow == "A"
            return process_part(part, workflows, next_workflow)
        raise Exception(f"Invalid workflow configuration: {w}")

    def evaluate_condition(part, cond):
        attribute, operator, value = re.match(r'(\w)([><]=?)(\d+)', cond).groups()
        value = int(value)
        part_value = part['xmas'.index(attribute)]
        return compare_values(part_value, operator, value)

    def compare_values(part_value, operator, target_value):
        if operator == '>':
            return part_value > target_value
    elif operator == '<':
        return part_value < target_value
elif operator == '>=':
    return part_value >= target_value
elif operator == '<=':
    return part_value <= target_value
else:
    raise ValueError(f"Invalid operator: {operator}")

def main(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split("\n\n")
        workflow_lines, part_lines = content[0].split("\n"), content[1].split("\n")

        workflows = parse_workflows(workflow_lines)
        parts = [parse_part(line) for line in part_lines]

        total_sum = sum(sum(part) for part in parts if process_part(part, workflows, 'in'))
        print(f"Total sum of ratings for accepted parts: {total_sum}")

        if __name__ == "__main__":
            input_path = 'input.txt'
            main(input_path)

