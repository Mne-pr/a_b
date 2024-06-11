import sys
input = sys.stdin.readline
from collections import deque

def main():
    N,M = map(int,input().split())
    land = []
    
    xx=[0,1,0,-1]
    yy=[1,0,-1,0]
    
    for _ in range(N):
        land.append(list(map(int,input().rstrip())))   
    q = deque([[0,0]])
    
    c = -1
    n = len(q)
    
    while q:
        tn = 0
        for _ in range(n):            
            y,x = q.popleft()
            land[y][x] = c
        
            for i in range(4):
                nx, ny = x+xx[i], y+yy[i]
                if nx == M-1 and ny == N-1:
                    print((c-1)*(-1)); return
                if 0 <= nx < M and 0 <= ny < N and [y,x] not in q and land[ny][nx] == 1:
                    q.append([ny,nx])
                    tn += 1   
        n = tn
        c -= 1

if __name__ == "__main__":
    main()
    