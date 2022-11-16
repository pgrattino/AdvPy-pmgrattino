def main():
    spaceAvl, groupsArri = input().split(' ')
    numSpace = int(spaceAvl)
    numGroups = int(groupsArri)
    numGroupsIn = input().split(' ')
    groupSize = [eval(i) for i in numGroupsIn]

    for i in range(0, len(groupSize)):
        if int(groupSize[i] <= numSpace):
            numSpace = numSpace - groupSize[i]
            numGroups = numGroups - 1
    
    print(numGroups)
        


if __name__ == "__main__":
    main()