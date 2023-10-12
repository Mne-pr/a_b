import sys

n,m = list(map(int,sys.stdin.readline().split()))
inp = [[] for _ in range(n+1)]

cur = 1
stack = [cur]
visited = []
res = 0

# 자료구조 생성
for _ in range(m):
    x,y = list(map(int,sys.stdin.readline().split()))
    inp[x].append(y)
    inp[y].append(x)
    
# 본격 탐색
while(cur < n+1):
    if cur in visited:
        cur += 1
        continue
        
    stack = [cur]
    res += 1
    
    while(stack):
        val = stack.pop()
        visited.append(val)
        for w in inp[val]:
            if w in visited or w in stack:
                continue
            stack.append(w)
    
print(res)