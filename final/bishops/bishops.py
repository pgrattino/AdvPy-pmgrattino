def solve(n):
    while True:
        try:
            if n == '':
                break
            else:
                if int(n) == 1:
                    print(1)
                if int(n) > 1:
                    print (2 * int(n) - 2)
        except KeyboardInterrupt:
            quit()

def userIn():
    n = input()
    solve(n)

if __name__ == "__main__":
    userIn()