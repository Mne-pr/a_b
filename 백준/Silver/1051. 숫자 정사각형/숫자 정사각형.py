h, w = list(map(int,input().split()))

lis = [ ]

ans = 0
temp = 0

for i in range(h):
    lis.append( list(input()) )
    
for i in range(h):
    for j in range(w):
        target = lis[i][j]
        #print('target = ',target)
        
        for t in range(j,w):
            if (lis[i][t] == target):
                if (i+(t-j) > h-1):
                    break
                if (lis[i][j] == lis[i+(t-j)][j] and lis[i][j] == lis[i+(t-j)][t]):
                    #print(i,',',j,' == ',i+(t-j),',',j,' == ',i,',',t,' == ',i+(t-j),',',t)
                    temp = (t-j+1)*(t-j+1)
                    if (ans < temp):
                        ans = temp
            else:
                continue
print(ans)