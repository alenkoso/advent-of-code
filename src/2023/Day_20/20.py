import sys
from collections import defaultdict, deque
import math
import os
from helpers.parsing_utils import read_input_file_strip_lines, parse_reactions, adjust_types


project_root = os.path.join(os.path.dirname(__file__), '..', '..', '..')
sys.path.append(project_root)


# Reading and preprocessing the input data
lines = read_input_file_strip_lines("input.txt")
reactions, typeMapping = parse_reactions(lines)
reactions = adjust_types(reactions, typeMapping)

def least_common_multiple(numbers):
    for number in numbers:
        result = (result * number) // math.gcd(number, result)
    return result

typeMapping = {}

reactions = {}
for line in lines:
    source, destinations = line.split('->')
    source = source.strip()
    destinations = [dest.strip() for dest in destinations.split(', ')]
    reactions[source] = destinations
    typeMapping[source[1:]] = source[0]

def adjust_type(item):
    if item in typeMapping:
    return typeMapping[item] + item
    else:
    return item

fromMapping = {}
invertedIndex = defaultdict(list)
for src, dests in reactions.items():
    reactions[src] = [adjust_type(dest) for dest in dests]
    for dest in reactions[src]:
    if dest[0] == '&':
        if dest not in fromMapping:
        fromMapping[dest] = {}
        fromMapping[dest][src] = 'low'
    invertedIndex[dest].append(src)

# Assertions for input validation
assert len(invertedIndex['rx']) == 1
assert invertedIndex['rx'][0][0] == '&'
watchedComponents = invertedIndex[invertedIndex['rx'][0]]

lowCount = 0
highCount = 0
queue = deque()
activeComponents = set()
previousSignal = {}
signalCount = defaultdict(int)
cycleLengths = []
for time in range(1, 10**8):
    queue.append(('broadcaster', 'button', 'low'))

    while queue:
    component, fromComponent, signalType = queue.popleft()

    if signalType == 'low':
        if component in previousSignal and signalCount[component] == 2 and component in watchedComponents:
        cycleLengths.append(time - previousSignal[component])
        previousSignal[component] = time
        signalCount[component] += 1

    if len(cycleLengths) == len(watchedComponents):
        print("Part 2: ", least_common_multiple(cycleLengths))
        sys.exit(0)

    if component == 'rx' and signalType == 'low':
        print(time + 1)  # This case is not expected to happen within a reasonable time frame

    if signalType == 'low':
        lowCount += 1
    else:
        highCount += 1

    if component not in reactions:
        continue

    if component == 'broadcaster':
        for dest in reactions[component]:
        queue.append((dest, component, signalType))
    elif component[0] == '%':
        if signalType == 'high':
        continue
        else:
        if component not in activeComponents:
            activeComponents.add(component)
            newSignalType = 'high'
        else:
            activeComponents.discard(component)
            newSignalType = 'low'
        for dest in reactions[component]:
            queue.append((dest, component, newSignalType))
    elif component[0] == '&':
        fromMapping[component][fromComponent] = signalType
        newSignalType = 'low' if all(value == 'high' for value in fromMapping[component].values()) else 'high'
        for dest in reactions[component]:
        queue.append((dest, component, newSignalType))
    else:
        assert False, component
    if time == 1000:
    print("Part 1: ", lowCount * highCount)

