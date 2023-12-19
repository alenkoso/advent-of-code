import re

def parse_workflows(workflow_lines):
    workflows = {}
    for line in workflow_lines:
        name, rules_str = line.split("{")
        rules_str = rules_str.strip("}")
        rules = [tuple(rule.split(":")) if ":" in rule else (None, rule) for rule in rules_str.split(",")]
        workflows[name] = rules
    return workflows

def parse_part(part_line):
    ratings = re.findall(r'(\w)=(\d+)', part_line)
    return {rating: int(value) for rating, value in ratings}

def process_part(part, workflows, current_workflow):
    for condition, destination in workflows[current_workflow]:
        if destination == "A":
            return sum(part.values())
        if destination == "R":
            return 0
        if condition:
            attribute, operator, value = re.match(r'(\w)([><]=?)(\d+)', condition).groups()
            value = int(value)
            if eval(f"part['{attribute}'] {operator}{value}"):
                return process_part(part, workflows, destination)
    return 0

def main(file_path):
    with open(file_path, 'r') as file:
        content = file.read().strip().split("\n\n")
        workflow_lines, part_lines = content[0].split("\n"), content[1].split("\n")

    workflows = parse_workflows(workflow_lines)
    parts = [parse_part(line) for line in part_lines]

    total_sum = sum(process_part(part, workflows, 'in') for part in parts)
    print(f"Total sum of ratings for accepted parts: {total_sum}")

if __name__ == "__main__":
    input_path = 'input.txt'  # Replace with your input file path
    main(input_path)
