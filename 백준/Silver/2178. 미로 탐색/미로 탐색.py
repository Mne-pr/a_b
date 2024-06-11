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
    q = deque([[0,0,-1]])
    
    while q:
        y,x,v = q.popleft()
    
        for i in range(4):
            nx, ny = x+xx[i], y+yy[i]
            if nx == M-1 and ny == N-1:
                print((v-1)*(-1)); return
            if 0 <= nx < M and 0 <= ny < N and land[ny][nx] == 1:
                q.append([ny,nx,v-1])
                land[ny][nx] = v-1

if __name__ == "__main__":
    main()