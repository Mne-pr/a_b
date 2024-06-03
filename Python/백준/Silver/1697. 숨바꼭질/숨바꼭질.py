import sys
input = sys.stdin.readline
from collections import deque

# BFS 인데 거를 건 거르자 문제인듯
def main():
    N,K = map(int,input().split())
    
    if (N >= K):
        print(N-K); return
    
    # 큐 한개, 거를여부(방문)와 계산횟수가 visit 배열로 한 번에..
    queue = deque([N])
    visit = [0]*100001
    
    while queue:
        tar = queue.popleft()
        
        if tar == K:
            print(visit[tar]); return
            
        for i in [tar+1,tar-1,tar*2]:
            if 0 <= i <= 100000 and visit[i] == 0:
                visit[i] = visit[tar]+1 
                queue.append(i)

if __name__ == "__main__": 
    main()