t1 = list(map(int, input().split()))
t2 = list(map(int, input().split()))

t1s = t1[0]+t1[1]*2+t1[2]*3
t2s = t2[0]+t2[1]*2+t2[2]*3

if t1s > t2s:
    print('1')
elif t1s == t2s:
    print('0')
else:
    print('2')