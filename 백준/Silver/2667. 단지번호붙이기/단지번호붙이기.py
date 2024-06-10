import sys
input = sys.stdin.readline

def main():
    N = int(input())
    hc = []
    g = []
    
    xx = [1,0,-1,0]
    yy = [0,1,0,-1]
    
    def check(x, y, v):
        if x == -1 or y == -1 or x == N or y == N:
            return
            
        if g[y][x] == '1':
            g[y][x] = v
            hc[-1] += 1
            
            for i in range(4):
                check(x+xx[i],y+yy[i],v)
        
    for i in range(N):
        g.append(list(input().rstrip()))
    
    house = 0
    for x in range(N):
        for y in range(N):
            if g[y][x] == '1':
                # 새 아파트의 주민수 0 추가
                house -= 1
                hc.append(0)
                check(x,y,str(house))
   
    print(len(hc))
    for item in sorted(hc):
        print(item)

if __name__ == "__main__":
    main()