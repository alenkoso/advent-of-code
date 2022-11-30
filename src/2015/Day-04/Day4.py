# (urL: https://www.geeksforgeeks.org/md5-hash-python/ )
# (urL: https://stackoverflow.com/questions/5297448/how-to-get-md5-sum-of-a-string-using-python)

from hashlib import md5
from itertools import count

with open("input.txt") as input:
    raw = input.read().strip()

    match_found = False
    for i in count(1):
        md5_hash = md5("{s}{n}".format(s=raw, n=i).encode()).hexdigest()
        if md5_hash.startswith("0" * 6):
            print("Smallest md5 hash in hexadecimal with at least five zeroes is: ", i)
            break
        elif not match_found and md5_hash.startswith("0" * 5):
            print("Smallest md5 hash in hexadecimal with exactly five zeroes is: ", i)
            match_found = True
