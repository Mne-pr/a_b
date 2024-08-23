import sys
input = sys.stdin.readline
 

def main():
    ms = [int(input()) for i in range(10)]
    cur = 0
    pre = 0
    
    for i in range(10):
        pre = cur
        cur += ms[i]
        
        if cur >= 100:
            if 100-pre < cur-100:
                print(pre)
            else:
                print(cur)
            return
    print(cur)
    
if __name__ == "__main__":
    main()
