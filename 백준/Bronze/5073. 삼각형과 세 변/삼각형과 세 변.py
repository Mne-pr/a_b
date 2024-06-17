import sys
input = sys.stdin.readline
 
# 삼각형이 되는지를 먼저
def main():
    res = []
    ip = sorted(list(map(int,input().split())))
    
    while ip != [0,0,0]:
        ipp = len(set(ip))
          
        if ip[-1] >= ip[0]+ip[1]:
            res.append(0)
        else:
            ipp = len(set(ip))
            if   ipp == 1:
                res.append(1)
            elif ipp == 2:
                res.append(2)
            else:
                res.append(3)
        
        
        ip = sorted(list(map(int,input().split())))
        
    for item in res:
        if   item == 1:
            print('Equilateral')
        elif item == 2:
            print('Isosceles')
        elif item == 3:
            print('Scalene')
        else:
            print('Invalid')
    
 
if __name__ == "__main__":
    main()