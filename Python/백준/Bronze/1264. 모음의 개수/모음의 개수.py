from sys import stdin
input = stdin.readline

def main():
    res = []
    inp = input().rstrip().lower()
    
    while inp != '#':
        count = 0
        for c in inp:
            if c in ['a','e','i','o','u']:
                count += 1
        res.append(count)
        inp = input().rstrip().lower()
    
    list(map(lambda x: print(x), res))
    
if __name__ == "__main__": 
    main()