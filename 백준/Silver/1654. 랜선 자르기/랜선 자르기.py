K, N = list(map(int,input().split()))
Klan = [int(input()) for _ in range(K)]

s = 1
e = max(Klan)
mid=0

while(s <= e):
    mid = (s+e) // 2
    res = 0

    for i in Klan:
        res += i // mid

    #print('s:',s,'e:',e,'mid:',mid,'res:',res)

    if res < N:
        e = mid - 1
    else:
        s = mid + 1

print(e)