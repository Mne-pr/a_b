import sys
input = sys.stdin.readline
from collections import deque

# BFS 인데 거를 건 거르자 문제인듯
def main():
    N,K = map(int,input().split())
    
    if (N >= K):
        print(N-K); return
    
    # 큐 2개 번갈아서
    queues  = [deque(),deque([N+1,N-1,N*2])]
    counter = [0]*10000001
    counter[N+1] = 1; counter[N-1] = 1; counter[N*2] = 1
    count   = 1
    
    while True:
        c  = count%2
        cc = (count+1)%2
        while queues[c]:
            tar = queues[c].popleft()
            if tar == K:
                print(count); return
                
            for i in [tar+1,tar-1,tar*2]:
                if 0 <= i <= 10000000 and counter[i] == 0:
                    queues[cc].append(i)
                    counter[i] = 1

        count += 1

if __name__ == "__main__": 
    main()