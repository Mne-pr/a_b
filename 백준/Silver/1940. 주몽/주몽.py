import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
Nlist = list(map(int,sys.stdin.readline().split()))
Nlist.sort()

min,max = 0,N-1
sum,res = 0,0

while(max > min):
    sum = Nlist[min]+Nlist[max]
    if (sum > M):
        max -= 1
    elif (sum < M):
        min += 1
    elif (sum == M):
        res += 1
        min += 1
        max -= 1
    
print(res)