from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    INP = [[0,0]]
    c = [0,0]

    lv = 10000000
    
    for i in range(1,n+1):
        x,y = map(int, input().split())
        # 일단 추가
        INP.append([x,y])
        c = [c[0]+x,c[1]+y]  
    print(*c)
    
    # 하나 뺐을 때 최소인 거 찾아
    for i in range(1,n+1):
        v = ((c[0]-INP[i][0])**2+(c[1]-INP[i][1])**2)**(1/2)
        if lv > v:
            lv = v
    print('%.2f' %(lv))

if __name__ == "__main__": 
    main()