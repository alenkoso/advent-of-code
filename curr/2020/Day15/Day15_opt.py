import time

def memory_game(myInput, limit, last_encountered=None, print_interval=0):
    """Generates the list of numbers after <limit> iterations of Day 14's
        number game
    Args:
        myInput (list(int)): Initial list of numbers
        limit (int): Maximum number of iterations
        last_encountered (dict(int:int), optional): A cached last_encountered
            list from a previous run, if any. Defaults to None.
        print_interval (int, optional): The number of iterations to print
            runtime at. If 0, this is disabled. Defaults to 0.
    Returns:
        [type]: [description]
    """
    if not last_encountered:
        last_encountered = {num: i for i, num in enumerate(myInput[:-1])}

    i = 0
    my_time = time.time()
    while len(myInput) < limit:
        number = myInput[-1]
        if number not in last_encountered:
            add = 0
        else:
            add = len(myInput) - last_encountered[number] - 1
        last_encountered[number] = len(myInput) - 1
        myInput.append(add)
        i += 1
        if print_interval > 0 and i % print_interval == 0:
            current = time.time()
            print(f"Iteration {i-print_interval+1}-{i}: {current - my_time} sec")
            my_time = current
    if print_interval > 0:
        current = time.time()
        print(f"Iteration {i - (i % print_interval) + 1}-{i}: {current - my_time} sec")

    return last_encountered


myInput = [0, 13, 1, 16, 6, 17]
print("Initial nums:", myInput)
partOne_2020 = memory_game(myInput, 2020)
print("The 2020th number spoken will be: ", myInput[-1])
start_time = time.time()
partTwo_30000000 = memory_game(myInput, 30000000, last_encountered=partOne_2020, print_interval=10000000)
print(f"The 30000000th number spoken will be: : {myInput[-1]} (time elapsed: {time.time() - start_time} sec)")
