# 10250 ACM 호텔
import math

res = []

for _ in range(int(input())):
    H,W,N = map(int,input().split())
    ww = math.ceil(N/H)
    hh = N%H
    if (hh == 0):
        hh = H
    
    if (len(str(ww)) == 1):
        res.append(str(hh)+'0'+str(ww))
    else:
        res.append(str(hh)+str(ww))
    
for i in res:
    print(i)