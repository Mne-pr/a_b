import sys
input = sys.stdin.readline

def main():
    N = int(input())
    INP  = [0]+list(map(int,input().split()))
    res  = [[0,1] for _ in range(N+1)] # 정답과 최소값의 인덱스

    # 현재 최소값의 인덱스
    minn = 1
    
    # 최소값 찾기, 이번에 추가되는 수가 최대라고 가정
    for i in range(1,N+1):
        if INP[minn] > INP[i]:
            minn = i
            
        # 이전 res의 정답과 i-minn 을 비교
        sub = INP[i]-INP[minn]
        if res[i-1][0] < sub:
            res[i] = [sub,minn]
        else:
            res[i] = res[i-1]
        
    print(*[i[0] for i in res[1::]])

if __name__ == "__main__":
    main()