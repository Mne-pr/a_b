dic = {}
inp = []
for _ in range(3):
    inp.append(int(input()))
R = list(str(inp[0]*inp[1]*inp[2]))

for i in R:
    if (i not in dic):
        dic[i] = 0
    dic[i] += 1
    
for i in range(10):
    index = str(i)
    if (index in dic):
        print(dic[index])
    else:
        print('0')