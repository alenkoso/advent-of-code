def parse_input_line(line):
    start, end = line.split('~')
    start = tuple(map(int, start.split(',')))
    end = tuple(map(int, end.split(',')))
    return start, end

def read_input(file_path):
    with open(file_path, 'r') as file:
        return [parse_input_line(line.strip()) for line in file]

def find_final_position(brick, settled_bricks):
    start, end = brick
    while True:
        if any(other_brick == brick for other_brick in settled_bricks):
            break
        start = (start[0], start[1], start[2] - 1)
        end = (end[0], end[1], end[2] - 1)
    return (start, end)

def find_dependencies(brick, settled_bricks):
    dependencies = []
    for other in settled_bricks:
        if is_directly_below(brick, other):
            dependencies.append(other)
    return dependencies

def is_directly_below(brick, other):
    pass

def is_safe_to_remove(brick, dependencies, graph):
    for dep in dependencies:
        if all(other == brick for other in graph[dep]):
            return False
    return True

input_data = read_input("example.txt")

settled_bricks = []
for brick in input_data:
    final_position = find_final_position(brick, settled_bricks)
    settled_bricks.append(final_position)

dependency_graph = {}
for brick in settled_bricks:
    dependency_graph[brick] = find_dependencies(brick, settled_bricks)

safe_bricks = []
for brick, dependencies in dependency_graph.items():
    if is_safe_to_remove(brick, dependencies, dependency_graph):
        safe_bricks.append(brick)

print("Part1:", len(safe_bricks))
