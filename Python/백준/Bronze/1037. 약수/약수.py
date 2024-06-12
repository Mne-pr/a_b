from sys import stdin
input = stdin.readline

def main():
    N = input()
    inp = list(map(int,input().split()))
    
    print(min(inp)*max(inp))
    
if __name__ == "__main__": 
    main()