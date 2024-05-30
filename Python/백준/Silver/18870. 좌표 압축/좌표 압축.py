import sys
input = sys.stdin.readline

def main():
    n = int(input())
    inp = list(map(int,input().split()))
    inpmap = {}
    
    for idx, item in enumerate(sorted(set(inp))):
        inpmap[item] = idx
     
    for item in inp:
        print(inpmap[item],end=' ')

if __name__ == "__main__": 
    main()