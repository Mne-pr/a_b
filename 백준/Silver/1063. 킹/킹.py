import sys
input = sys.stdin.readline
 
def main():
    inp = input().split()
    king = [ord(inp[0][0]),int(inp[0][1])]
    dol  = [ord(inp[1][0]),int(inp[1][1])]
    
    ctl = { 
        "R" : [1,0], "L" : [-1,0], "B" : [0,-1], "T" : [ 0, 1],
        "RT": [1,1], "LT": [-1,1], "RB": [1,-1], "LB": [-1,-1]
    }
    
    for i in range(int(inp[-1])):
        com = input().strip()
        
        # 왕이 갈 지점
        ktmp = [king[0]+ctl[com][0], king[1]+ctl[com][1]]
        
        # 그 지점에 돌이 있는지
        if ktmp[0] == dol[0] and ktmp[1] == dol[1]:
            # 돌 가는 길에 벽이 없는지
            dtmp = [dol[0]+ctl[com][0], dol[1]+ctl[com][1]]
            if (65 <= dtmp[0] <= 72) and (1 <= dtmp[1] <= 8):
                dol  = dtmp
                king = ktmp
            else:
                continue
        # 돌이 없다면 벽이 있는지
        elif (65 <= ktmp[0] <= 72) and (1 <= ktmp[1] <= 8):
            king = ktmp

    print(chr(king[0]),king[1],sep='')
    print(chr(dol[0]),dol[1],sep='')
    
if __name__ == "__main__":
    main()
