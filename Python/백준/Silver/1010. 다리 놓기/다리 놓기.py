from sys import stdin
input = stdin.readline

# 순서에 상관없이 M에서 N개를 뽑는 경우니 combination임

def com(n,r):
    res = 1
    for i in range(r):
        res = res * (n-i) / (i+1)
    return int(res)

def main():
    T = int(input())
    res = []
    
    for _ in range(T):
        N,M = map(int,input().split())
        res.append(com(M,N))
    
    for item in res:
        print(item)
    
if __name__ == "__main__": 
    main()