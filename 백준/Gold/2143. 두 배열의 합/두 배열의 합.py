import sys
import bisect
input = sys.stdin.readline

# 두 배열의 합
# 배열을 받아서 a인덱스부터 b인덱스까지의 누적합을 미리 구해놓는?
def main():
    call = int(input())
    res = 0
    
    ac = int(input())
    a = list(map(int,input().split()))
    amap =[]
    
    bc = int(input())
    b = list(map(int,input().split()))
    bmap = []
    
    # 누적합 계산하기
    for i in range(ac):
        for j in range(i+1,ac+1):
            amap.append(sum(a[i:j]))
            
    for i in range(bc):
        for j in range(i+1,bc+1):
            bmap.append(sum(b[i:j]))
            
    bmap.sort()
    
    for aa in amap:
        target = call-aa
        res += bisect.bisect_right(bmap,target) - bisect.bisect_left(bmap,target)
   
    print(res)
    
if __name__ == "__main__":
    main()
    