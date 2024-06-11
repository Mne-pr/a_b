import sys
input = sys.stdin.readline
from collections import deque

def main():
    M,N,H = map(int,input().split())
    box = []
    q = deque()
    maxv = -1
    
    xx = [0,1,0,-1,0,0]
    yy = [1,0,-1,0,0,0]
    hh = [0,0,0,0,1,-1]
    
    # 입력받음
    for i in range(H):
        box.append([])
        for j in range(N):
            inp = list(map(int,input().split()))
            box[-1].append(inp)
            for k in range(M):
                if inp[k] == 1:
                    q.append([i,j,k,1]) # 높이,세로,가로
                elif inp[k] == 0:
                    maxv = 0 
    # 이미 다 썩은 경우
    if maxv == -1:
        print(0)
        return

    while q:
        h,y,x,v = q.popleft()
        
        for i in range(6):
            nh,ny,nx = h+hh[i], y+yy[i], x+xx[i]
            
            if 0 <= nh < H and 0 <= ny < N and 0 <= nx < M:
                if box[nh][ny][nx] == 0:
                    q.append([nh,ny,nx,v+1])
                    box[nh][ny][nx] = v+1
                    if v+1 > maxv:
                        maxv = v+1          
    for plane in box:
        for line in plane:
            if 0 in line:
                print(-1)
                return
    print(maxv-1)

if __name__ == "__main__":
    main()