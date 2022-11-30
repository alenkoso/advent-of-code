import collections

with open("../Inputs/InputDay2.txt", 'r') as f:
    partOne = 0
    partTwo = 0
    for line in f.read().splitlines():
        (code, letter, password) = (line.replace(":", "")).split(" ")
        (rangeLow, rangeHigh) = [int(x) for x in code.split("-")]

        # part 1
        counter = collections.Counter(password)
        charCount = int(counter[letter])
        if charCount in range(rangeLow, rangeHigh + 1):
            partOne += 1
        # part 2
        charLow = password[rangeLow - 1]
        charHigh = password[rangeHigh - 1]
        if (charLow == letter or charHigh == letter) and charHigh != charLow:
            partTwo += 1

    print("Part one: ", partOne)
    print("Part two: ", partTwo)
