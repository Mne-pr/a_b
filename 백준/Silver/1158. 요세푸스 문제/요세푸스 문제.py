import collections

N,K = list(map(int,input().split()))
queue = collections.deque([i for i in range(1,N+1)])

print('<',end='')
while (N > 0):
    for i in range(K-1):
        n = queue.popleft()
        queue.append(n)
    
    print(queue.popleft(),end='')
    N -= 1
    if (N > 0):
        print(', ',end='')
    
print('>')