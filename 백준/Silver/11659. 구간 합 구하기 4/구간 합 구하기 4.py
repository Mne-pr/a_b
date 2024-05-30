import sys
input = sys.stdin.readline

def main():
    N,M = map(int,input().split())
    inp = list(map(int,input().split()))
    
    res = [0]*(len(inp)+1)
    res[0] = inp[0]
    realres = []
    
    for i in range(1,len(inp)):
        res[i] = res[i-1] + inp[i]
    
    for i in range(M):
        s,e = map(int,input().split())
        realres.append(res[e-1] - res[s-2])
        
    for item in realres:
        print(item)
    
if __name__ == "__main__":
    main()
