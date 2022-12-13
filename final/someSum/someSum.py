def main():
    n = int(input())
    
    test = n % 4

    if test == 0:
        print("Even")
    elif test == 2:
        print("Odd")
    else:
        print("Either")

if __name__ == "__main__":
    main()

    