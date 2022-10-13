#!/Users/peyton/Library/Python
import random
import hangStats
import stages  # This is the ASCII art for the different stages of the game
import os
import time

# I would like to note that I did do this project before so I did copy some of my old code in to this project


def clearScreen():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def words():
    for _ in range(1):
        numOfWord = random.randint(1, 20)  # generating random number
    wordBank = open("word.txt")  # Opening text file
    wordlines = wordBank.readlines()  # Storing the words in a list
    useWord = wordlines[numOfWord - 1]  # Using random number to pick a word in the list
    useWord = useWord.strip()  # Stripping the word of any extra characters
    return useWord  # Return the word for the game


# print(gameWord)
# print(" ".join(wordLength))  # Printing the _ with out the quotes and brackets


def menu():
    print("Welcome to the hangman game!")
    print("a.   Play Game")
    print("b.   Quit Game")
    print("c.   Display status of the player")
    print("d.   Create a new player")
    menuChoice = input()
    if menuChoice == "a":
        clearScreen()
        game(words())
    elif menuChoice == "b":
        exit
    elif menuChoice == "c":
        clearScreen()
        playerName = input("What is your name? ")
        clearScreen()
        win, lose = hangStats.checkStats(playerName)
        if win > lose:
            print("Player Status: Nerd")
        if lose > win:
            print("Player Status: Loser")
        print("Total number of Wins: ", win)
        print("Total number of Losses: ", lose)
        time.sleep(1)
        menu()
    elif menuChoice == "d":
        clearScreen()
        playerName = input("What is your name? ")
        hangStats.playerMake(playerName)
        menu()
    else:
        print("Please enter a valid option")
        menu()


def guess(useWord, wordLength):
    letGuess = input("Pick a letter: ")
    z = 0  # This will indicate if the letter is in the word
    for x, y in enumerate(useWord):  # Traverse the array of our word
        if letGuess == y:  # if letter matches the letter in the array
            wordLength[x] = letGuess
            z += 1
    if z == 0:
        return False
    else:
        return True


def gameProg(tries, useWord, wordLength):
    if tries == 0:
        print("You lost")
    if guess(useWord, wordLength) == False:
        if tries > 0:
            tries -= 1
        else:
            print("You lost")
    return tries


def game(useWord):
    tries = 6
    useWord = useWord.strip()
    wordLength = ["_"] * len(useWord)
    while tries > 0:
        stages.stageControl(tries)
        print("".join(wordLength))
        tries = gameProg(tries, useWord, wordLength)
        if "".join(wordLength) == useWord:
            print("Congrats!! You Won!!")
            playerName = input("What is your name? ")
            hangStats.gameWon(playerName)
            break
        elif tries < 1:
            print("You lost. The correct word was: ", useWord)
            playerName = input("What is your name? ")
            hangStats.gameLost(playerName)
            break
        clearScreen()
    menu()


def main():
    clearScreen()
    menu()


main()
