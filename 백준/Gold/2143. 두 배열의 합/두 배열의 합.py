import sys
input = sys.stdin.readline

# 두 배열의 합
# 배열을 받아서 a인덱스부터 b인덱스까지의 누적합을 미리 구해놓는?
def main():
    call = int(input())
    res = 0
    
    ac = int(input())
    a = list(map(int,input().split()))
    amap = {}
    
    bc = int(input())
    b = list(map(int,input().split()))
    bmap = {}
    
    # 누적합 계산하기
    for i in range(ac):
        for j in range(i+1,ac+1):
            t = sum(a[i:j])
            if amap.get(t) == None:
                amap[t] = 1
            else:
                amap[t] += 1
            
    for i in range(bc):
        for j in range(i+1,bc+1):
            t = sum(b[i:j])
            if bmap.get(t) == None:
                bmap[t] = 1
            else:
                bmap[t] += 1
                        

    for aa in amap.keys():
        tmp = call - aa
        if bmap.get(tmp) != None:
            res += amap[aa]*bmap[tmp]
   
    print(res)
    
if __name__ == "__main__":
    main()
    