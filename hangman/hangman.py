#!/Users/peyton/Library/Python
import random


def words():
    for _ in range(1):
        numOfWord = random.randint(1, 20)
    wordBank = open("word.txt")
    wordlines = wordBank.readlines()
    useWord = wordlines[numOfWord - 1]
    useWord = useWord.strip()
    return useWord


print(words())
