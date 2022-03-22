import regex


class Rule:
    def __init__(self, rule_num):
        self.num = rule_num
        self.sub_rules = []
        self.literal = None
        self.recursive = False

    def __repr__(self):
        return f"Rule: {self.num} ({self.sub_rules if not self.literal else self.literal})"

    def special_processing(self):
        # Super duper hacky, but I really don't give a damn anymore
        if self.num == 8:
            rule = self.sub_rules[0][0]
            print(rule.num)
            return f"({rule.generate_regex()})+"
            # return f"(?<eight>{rule.generate_regex()})(?&eight)?"
        elif self.num == 11:
            sr = self.sub_rules[0]
            fortytwo, thirtyone = sr
            if not (fortytwo.num == 42 and thirtyone.num == 31):
                print("ALO BA, OVO NIJE OK")
                exit(1)
            fortytwo_s = fortytwo.generate_regex()
            thirtyone_s = thirtyone.generate_regex()
            return f"(?<eleven>({fortytwo_s}(?&eleven)?{thirtyone_s}))"

    def generate_regex(self):
        # if self.num in (8, 11):
        # return self.special_processing()
        if self.literal:
            return self.literal
        else:
            sub_rules = []
            for rule in self.sub_rules:
                sr = []
                sr.append('(')
                for r in rule:
                    sr.append('(')
                    subregex = r.generate_regex()
                    if isinstance(subregex, Rule):
                        raise ValueError
                    sr.append(subregex)
                    sr.append(')')
                sr.append(')')
                sub_rules.append(''.join(sr))
            return '|'.join(sub_rules)


def get_rule(the_map, rule_num):
    if not rule_num in the_map:
        the_map[rule_num] = Rule(rule_num)
    return the_map[rule_num]


with open("../Inputs/InputDay19_Rules.txt")as input_file:
    raw = input_file.read()

rules_raw = [line for line in raw.split('\n') if line.strip()]

with open("../Inputs/InputDay19_Messages.txt") as input_file:
    raw = input_file.read()

messages = [line for line in raw.split('\n') if line.strip()]

num_rules_map = {}

for line in rules_raw:
    rule_num, r_rule = line.split(': ')
    rule_num = int(rule_num)

    rule = get_rule(num_rules_map, rule_num)

    if rule_num == 8:
        # hack, increase as needed
        r_rule = ' | '.join([' '.join(['42' for _ in range(n)]) for n in range(1, 10)])
    elif rule_num == 11:
        actual_subrules = []
        for i in range(1, 10):
            rules = ['42' for _ in range(i)] + ['31' for _ in range(i)]
            actual_subrules.append(' '.join(rules))
        r_rule = ' | '.join(actual_subrules)

    if r_rule.startswith('"'):
        rule.literal = r_rule.strip('"')
    else:
        r_sub_rules = r_rule.split(' | ')

        sub_rules = []
        for r in r_sub_rules:
            parts = r.split(' ')
            rule_parts = []
            for p in parts:
                p = int(p)
                if p == rule_num:
                    rule.recursive = True
                rule_part = get_rule(num_rules_map, p)
                rule_parts.append(rule_part)
            sub_rules.append(rule_parts)

        rule.sub_rules = sub_rules

# process_subrules(num_rules_map[0])

part_two_valid_messages = 0
rule_0 = num_rules_map[0]
rule_0_regex = rule_0.generate_regex()
print(rule_0_regex)
regex = regex.compile(rule_0_regex + "\\Z")
for i, msg in enumerate(messages):
    valid = regex.match(msg)
    if valid:
        print(i, msg, "Valid")
        part_two_valid_messages += 1
print("After updating rules 8 and 11, how many messages completely match rule 0? ", part_two_valid_messages)
