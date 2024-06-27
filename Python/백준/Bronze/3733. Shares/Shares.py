from sys import stdin
input = stdin.readline

def main():
    res = []
    
    while True:
        inp = input()
        if len(inp) == 0:
            break
        
        x, s = map(int,inp.split())
        res.append(s//(x+1))
    
    for item in res:
        print(item)
        
if __name__ == "__main__": 
    main()