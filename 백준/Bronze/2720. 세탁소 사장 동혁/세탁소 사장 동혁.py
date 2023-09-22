test = int(input())

price = [25, 10, 5, 1]
ans = []

for i in range(test):
    inp = int(input())
    ans = [0]*4
    
    for j in range(4):
        ans[j] = inp // price[j]
        inp = inp % price[j]
            
    for j in ans:
        print('%d '%j,end='')