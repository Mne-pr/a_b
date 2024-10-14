import sys
import math
input = sys.stdin.readline
 
def main():
    res = []
    
    while True:
        inp = input().split()
        if inp[0] == "0.0" and inp[1] == "0":
            break
        
        hives = []
        dup = set()
        for i in range(int(inp[1])):
            hives.append(list(map(float,input().split())))
            
        # hives끼리 비교
        for cur1 in range(len(hives)):
            for cur2 in range(cur1+1, len(hives)):
                if ( math.sqrt((hives[cur1][0]-hives[cur2][0])**2 + (hives[cur1][1]-hives[cur2][1])**2 )) <= float(inp[0]):
                    dup.add(cur1)
                    dup.add(cur2)
        
        res.append([len(dup),int(inp[1])-len(dup)])

    for item in res:
        print(f"{item[0]} sour, {item[1]} sweet")

if __name__ == "__main__":
    main()
