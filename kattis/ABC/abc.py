import sys

def main():
    userInNum = [] * 3
    userInNum = input().split() #the 3 numbers that will be inputed
    userInLet = input() #the order that the numbers should be in
    userInNum.sort(key=int) #sorting the numbers to make assigning them easy

    #assigning the numbers to their letters
    a = userInNum[0]
    b = userInNum[1]
    c = userInNum[2]

    userInLet = [*userInLet] # make the string into an array of letters

    output = ""

    for i in userInLet:
        if i == 'A':
            output = output + a + " "
        elif i == 'B':
            output = output + b + " "
        elif i == 'C':
            output = output + c + " "
    
    print(output.strip())

def test():
    input1_1 = ["1 2 3"]
    input1_2 = ["ABC"]




if __name__ == "__main__":
    main()