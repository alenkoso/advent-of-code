def is_valid(springs, group_sizes):
    count, groups = 0, []
    for spring in springs:
        if spring == '#':
            count += 1
        elif count > 0:
            groups.append(count)
            count = 0
    if count > 0:
        groups.append(count)
    return groups == group_sizes

def fill_springs(springs, group_sizes, index=0):
    if index >= len(springs):
        return 1 if is_valid(springs, group_sizes) else 0

    if springs[index] != '?':
        return fill_springs(springs, group_sizes, index + 1)

    # Try replacing '?' with '.' or '#'
    springs[index] = '.'
    count = fill_springs(springs, group_sizes, index + 1)
    springs[index] = '#'
    count += fill_springs(springs, group_sizes, index + 1)
    springs[index] = '?'  # Reset to original state
    return count

def process_row(row):
    springs, group_str = row.split()
    group_sizes = [int(x) for x in group_str.split(',')]
    return fill_springs(list(springs), group_sizes)

def main(filename):
    with open(filename, 'r') as file:
        rows = file.readlines()

    total_arrangements = sum(process_row(row.strip()) for row in rows)
    return total_arrangements

# Test with example input
print(main('input.txt'))  # Should return 21
