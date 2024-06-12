from sys import stdin
input = stdin.readline

def main():
    N = int(input())
    res = list(input().rstrip())
    reslen = len(res)
    
    for _ in range(N-1):
        inp = input().rstrip()
        for i in range(reslen):
            if inp[i] != res[i]:
                res[i] = '?'
    
    print(''.join(res))

if __name__ == "__main__": 
    main()