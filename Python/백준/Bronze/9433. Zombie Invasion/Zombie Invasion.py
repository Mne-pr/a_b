from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    res = []
    
    for _ in range(N):
        inp = list(map(int,input().split()))
         
        for i in range(19,0,-1):
            inp[i-1] += inp[i]//2
            inp[i]    = inp[i]%2
            
        res.append(inp)
        
    for item in res:
        for it in item:
            print(it,end=' ')
        print()

if __name__ == "__main__": 
    main()