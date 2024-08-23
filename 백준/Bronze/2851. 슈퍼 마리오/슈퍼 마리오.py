cur = 0

for i in map(int,open(0)):
    
    if abs(cur - 100) >= abs(cur + i - 100):
        cur += i
    else:
        break
        
print(cur)