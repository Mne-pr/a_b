import sys
input = sys.stdin.readline

def main():
    gplist = { 'Y':1,'F':2,'O':3 }
    
    N, G = input().split()
    inp = [input().rstrip() for i in range(int(N))]
    nop = len(set(inp))
    
    print(nop//gplist[G])
        
if __name__ == "__main__":
    main()