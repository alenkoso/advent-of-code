inp = [l.strip().split('-') for l in open('input.txt')]
g = {v : {[a, b][a == v] for a, b in inp if v in [a,b]} for v in {w for l in inp for w in l}}

# rep : control small caves, True if a small cave was repeated, then don't repeat again
# once : True for star 1, don't repeat small caves, make rep always True (rep = once or ...)
def dfs(v, vis = set(), rep = False, once = True):
    if (rep and v in vis) or v == 'start':
        return 0
    if v == 'end':
        return 1

    return sum(dfs(w, [vis,{*vis,v}][v.islower()], once or v in vis or rep, once) for w in g[v])

print('Star 1:', sum(dfs(v) for v in g['start']))
print('Star 2:', sum(dfs(v, once = False) for v in g['start']))