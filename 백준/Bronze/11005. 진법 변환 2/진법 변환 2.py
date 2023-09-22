N,B = list(map(int,input().split()))

vals = []
div = 0
maintain = N

while(maintain >= B):
    div = maintain % B
    maintain = maintain // B
    vals = [div] + vals

vals = [maintain] + vals


for i in range(len(vals)):
    if (vals[i] > 9):
        print(chr(ord('A') + vals[i] -10),end='')
    else:
        print(vals[i],end='')
        
