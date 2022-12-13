def solve(n):
    test = n % 4

    if test == 0:
        print("Even")
    elif test == 2:
        print("Odd")
    else:
        print("Either")

def userIn():
    n = int(input())
    solve(n)

if __name__ == "__main__":
    userIn()

    