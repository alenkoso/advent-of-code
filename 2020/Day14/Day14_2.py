import re
from collections import defaultdict
from itertools import combinations


class Mask:
    def __init__(self, mask):
        self.mask = mask
        self.set_mask = 0
        self.floating = []
        for i, bit in enumerate(mask):
            if bit == '0':
                continue
            elif bit == '1':
                mask = 1 << (35 - i)
                self.set_mask |= mask
            else:
                self.floating.append(i)

    def apply(self, value):
        values = []
        value |= self.set_mask
        for i in range(len(self.floating)):
            num = i + 1
            masks = combinations(self.floating, num)

            for mask in masks:
                complement_masks = [x for x in self.floating if x not in mask]
                c_mask = 0
                for position_index in complement_masks:
                    c_mask |= 1 << (35 - position_index)
                c_mask = ~c_mask
                mask_set = value & c_mask
                mask_unset = value & c_mask

                actual_mask = 0
                for position_index in mask:
                    actual_mask |= 1 << (35 - position_index)
                mask_set |= actual_mask
                mask_unset &= ~actual_mask
                values.append(mask_set)
                values.append(mask_unset)
        return values


with open("../Inputs/InputDay14.txt") as input:
    raw = input.readlines()

# da shranimo trenutn memory računalnika, bomo uporabili kar Pythonov built-in dictionary, ker je povsem ok
# struktura za kaj takega
original_memory = defaultdict(int)
# initialize mask
current_mask = None

# v osnovi je zelo podobno part 1
# sprehod se skoz input file, poglej ujemanje za masko (navodila)
# ===================================================================
# vse permuntacije rabis
# maskiras vrednost na memory addresse
# in dobis vrednost z X, naredis permutacije in zafilas tista mesta

for row in raw:
    row = row.strip()
    memory_mask = re.match("mask = (.*)", row)
    if memory_mask:
        mask = memory_mask.group(1)
        current_mask = Mask(mask)
    elif memory_write := re.match("mem\[(.*?)\] = (.*)", row):
        address = int(memory_write.group(1))
        memory_address_value = int(memory_write.group(2))
        # masked_value = current_mask.apply(value)
        # original_memory[address] = masked_value
        actual_address = current_mask.apply(address)
        for naslov in actual_address:
            original_memory[naslov] = memory_address_value
    else:
        exit(1)

print("The sum of all values left in memory after it completes is: ", sum(list(original_memory.values())))
