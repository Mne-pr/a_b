from sys import stdin
input = stdin.readline

def main():
    res = 0
    n = int(input())
    l = int(input())
    inp = input().rstrip()
    
    cur = 0
    grade = 0
    while cur <= l-3:
        if inp[cur:cur+3] == 'IOI':
            grade += 1
            cur += 2
            if grade >= n:
                res += 1
        else:
            cur += 1
            grade = 0
    print(res)
    
if __name__ == "__main__": 
    main()