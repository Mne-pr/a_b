import sys
input = sys.stdin.readline

def main():
    m,n,p = map(int,input().split())
    res = []
    
    while m+n+p != 0:
        u = set([p])
        v = 1
        
        for i in range(n):
            a,b = map(int,input().split())
            if (a in u and b not in u) or (a not in u and b in u):
                v += 1
                u.update([a,b])
        res.append(v)
        m,n,p = map(int,input().split())
        
    [print(i) for i in res]
    
if __name__ == "__main__":
    main()