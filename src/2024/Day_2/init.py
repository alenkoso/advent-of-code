import os

def parse_input(file_path):
    report_list = []
    with open(file_path) as file:
        for line in file:
            if line.strip():
                report_list.append(list(map(int, line.split())))
    return report_list

def is_safe(levels):
    is_increasing = True
    is_decreasing = True
    for i in range(len(levels) - 1):
        level_difference = levels[i + 1] - levels[i]
        if abs(level_difference) > 3 or level_difference == 0:
            return False
        if level_difference < 0:
            is_increasing = False
        if level_difference > 0:
            is_decreasing = False
    return is_increasing or is_decreasing

def dampners(levels):
    for i in range(len(levels)):
        modified_levels = levels[:i] + levels[i + 1:]
        if is_safe(modified_levels):
            return True
    return False

def part1(report_list):
    safe_report_count = 0
    for levels in report_list:
        if is_safe(levels):
            safe_report_count += 1
    return safe_report_count

def part2(report_list):
    safe_report_count = 0
    for levels in report_list:
        if is_safe(levels) or dampners(levels):
            safe_report_count += 1
    return safe_report_count

def main():
    report_list = parse_input("input.txt")
    
    part_1 = part1(report_list)
    print(part_1)
    
    part_2 = part2(report_list)
    print(part_2)

if __name__ == "__main__":
    main()
