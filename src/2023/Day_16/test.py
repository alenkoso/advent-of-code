import sys
sys.setrecursionlimit(1000000)

ll = [list(x) for x in open('input.txt').read().strip().split('\n')]
DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
DNS = ['R', 'L', 'D', 'U']
MIRRORS = {
	'.': {'R': ['R'], 'L': ['L'], 'D': ['D'], 'U': ['U']},
	'-': {'R': ['R'], 'L': ['L'], 'D': ['L', 'R'], 'U': ['L', 'R']},
	'|': {'R': ['D', 'U'], 'L': ['D', 'U'], 'D': ['D'], 'U': ['U']},
	'/': {'R': ['U'], 'L': ['D'], 'D': ['L'], 'U': ['R']},
	'\\': {'R': ['D'], 'L': ['U'], 'D': ['R'], 'U': ['L']},
}

def countfrom(start):
	illum = set()
	def illuminate(x, y, dr):
		if (x, y, dr) in illum:
			return
		illum.add((x, y, dr))
		mr = ll[x][y]
		for nxt in MIRRORS[mr][dr]:
			nxt_dr = DIRS[DNS.index(nxt)]
			nx = x + nxt_dr[0]
			ny = y + nxt_dr[1]
			if nx in range(len(ll)) and ny in range(len(ll[0])):
				illuminate(nx, ny, nxt)
	illuminate(start[0], start[1], start[2])
	return len(set([(x, y) for x, y, _ in illum]))

tests = []
for x in range(len(ll)):
	tests.append((x, 0, 'R'))
	tests.append((x, len(ll[0]) - 1, 'L'))
for y in range(len(ll[0])):
	tests.append((0, y, 'D'))
	tests.append((0, len(ll) - 1, 'U'))

print(countfrom((0, 0, 'R')))
print(max(countfrom(test) for test in tests))