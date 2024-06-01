import sys
input = sys.stdin.readline

# depth
def DFS(V,inp,N):
    print(V,end=' ')
    stack = inp[V].copy()
    poped = [0]*(N+1)
    poped[V] = 1
    
    while stack:
        val = stack.pop(0)
        if poped[val] == 1:
            continue
        poped[val] = 1
        print(val,end=' ')
        stack = inp[val] + stack

# breadth
def BFS(V,inp,N):
    print(V,end=' ')
    queue = inp[V].copy()
    poped = [0]*(N+1)
    poped[V] = 1
    
    while queue:
        val = queue.pop(0)
        if poped[val] == 1:
            continue
        poped[val] = 1
        print(val,end=' ')
        queue = queue + inp[val]

def main():
    N,M,V = map(int,input().split())
    inp=[[] for i in range(N+1)]

    for i in range(M):
        a,b = map(int,input().split())
        inp[a].append(b)
        inp[b].append(a)

    for item in inp:
        item.sort()

    DFS(V,inp,N)
    print()
    BFS(V,inp,N)

if __name__ == "__main__": 
    main()
