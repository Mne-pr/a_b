from sys import stdin
input = stdin.readline

def main():
    T = 'I'
    res = 0
    
    for _ in range(int(input())):
        T += 'OI'

    l = int(input())
    inp = input().rstrip()
    
    lt = len(T)
    for i in range(l-lt+1):
        if inp[i:i+lt] == T:
            res += 1
    
    print(res)
    
if __name__ == "__main__": 
    main()