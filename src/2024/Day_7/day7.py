def eval_expr(nums, ops):
    res = nums[0]
    for i in range(len(ops)):
        if ops[i] == '+':
            res += nums[i+1]
        elif ops[i] == '*':
            res *= nums[i+1]
        else:
            res = int(str(res) + str(nums[i+1]))
    return res

def solve(nums, target, part2=False):
    n = len(nums) - 1  # operators needed
    max_ops = 3 if part2 else 2
    
    # Try all combinations using base-max_ops numbers
    for mask in range(max_ops ** n):
        ops = []
        temp = mask
        for _ in range(n):
            ops.append(['+', '*', '||'][temp % max_ops])
            temp //= max_ops
        
        try:
            if eval_expr(nums, ops) == target:
                return True
        except:
            continue
            
    return False

p1 = p2 = 0
for line in open('input.txt'):
    if not line.strip(): 
        continue
        
    target, nums = line.split(':')
    target = int(target)
    nums = list(map(int, nums.split()))
    
    if solve(nums, target):
        p1 += target
    if solve(nums, target, True):
        p2 += target

print(p1)
print(p2)