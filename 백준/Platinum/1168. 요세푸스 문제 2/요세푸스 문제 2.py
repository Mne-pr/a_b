import sys
input = sys.stdin.readline

def mt(tree,node,start,end):
    if start == end:
        tree[node] = 1
    else:
        mid = (start+end)//2
        tree[node] = mt(tree,node*2,start,mid) + mt(tree,node*2+1,mid+1,end)

    return tree[node]

def main():
    n,k = list(map(int,input().split()))
    # 추후수정
    tree=[0]*n*4

    # 트리 생성
    mt(tree,1,1,n)

    print('<',end='')

    idx = 1
    kmo = k-1
    for i in range(n):
        # 다음에 죽일 놈 위치 찾기
        idx += kmo
        cursize = n-i

        idx %= cursize
        if idx == 0:
            idx = cursize

        # 다음에 죽을 놈 등번호 찾고 없애기
        target = idx
        node = 1
        start = 1
        end = n
        while True:
            if start == end:
                while node != 0:
                    tree[node] -= 1
                    node //= 2
                break
            else:
                mid = (start+end)//2
                if target <= tree[node*2]:
                    node = node*2
                    end = mid
                else:
                    target -= tree[node*2]
                    node = node*2+1
                    start = mid+1

        # 찾았으니 출력
        if i < n-1:
            print(start,end=', ')
        else:
            print(start,end='>')
            break

if __name__ == "__main__":
    main()