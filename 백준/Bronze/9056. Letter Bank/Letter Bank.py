import sys
input = sys.stdin.readline
 
def main():
    n = int(input())
    res = []
    for _ in range(n):
        bank, word = input().split()
        
        if sorted(list(bank)) == sorted(list(set(word))):
            res.append('YES')
        else:
            res.append('NO')
        
    for item in res:
        print(item)
        
if __name__ == "__main__":
    main()
    