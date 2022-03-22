import itertools
import time


class Rule:
    def __init__(self, rule_number):
        self.num = rule_number
        self.sub_rules = []
        self.literal = None
        self.valid_strings = []

    def __repr__(self):
        return f"Rule: {self.num} ({self.sub_rules if not self.literal else self.literal})"

    def get_valid_strings(self):
        if self.literal:
            return [self.literal]
        else:
            return self.valid_strings

    def evaluate_msg(self, msg):
        return msg in self.valid_strings


def get_rule(the_map, rule_num):
    if not rule_num in the_map:
        the_map[rule_num] = Rule(rule_num)
    return the_map[rule_num]


def process_sub_rules(rule):
    if rule.literal:
        return [rule.literal]
    elif rule.sub_rules:
        for r in rule.sub_rules:
            parts_evaluated = []
            for sr in r:
                s = process_sub_rules(sr)
                parts_evaluated.append(s)
            combs = itertools.product(*parts_evaluated)
            for c in combs:
                rule.valid_strings.append(''.join(c))
    return rule.valid_strings


def get_valid_strings(rule):
    if rule.literal:
        yield rule.literal
    else:
        yield from rule.valid_strings
        sub_rules = rule.sub_rules
        for i, local_rule in enumerate(sub_rules):
            parts_evaluated = []
            for local_subrule in local_rule:
                s = get_valid_strings(local_subrule)
                parts_evaluated.append(list(s))
            combinations = itertools.product(*parts_evaluated)
            for c in combinations:
                valid_string = ''.join(c)
                rule.valid_strings.append(valid_string)
                yield valid_string
        rule.sub_rules = []


def check_valid(rule, msg):
    if rule.literal:
        return msg == rule.literal
    else:
        for s in get_valid_strings(rule):
            if s == msg:
                return True
        return False


with open("../Inputs/InputDay19_Rules.txt") as input:
    raw = input.read()

    rules_raw = [line for line in raw.split('\n') if line.strip()]

    with open("../Inputs/InputDay19_Messages.txt") as input:
        raw = input.read()

    messages = [line for line in raw.split('\n') if line.strip()]

    num_rules_map = {}

    for line in rules_raw:
        rule_num, r_rule = line.split(': ')
        rule_num = int(rule_num)

        rule = get_rule(num_rules_map, rule_num)

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
                    rule_part = get_rule(num_rules_map, p)
                    rule_parts.append(rule_part)
                sub_rules.append(rule_parts)

            rule.sub_rules = sub_rules

    # process_subrules(num_rules_map[0])

    number_of_valid_messages = 0
    rule_0 = num_rules_map[0]
    start_time = time.time()
    for i, message in enumerate(messages):
        valid = check_valid(rule_0, message)
        if valid:
            # print(i, msg, "Valid")
            number_of_valid_messages += valid
    print("How many messages completely match rule 0? ", number_of_valid_messages)
    print(f"Code run time: {time.time() - start_time} sec")
