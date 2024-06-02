import sys
input = sys.stdin.readline
from collections import deque


def main():
    N,M = map(int,input().split())
    inpmap = []
    visit = [[False for i in range(M)] for j in range(N)]
    queue = deque()
    
    x = [0,0,1,-1]
    y = [1,-1,0,0]
    
    for i in range(N):
        inp = list(map(int, input().split()))
        inpmap.append(inp)
        if 2 in inp:
            nx = inp.index(2)
            queue.append([i,nx,1])
            visit[i][nx] = True
            inpmap[i][nx] = 0
    
    while queue:
        tar = queue.popleft()
        
        for i in range(4):
            nexty = tar[0]+y[i]
            nextx = tar[1]+x[i]
            if -1<nexty<N and -1<nextx< M and visit[nexty][nextx] == False:
                if inpmap[nexty][nextx] != 0:
                    visit[nexty][nextx] = True
                    inpmap[nexty][nextx] = tar[2]
                    queue.append([nexty,nextx,tar[2]+1])

    for i in range(N):
        for j in range(M):
            if visit[i][j] == False and inpmap[i][j] == 1:
                print(-1, end=' ')
            else:
                print(inpmap[i][j], end=' ')
        print()
        
if __name__ == "__main__": 
    main()