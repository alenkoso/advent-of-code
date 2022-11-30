from collections import defaultdict
from pprint import pprint
import math

with open("input.txt") as f:
    #content = f.readlines()
    content = [int(x,16) for x in f.readline().strip()]

bits = ""
for c in content:
 bits += format(c, "04b")

print(bits)

# VVVTTTAAAAABBBBBCCCCC

versions = []


def parse(bits, pos=0):
    global versions
    version = bits[pos:pos+3]
    versions.append(version)
    pos += 3
    type = bits[pos:pos+3]
    pos += 3
    if type == '100':
        readbits = True
        out = ""
        while readbits:
            v = bits[pos:pos+5]
            pos += 5
            check = v[0]
            v = v[1:]
            if check == '0':
                readbits = False
            out += v
        return pos, int(out, 2)
    else:
        i = bits[pos]
        pos += 1
        subpackets = []
        if i == '0':
            l = bits[pos:pos+15]
            pos += 15
            limit = pos + int(l, 2)
            while pos < limit:
                pos, v = parse(bits, pos)
                subpackets.append(v)
        else:
            l = bits[pos:pos+11]
            pos += 11
            for p in range(int(l, 2)):
                pos, v = parse(bits, pos)
                subpackets.append(v)

        out = ""
        type = int(type, 2)
        if type == 0:
            out = sum(subpackets)
        elif type == 1:
            out = math.prod(subpackets)
        elif type == 2:
            out = min(subpackets)
        elif type == 3:
            out = max(subpackets)
        elif type == 5:
            a, b = subpackets
            if a > b:
                out = 1
            else:
                out = 0
        elif type == 6:
            a, b = subpackets
            if a < b:
                out = 1
            else:
                out = 0
        elif type == 7:
            a, b = subpackets
            if a == b:
                out = 1
            else:
                out = 0

        return pos, out


pos, values = parse(bits)
# print(versions, values)
s = [int(x, 2) for x in versions]

print(sum(s))
print(values)