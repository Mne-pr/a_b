start = 2
plus= 1

step = int(input())

for _ in range(step):
    start += plus
    plus *= 2
    
print(start**2)