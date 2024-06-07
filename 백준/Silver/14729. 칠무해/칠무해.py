import sys
input = sys.stdin.readline

def main():
    N = int(input())
    inp=[]
    
    for i in range(N):
        inp.append(float(input()))
        
    inp.sort()
    
    for i in range(7):
        print('%.3f'%(inp[i]))
        
if __name__ == "__main__":
    main()