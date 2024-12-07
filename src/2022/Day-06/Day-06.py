import time



def solve(number_of_chars):
    with open('input.txt') as f:
        DATA = f.read()
    for index in range(number_of_chars, len(DATA)):
        packet = DATA[index - number_of_chars:index]  # sliding window
        if len(set(packet)) == number_of_chars:
            return index


def main():
    print('Part 1: ', solve(4))
    print('Part 2: ', solve(14))


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("--- %s seconds ---" % (time.time() - start_time))

