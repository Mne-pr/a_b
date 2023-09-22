N,B = input().split()
N,B = list(N),int(B)
Nlen = len(N)

res = 0

for i in range(len(N)):
    cha = N[Nlen -1 -i]
    temp = 0
    if (ord(cha) < ord('A')):
        temp = int(cha)
    else:
        temp = ord(cha) - ord('A') + 10
    res += temp * (B**i)
    
print(res)