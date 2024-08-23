import sys
input = sys.stdin.readline

def main():
    cur = 0
    
    for i in range(10):
        inp = int(input())
        
        if abs(cur - 100) >= abs(cur + inp - 100):
            cur += inp
        else:
            break
            
    print(cur)
    
if __name__ == "__main__":
    main()