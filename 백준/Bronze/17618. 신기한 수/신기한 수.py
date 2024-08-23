import sys
input = sys.stdin.readline
 

def main():
    end = int(input())
    res = 0
    
    for i in range(1,end+1):
        it = i
        t = 0
        while it > 0:
            t += it % 10
            it = it // 10

        if i % t == 0:
            res += 1
            
    print(res)

if __name__ == "__main__":
    main()
