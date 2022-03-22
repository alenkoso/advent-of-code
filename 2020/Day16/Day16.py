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

with open("../Inputs/Day16_nearby.txt") as nearby:
    raw = nearby.readlines()

    tickets = []
    for row in raw:
        split = row.strip().split(',')
        ticket = [int(f) for f in split]
        tickets.append(ticket)

    input_ticket = [71, 127, 181, 179, 113, 109, 79, 151, 97, 107, 53, 193, 73, 83, 191, 101, 89, 149, 103, 197]

    number_of_invalid_tickets = 0

    for ticket in tickets:
        for field in ticket:
            is_valid = False
            for rule in rules:
                if valid(field, rules[rule]):
                    is_valid = True
                    break
            number_of_invalid_tickets += field if not is_valid else 0  # ternary operator

print("Consider the validity of the nearby tickets you scanned.")
print("What is your ticket scanning error rate? ", number_of_invalid_tickets)
