sum = 0
inp = list(map(int,input().split()))

for i in inp:
    sum += i**2
    
print(sum%10)