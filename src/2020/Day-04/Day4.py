def part1(data):
    passports = data.split('\n\n')
    passports = [p.split() for p in passports]
    count = 0
    for passport in passports:
        keys = {p.split(':')[0] for p in passport}
        count += all(k in keys for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'})
    return count


def part2(data):
    passports = data.split('\n\n')
    passports = [p.split() for p in passports]
    count = 0
    for passport in passports:
        keys = {p.split(':')[0]: p.split(':')[1] for p in passport}
        if not all(k in keys for k in {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}):
            continue
        if not keys['byr'].isdigit():
            continue
        if not (1920 <= int(keys['byr']) <= 2002):
            continue
        if not keys['iyr'].isdigit():
            continue
        if not (2010 <= int(keys['iyr']) <= 2020):
            continue
        if not keys['eyr'].isdigit():
            continue
        if not (2020 <= int(keys['eyr']) <= 2030):
            continue
        if not keys['pid'].isdigit():
            continue
        if not len(keys['pid']) == 9:
            continue
        if not keys['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
            continue
        if not keys['hcl'].startswith('#') or not len(keys['hcl']) == 7:
            continue
        if not (keys['hcl'][1:].isalnum()):
            continue
        if keys['hgt'][-2:] not in {'cm', 'in'}:
            continue
        if not keys['hgt'][:-2].isdigit():
            continue
        if keys['hgt'].endswith('cm') and not (150 <= int(keys['hgt'][:-2]) <= 193):
            continue
        if keys['hgt'].endswith('in') and not (59 <= int(keys['hgt'][:-2]) <= 76):
            continue
        count += 1
    return count


with open('../../../curr/2020/Inputs/InputDay4.txt', 'r') as f1:
    inputData = f1.read()
    print('Part 1: {}' .format(part1(inputData)))
    print('Part 2: {}' .format(part2(inputData)))