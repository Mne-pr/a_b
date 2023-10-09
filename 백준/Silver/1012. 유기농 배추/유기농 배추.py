import sys
sys.setrecursionlimit(10**6)

for1 = int(input())
w,h,n = 0,0,0
inp = []
res = []

def rem(x,y):
    if (x < 0 or x >= w or y < 0 or y >= h):
        return
    if(str(y) not in inp[x]):
        return
    
    del inp[x][str(y)]
    rem(x-1,y)
    rem(x+1,y)
    rem(x,y-1)
    rem(x,y+1)
    

for _ in range(for1):
    w,h,n = list(map(int, input().split()))
    inp = [{} for _ in range(w)]
    count = 0
    
    for _ in range(n):
        n1,n2 = input().split()
        inp[int(n1)][n2] = int(n2)
    
    for i in range(w):
        for j in range(h):
            if (str(j) in inp[i]):
                rem(i,j)
                count += 1
    res.append(count)

for i in res:
    print(i)