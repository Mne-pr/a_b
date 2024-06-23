from sys import stdin
input = stdin.readline

def main():
    n,T = map(int,input().split())
    m = int(input())
    x,y = map(int,input().split())
    
    time1 = m / x
    time2 = (n-m) / y
    tt = (time1+time2) / 60
    
    if tt % 1 > 0:
        tt += 1
    
    
    if tt <= T:
        print(0)
    else:
        print(int(tt-T))

if __name__ == "__main__": 
    main()