import re
from string import ascii_lowercase
import time


def find_next_password(password, n=1):
    for i in range(n):
        password = increment_password(password)
        while not validate(password):
            password = increment_password(password)
    return password


def validate(password):
    # Requirement 2
    if re.search(r"[iol]", password):
        return False

    # Requirement 1
    for i in range(len(password) - 2):
        if password[i:i + 3] in ascii_lowercase:
            break
    else:
        return False

    # Requirement 3
    return True if re.search(r"(\w)\1.*(\w)\2", password) else False


def increment_password(password):
    if password.endswith("z"):
        i_z = password.index("z")
        n_z = len(password) - i_z
        boundary_letter = password[i_z - 1]
        return password[:i_z - 1] + next_letter(boundary_letter) + "a" * n_z
    else:
        return password[:-1] + next_letter(password[-1])


def next_letter(c):
    return ascii_lowercase[(ascii_lowercase.index(c) + 1) % 26]


with open("input.txt") as input_file:
    start_time = time.time()
    password = input_file.readline().strip()
    next_password = find_next_password(password)
    print("First password: {}".format(next_password))
    print("Second password: {}".format(find_next_password(next_password)))
    print()
    print("Code run time", (time.time() - start_time)*1000, "ms")
