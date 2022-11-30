import time


def get_loopsize(pubkey):
    value = 1
    subject = 7
    i = 0
    while value != pubkey:
        value = value * subject
        value = value % 20201227
        i += 1
        # print(value)

    return i


def encrypt_subject(subject, iterations):
    value = 1
    for i in range(iterations):
        value = value * subject
        value = value % 20201227

    return value


with open("../Inputs/InputDay25.txt") as input_file:
    start_time = time.time()
    raw = input_file.read()

    input_raw = [int(line) for line in raw.split('\n') if line.strip()]

    starting_value = 1
    dividing_value = 20201227

    card_pubkey, door_pubkey = input_raw

    # Derive card's loop size

    # door_loopsize = get_loopsize(door_pubkey)
    # print(door_loopsize)
    card_loopsize = get_loopsize(card_pubkey)

    encryption_key = encrypt_subject(door_pubkey, card_loopsize)

    print("What encryption key is the handshake trying to establish? ", encryption_key)
    print()
    print("Code run time: ", (time.time() - start_time) * 1000, "ms")
