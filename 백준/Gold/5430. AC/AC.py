import sys
input = sys.stdin.readline
from collections import deque

def main():
    T = int(input())
    res = []           
    
    for _ in range(T):
        fs = input().rstrip(); input()
        l  = input().rstrip()
        if l == '[]':
            l = deque([])
        else:
            l = deque(l[1:-1].split(',')) # [], 순으로 거름
        r = 0; t = 0
        
        for f in fs:
            if f == 'D':
                if len(l) == 0:
                    t = 1; break
                else:
                    if r == 0:  l.popleft()
                    else:       l.pop()
            else:
                r = (r+1)%2
        
        if t == 0:
            if r == 1: l.reverse()
            res.append('['+(',').join(list(l))+']')
        else:
            res.append('error')
        
    for item in res:
        print(item)

if __name__ == "__main__":
    main()