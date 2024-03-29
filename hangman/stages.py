def stage0():
    # This is just all of the ASCII art for the start stage
    print("|________________")
    print("|/              |")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|\_______________")


def stage1():
    # This is the ASCII art for the first wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|")
    print("|")
    print("|")
    print("|")
    print("|\_______________")


def stage2():
    # This is the ASCII art for the second wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|               |")
    print("|")
    print("|")
    print("|")
    print("|\_______________")


def stage3():
    # This is the ASCII art for the third wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|              /|")
    print("|")
    print("|")
    print("|")
    print("|\_______________")


def stage4():
    # This is the ASCII art for the fourth wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|              /|\\")
    print("|")
    print("|")
    print("|")
    print("|\_______________")


def stage5():
    # This is the ASCII art for the 5th wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|              /|\\")
    print("|              /")
    print("|")
    print("|")
    print("|\_______________")


def stage6():
    # This is the ASCII art for the 6th wrong answer
    print("|________________")
    print("|/              |")
    print("|               O")
    print("|              /|\\")
    print("|              / \\")
    print("|")
    print("|")
    print("|\_______________")


def stageControl(tries):
    if tries == 6:
        stage0()
    if tries == 5:
        stage1()
    if tries == 4:
        stage2()
    if tries == 3:
        stage3()
    if tries == 2:
        stage4()
    if tries == 1:
        stage5()
    if tries == 0:
        stage6()
