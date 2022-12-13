def main():
    while True:
        try:
            n = input()

            if n == '':
                break
            else:
                if int(n) == 1:
                    print(1)
                if int(n) > 1:
                    print (2 * int(n) - 2)
        except KeyboardInterrupt:
            quit()



if __name__ == "__main__":
    main()