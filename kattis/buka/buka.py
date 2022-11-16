def main():
    firstIn = input() #this is the first number
    operIn = input() #operation to do
    lastIn = input() #last var that will be sent in

    firstNum = int(firstIn)
    secondNum = int(lastIn)

    if operIn == '+':
        print(firstNum + secondNum)
    elif operIn == '*':
        print(firstNum * secondNum)


if __name__ == "__main__":
    main()