inp = int(input())
step = 1

while(inp-step > 0):
    inp -= step
    step += 1
    
x,y=step,1
# inp - 빼고 남은 것
# step - 단계

if (step % 2 == 1):
    x -= (step - inp)
    y += (step - inp)
else:
    x -= (inp -1)
    y += (inp -1)

print("%d/%d"%(y,x))