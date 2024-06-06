import sys
input = sys.stdin.readline
from collections import deque

def main():
    w,h = map(int,input().split())
    boxes  = []
    q = deque()
    maxv = -1  
    
    for i in range(h):
        states = list(map(int,input().split()))
        boxes.append(states)
        for t in range(w):
            if states[t] == 1:
                q.append([i,t,1])
            if states[t] == 0:
                maxv = 0
    
    if maxv == -1:
        print(0)
        return
    
    xx = [0,0,1,-1]
    yy = [1,-1,0,0]
    
    while q:
        y,x,t = q.popleft()
        
        for i in range(4):
            nx = x+xx[i]
            ny = y+yy[i]
            if 0 <= nx < w and 0 <= ny < h:
                if boxes[ny][nx] == 0:
                    q.append([ny,nx,t+1])
                    boxes[ny][nx] = t+1
                    if t+1 > maxv:
                        maxv = t+1

    for item in boxes:
        if 0 in item:
            print(-1)
            return
    print(maxv-1)
    
if __name__ == "__main__": 
    main()