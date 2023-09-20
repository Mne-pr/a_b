N, M = list(map(int,input().split()))
tree_list = list(map(int,input().split()))
trees = {}

for i in tree_list:
    if (i not in trees.keys()):
        trees[i] = 1
    else:
        trees[i] += 1

s,e = 0,max(trees)
ans = 0

while(s <= e):
    H = (s+e) // 2
    res = 0
    
    for i in trees.keys():
        if i > H:
            res += (i - H) * trees[i]
        
    #print('s:',s,'e:',e,'mid:',H,'res:',res)
    
    if res < M:
        e = H - 1
    else:
        if H > ans:
            #print('ans <-',H)
            ans = H
        s = H + 1
        
print(ans)