import itertools

p1, p2 = 8, 7

counter = itertools.count()
die = lambda: (next(counter) % 100) + 1
dieroll = lambda: die() + die() + die()
mod10 = lambda x: ((x - 1) % 10) + 1

pos, score = [p1, p2], [0, 0]
for i in range(1000):
    pos[i % 2] = mod10(pos[i % 2] + dieroll())
    score[i % 2] += pos[i % 2]
    if score[i % 2] >= 1000:
        break

print(min(score) * next(counter))

