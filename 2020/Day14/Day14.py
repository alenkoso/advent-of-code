from collections import defaultdict
import re


# bom reševal z bitwise operatorji
# za hitro delovanje bo v uporabi tudi bit shift

class Mask:
    def __init__(self, mask):
        self.mask = mask
        self.actual_masks = []
        for i, bit in enumerate(mask):
            if bit == '0':
                bit_operator = '+'
                mask = ~(1 << (35 - i))
            elif bit == '1':
                bit_operator = '|'
                mask = 1 << (35 - i)
            else:
                continue
            self.actual_masks.append((bit_operator, mask))

    def apply(self, value):
        for bitOperator, mask in self.actual_masks:
            if bitOperator == '+':
                value = value & mask
            elif bitOperator == '|':
                value = value | mask
        return value


with open("../Inputs/InputDay14.txt") as input:
    raw = input.readlines()

# da shranimo trenutn memory računalnika, bomo uporabili kar Pythonov built-in dictionary, ker je povsem ok
# struktura za kaj takega
original_memory = defaultdict(int)
# initialize mask
current_mask = None

# sprehod se skoz input file, poglej ujemanje za masko (navodila)
# če se ujema s prvim vzorcem: uporabi class Mask
# če se ujema z drugim vzorcem: se moraš igrat s spominom
for row in raw:
    row = row.strip()
    memory_mask = re.match("mask = (.*)", row)
    if memory_mask:
        mask = memory_mask.group(1)
        current_mask = Mask(mask)
    elif memory_write := re.match("mem\[(.*?)\] = (.*)", row):
        address = int(memory_write.group(1))
        value = int(memory_write.group(2))
        masked_value = current_mask.apply(value)
        original_memory[address] = masked_value
    else:
        exit(1)

print("The sum of all values left in memory after it completes is: ", sum(list(original_memory.values())))
