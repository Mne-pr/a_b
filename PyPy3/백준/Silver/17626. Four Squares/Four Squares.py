import sys
input = sys.stdin.readline

def main():
    N = int(input())
    res = [0,1]
    
    for i in range(2,N+1):
        mv = N+1
        
        for j in range(1,int(i**(1/2))+1):
            mv = min(mv, res[i-j*j])
        
        res.append(mv+1)

    print(res[N])
    
if __name__ == "__main__": 
    main()