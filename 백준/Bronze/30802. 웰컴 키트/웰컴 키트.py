import sys
input = sys.stdin.readline

    
def main():
    N = int(input())
    size = list(map(int,input().split()))
    T,P = map(int,input().split())
    
    res1 = 0
    
    for s in size:
        if s%T == 0:
            res1 += s//T
        else:
            res1 += s//T+1
    print(res1)
    print(N//P, N%P)
    

if __name__ == "__main__":
    main()