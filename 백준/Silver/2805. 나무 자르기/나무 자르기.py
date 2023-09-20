N, M = list(map(int,input().split()))
Klan = list(map(int,input().split()))

s,e = 0,max(Klan)
ans = 0

while(s <= e):
    H = (s+e) // 2
    res = 0
    
    for i in Klan:
        if i > H:
            res += (i - H)
        
    #print('s:',s,'e:',e,'mid:',H,'res:',res)
    
    if res < M:
        e = H - 1
    else:
        if H > ans:
            #print('ans <-',H)
            ans = H
        s = H + 1
        
print(ans)