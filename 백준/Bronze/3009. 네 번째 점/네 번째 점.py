from sys import stdin
input = stdin.readline

def main():
    x=[]
    y=[]
    for i in range(3):
        nx,ny = map(int,input().split())
        x.append(nx)
        y.append(ny)
        
    tx = x.pop()
    ty = y.pop()
    if tx in x:
        del x[x.index(tx)]
    else:
        x[0] = tx
        
    if ty in y:
        del y[y.index(ty)]
    else:
        y[0] = ty
    
    print(x[0],y[0])
    
    
if __name__ == "__main__":
    main()
        