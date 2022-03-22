def earliest_bus(arrival, schedule):
    min_bus = None
    min_wait_time = 1e99
    for bus in schedule:
        wait_time = bus - (arrival % bus)
        if wait_time < min_wait_time:
            min_wait_time = wait_time
            min_bus = bus
    return min_bus, min_wait_time


with open("../Inputs/InputDay13.txt") as input:
    raw = input.readlines()

estimate = int(raw[0].strip())
schedule = [int(x) for x in raw[1].strip().split(',') if x != 'x']

b, w = earliest_bus(estimate, schedule)
print("ID of the earliest bus you can take to the airport: ", b, "\n number of minutes you have to wait for the bus: ", w)
print("Part one: ",b * w)
