import sys
input = sys.stdin.readline

def main():
    T = int(input())
    res = 0
    
    ac = int(input())
    a = list(map(int,input().split()))
    amap = {}

    # a의 누적합 계산하기 - 구간별 sum 함수 갈기는 것 보다 일일이 더해서 추가하는 것
    for i in range(ac):
        t = 0
        for j in range(i,ac):
            t += a[j]
            amap[t] = amap.get(t,0) + 1 # get 실패하면 두 번째 인자를 반환한대..
    
    bc = int(input())
    b = list(map(int,input().split()))
    
    # b의 누적합 계산과 동시에 만족하는지 확인        
    for i in range(bc):
        t = 0
        for j in range(i,bc):
            t += b[j]
            res += amap.get(T-t,0)
    
    print(res)
    
if __name__ == "__main__":
    main()