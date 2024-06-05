import sys
input = sys.stdin.readline

    
def main():
    A = int(input())
    B = int(input())
    C = int(input())
    
    print(A+B-C)
    
    AB = str(A) + str(B)
    print(int(AB) - C)

if __name__ == "__main__":
    main()
    