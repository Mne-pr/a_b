import sys
import collections

N,K = list(map(int,sys.stdin.readline().split()))
queue = collections.deque([i for i in range(1,N+1)])

print('<',end='')
while (N > 1):
    for i in range(K-1):
        queue.append(queue.popleft())
    
    print('%d, '%(queue.popleft()),end='')
    N -= 1
    
print('%d>'%(queue.popleft()))