from collections import defaultdict
import copy

rules = {
    "departure location": [[41, 598], [605, 974]],
    "departure station": [[30, 617], [625, 957]],
    "departure platform": [[29, 914], [931, 960]],
    "departure track": [[39, 734], [756, 972]],
    "departure date": [[37, 894], [915, 956]],
    "departure time": [[48, 54], [70, 955]],
    "arrival location": [[39, 469], [491, 955]],
    "arrival station": [[47, 269], [282, 949]],
    "arrival platform": [[26, 500], [521, 960]],
    "arrival track": [[26, 681], [703, 953]],
    "class": [[49, 293], [318, 956]],
    "duration": [[25, 861], [873, 973]],
    "price": [[30, 446], [465, 958]],
    "route": [[50, 525], [551, 973]],
    "row": [[39, 129], [141, 972]],
    "seat": [[37, 566], [573, 953]],
    "train": [[43, 330], [356, 969]],
    "type": [[32, 770], [792, 955]],
    "wagon": [[47, 435], [446, 961]],
    "zone": [[30, 155], [179, 957]]
}


def valid(field, ranges):
    for minimum, maximum in ranges:
        if minimum <= field <= maximum:
            return True
    return False


def more_valid(fields, ranges):
    for field in fields:
        is_valid = True
        for minimum, maximum in ranges:
            if field < minimum or field > maximum:
                is_valid = False
            else:
                is_valid = True
        if is_valid:
            break
    return is_valid


# have to implement checks for ticket validity

def is_ticket_valid(ticket):
    for field in ticket:
        is_valid = False
        for r in rules:
            if valid(field, rules[r]):
                is_valid = True
                break
        if not is_valid:
            return False
    return True


# have to check for all field names


def field_names(column):
    valid_names = []
    for field, rule in rules.items():
        is_valid = True
        for c in col:
            if not valid(c, rule):
                is_valid = False
                break
        if is_valid:
            valid_names.append(field)

    return valid_names


def columns(lists, column):
    result = []
    for list in lists:
        result.append(list[column])
    return result


def find_actual_field_names(possible_fields):
    fields = copy.deepcopy(possible_fields)
    field_map = {}
    while len(field_map) < len(possible_fields):
        # get field with only one element
        field = None
        index = None
        for f, p in fields.items():
            if len(p) == 1:
                field = f
                index = p[0]
                break
        del fields[f]
        field_map[field] = index
        for f, p in fields.items():
            if index in p:
                fields[f].remove(index)
    return field_map


with open("../Inputs/Day16_nearby.txt") as nearby:
    raw = nearby.readlines()

    tickets = []
    for row in raw:
        split = row.strip().split(',')
        initial_ticket = [int(f) for f in split]
        tickets.append(initial_ticket)

    input_ticket = [71, 127, 181, 179, 113, 109, 79, 151, 97, 107, 53, 193, 73, 83, 191, 101, 89, 149, 103, 197]

    # use defaultdict to build a structure of indexes

    valid_tickets = [ticket for ticket in tickets if is_ticket_valid(ticket)]
    to_check = valid_tickets + [input_ticket]

    field_index_map = defaultdict(list)
    for i in range(len(valid_tickets[0])):
        col = columns(to_check, i)
        possible_field_names = field_names(col)
        for f in possible_field_names:
            field_index_map[f].append(i)

    for k, v in field_index_map.items():
        print(f"{k}:{v}")

    actual_field_index_map = find_actual_field_names(field_index_map)

    result = 1
    for f in rules:
        if f.startswith('departure'):
            result *= input_ticket[actual_field_index_map[f]]

print("Once you work out which field is which, look for the six fields on your ticket that start with the word "
      "departure.")
print("What do you get if you multiply those six values together? ", result)
