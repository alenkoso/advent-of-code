def selector_v2(input):
    seat = input.replace('F', '0').replace('B', '1').replace('L', '0').replace('R', '1')
    return int(seat[:7], 2) * 8 + int(seat[-3:], 2)


boardingPasses = open('../../../curr/2020/Inputs/InputDay5.txt').read().splitlines()
seatIDs = [selector_v2(ticket) for ticket in boardingPasses]
first = max(seatIDs)
print('Part one: ', first)
second = sum(range(min(seatIDs), first + 1)) - sum(seatIDs)
print('Part two: ', second)
