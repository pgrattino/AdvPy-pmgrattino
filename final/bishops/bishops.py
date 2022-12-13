from sys import stdin

def main(n):
    n = int(n)
    if n == 1:
        print(1)
    if n > 1:
        print (2 * n - 2)

def userIn():
    for line in stdin.readlines():
        main(line.rstrip())

if __name__ == "__main__":
    userIn()