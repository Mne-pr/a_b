import sys
input = sys.stdin.readline

# depth
def DFS(V,inp):
    if inp.get(V) == None:
        return
    stack = inp[V].copy()
    poped = [V]
    while stack:
        val = stack.pop(0)
        if val in poped:
            continue
        poped.append(val)
        print(val,end=' ')
        stack = inp[val] + stack

# breadth
def BFS(V,inp):
    if inp.get(V) == None:
        return
    queue = inp[V].copy()
    poped = [V]
    while queue:
        val = queue.pop(0)
        if val in poped:
            continue
        poped.append(val)
        print(val,end=' ')
        queue = queue + inp[val]

def main():
    N,M,V = map(int,input().split())
    inp={}

    for i in range(M):
        a,b = map(int,input().split())
        if inp.get(a) == None:
            inp[a] = [b]
        else:
            inp[a].append(b)
            
        if inp.get(b) == None:
            inp[b] = [a]
        else:
            inp[b].append(a)

    for i in inp.values():
        i.sort()

    print(V,end=' ')
    DFS(V,inp)
    print(f'\n{V}',end=' ')
    BFS(V,inp)

if __name__ == "__main__": 
    main()
