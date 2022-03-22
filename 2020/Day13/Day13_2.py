import functools


def earliest_bus(arrival, schedule):
    min_bus = None
    min_wait_time = 1e99
    for bus in schedule:
        wait_time = bus - (arrival % bus)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_bus = bus
    return min_bus, min_wait_time


# za pomoč pri pisanju spodnje funkcije, je dosti v redu pristop z iskanjem najmanjšega skupnega večkratnika oz.
# največjega skupnega delitelja = bezoutID (url: https://en.wikipedia.org/wiki/B%C3%A9zout%27s_identity )

def gcd_bezout_coefficients(a, b):
    old_x, x = a, b
    old_y, y = 1, 0
    old_z, z = 0, 1

    while x != 0:
        q = old_x // x  # floor division
        # The division of operands where the result is the quotient in which the digits after the decimal point are removed.
        # But if one of the operands is negative, the result is floored, i.e., rounded away from zero (towards negative infinity).
        # 9//2 = 4 and 9.0//2.0 = 4.0, -11//3 = -4, -11.0//3 = -4.0

        old_x, x = x, old_x - q * x
        old_y, y = y, old_y - q * y
        old_z, z = z, old_z - q * z

    return old_y, old_z


# zaporedni_bus(razpored)
# uporabu boš in earliest_bus in gcd_bezout_coefficients
# nek list of tuples (a, b), kjer x = a % n
# potreboval bom en var za ostanke
# en var za delitelje


def zaporedni_bus(razpored):
    schedule_part = [(-i, razpored[i]) for i in range(len(razpored)) if razpored[i]]
    remainder_i = [x[0] for x in schedule_part]  # ostanki
    divisors_i = [x[1] for x in schedule_part]  # delitelji
    N = functools.reduce(lambda x, y: x * y, divisors_i)

    divisor_1 = divisors_i[0]
    divisor_2 = divisors_i[1]
    remainder_1 = remainder_i[0]
    remainder_2 = remainder_i[1]

    gcd_1, gcd_2 = gcd_bezout_coefficients(divisor_1, divisor_2)

    x = gcd_1 * divisor_1 * remainder_2 + gcd_2 * divisor_2 * remainder_1

    # ok zdej maš poračunan osnovni x, poračunan maš N za un končni modulo
    # kar zdej rabš je pa še, da to isto sranje nardiš skoz celoten razpored

    # od 2 naprej gledaš, ker prvi korak že maš od prej
    for i in range(2, len(schedule_part)):
        divisor_1 *= divisor_2
        divisor_2 = divisors_i[i]
        remainder_1 = x
        remainder_2 = remainder_i[i]
        gcd_1, gcd_2 = gcd_bezout_coefficients(divisor_1, divisor_2)
        x = gcd_1 * divisor_1 * remainder_2 + gcd_2 * divisor_2 * remainder_1  # dobiš x za posamezen korak

    return x % N


with open("../Inputs/InputDay13.txt") as input:
    raw = input.readlines()

estimate = int(raw[0].strip())
razpored = [int(x) if x != 'x' else None for x in raw[1].strip().split(',')]

print(
    "The earliest timestamp such that all of the listed bus IDs depart at offsets matching their positions in the list: ",
    zaporedni_bus(razpored))
