import sys
input = sys.stdin.readline

def main():
    numDict = {
        0:"zero", 1:"one", 2:"two", 3:"three",
        4:"four", 5:"five", 6:"six", 7:"seven", 
        8:"eight", 9:"nine", 10:"ten"
    }
    
    start, end = map(int, input().split())
    reslist = []
    
    for i in range(start, end+1):
        tmpnum = i
        tmp = ""
        
        for item in str(i):
            tmp += numDict[int(item)]
        reslist.append([i,tmp])
    
    reslist.sort(key=lambda x: x[1])
    
    for i in range(len(reslist)):
        if i >= 10 and i%10 == 0:
            print()
        print(reslist[i][0], end=' ')

if __name__ == "__main__":
    main()