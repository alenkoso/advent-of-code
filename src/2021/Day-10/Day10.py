with open("input.txt", mode='r') as f:
    data = f.read().splitlines()

total_points = 0

incomplete_line_scores = []

for line in data:
    failed = False
    stack = []
    incomplete_line_points = 0
    for char in line:
        if char in ["(", "[", "{", "<"]:
            stack.append(char)
        elif char in [")", "]", "}", ">"]:
            if len(stack) == 0:
                break
            if char == ")" and stack[-1] == "(":
                stack.pop()
            elif char == "]" and stack[-1] == "[":
                stack.pop()
            elif char == "}" and stack[-1] == "{":
                stack.pop()
            elif char == ">" and stack[-1] == "<":
                stack.pop()
            else:
                # get points for this error
                if char == ")":
                    points = 3
                elif char == "]":
                    points = 57
                elif char == "}":
                    points = 1197
                elif char == ">":
                    points = 25137
                total_points += points
                failed = True
                break
    if failed or len(stack) == 0:
        continue
    # find the closing characters for all remaining open brackets
    for char in reversed(stack):
        incomplete_line_points *= 5
        if char == "(":
            incomplete_line_points += 1
        elif char == "[":
            incomplete_line_points += 2
        elif char == "{":
            incomplete_line_points += 3
        elif char == "<":
            incomplete_line_points += 4
    incomplete_line_scores.append(incomplete_line_points)

# Part 1
print(total_points)

# Part 2
incomplete_line_scores.sort()
print(incomplete_line_scores[len(incomplete_line_scores) // 2])