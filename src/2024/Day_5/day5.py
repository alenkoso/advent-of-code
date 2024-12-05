from collections import defaultdict, deque

def check(nums, g):
    n = len(nums)
    deg = defaultdict(int)
    adj = defaultdict(list) 
    seen = set(nums)
    
    for a,b in g:
        if a in seen and b in seen:
            adj[a].append(b)
            deg[b] += 1
    
    q = deque([x for x in nums if deg[x] == 0])
    res = []
    
    while q:
        x = q.popleft()
        res.append(x)
        for y in adj[x]:
            deg[y] -= 1
            if deg[y] == 0:
                q.append(y)
                
    return res if len(res) == n else None

rules = []
nums = []
parsing_rules = True

for line in open('input.txt'):
    line = line.strip()
    if not line:
        parsing_rules = False
        continue
    if parsing_rules:
        a,b = map(int, line.split("|"))
        rules.append((a,b))
    else:
        nums.append(list(map(int, line.split(","))))

p1 = p2 = 0

for arr in nums:
    ordered = check(arr, rules)
    if ordered and ordered == arr:
        p1 += arr[len(arr)//2]
    elif ordered:
        p2 += ordered[len(ordered)//2]

print(p1)
print(p2)