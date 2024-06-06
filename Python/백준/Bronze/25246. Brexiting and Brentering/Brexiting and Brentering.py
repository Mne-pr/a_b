import sys
input = sys.stdin.readline

def main():
    inp = input()
    idx = 0
    for char in inp[::-1]:
        if char in ["a","e","i","o","u"]:
            break
        idx += 1
    
    print(inp[0:len(inp)-idx] + "ntry")

if __name__ == "__main__": 
    main()
