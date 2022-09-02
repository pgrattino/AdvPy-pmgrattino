#!/Users/peyton/Library/Python
import random
import stages  # This is the ASCII art for the different stages of the game


def words():
    for _ in range(1):
        numOfWord = random.randint(1, 20)  # generating random number
    wordBank = open("word.txt")  # Opening text file
    wordlines = wordBank.readlines()  # Storing the words in a list
    useWord = wordlines[numOfWord - 1]  # Using random number to pick a word in the list
    useWord = useWord.strip()  # Stripping the word of any extra characters
    return useWord  # Return the word for the game


print(words())
stages.stage5()
