import sys
input = sys.stdin.readline
 
# 삼각형이 되는지를 먼저
def main():
    res = []
    ip = sorted(list(map(int,input().split())))
    
    while ip != [0,0,0]:
        ipp = len(set(ip))
          
        if ip[-1] >= ip[0]+ip[1]:
            res.append('Invalid')
        else:
            ipp = len(set(ip))
            if   ipp == 1:
                res.append('Equilateral')
            elif ipp == 2:
                res.append('Isosceles')
            else:
                res.append('Scalene')

        ip = sorted(list(map(int,input().split())))
        
    for item in res:
        print(item)

if __name__ == "__main__":
    main()