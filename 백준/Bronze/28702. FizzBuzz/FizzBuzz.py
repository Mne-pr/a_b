import sys
input = sys.stdin.readline

    
def main():
    i = 0
    for j in range(3):
        inp = input().rstrip()
        if "Fizz" in inp or "Buzz" in inp:
            i += 1
        else:
            i = int(inp)
    
    i += 1
    
    if i%3 == 0:
        if i%5 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif i%5 == 0:
            print("Buzz")
    else:
        print(i)
    

if __name__ == "__main__":
    main()
    
    