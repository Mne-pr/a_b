import sys
input = sys.stdin.readline
 
def main():
    end = int(input())
    res = 0
    
    for i in range(1,end+1):
        t = sum([int(c) for c in str(i)])
        if i % t == 0:
            res += 1
            
    print(res)

if __name__ == "__main__":
    main()
