from sys import stdin
input = stdin.readline

def main():
    n = int(input())
    a = 65
    l = {}
    r = []
    
    for i in range(65,91):
        l[chr(i)] = i
    
    for i in range(n):
        it = list(input())
        res = 0
        for j in l.keys():
            if j not in it:
                res += l[j]
                       
        r.append(res)
        
    for item in r:
        print(item)

if __name__ == "__main__": 
    main()