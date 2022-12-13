def main():
    n = int(input())
    bev = input()

    for i in reversed(range(n + 1)):
        if i == 0:
            break
        else:
            if i == 1:
                print(f"{i} bottle of {bev} on the wall, {i} bottle of {bev}.")
                print(f"Take it down, pass it around, no more bottles of {bev}. \n")
            elif i == 2:
                print(f"{i} bottles of {bev} on the wall, {i} bottles of {bev}.")
                print("Take one down, pass it around,", i - 1, " bottle of", bev, "on the wall. \n")
            else:
                print(f"{i} bottles of {bev} on the wall, {i} bottles of {bev}.")
                print("Take one down, pass it around,", i - 1, " bottles of", bev, "on the wall. \n")

if __name__ == "__main__":
    main()