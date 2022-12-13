from sys import stdin

def main(n):
    if n == 1:
        print(1)
    if n > 1:
        print (2 * n - 2)

def userIn():
    n = int(stdin.readline())
    main(n)

if __name__ == "__main__":
    userIn()