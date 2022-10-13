from pathlib import (
    Path,
)  # I got this code from this website: https://www.easytweaks.com/python-write-to-text-file/
import os.path
from os.path import (
    exists,
)  # got this code from: https://www.pythontutorial.net/python-basics/python-check-if-file-exists/
import time


def fileCheck(playerName):
    dir_path = Path("playerFiles/")
    pFileName = playerName + ".txt"
    pathToFile = dir_path.joinpath(pFileName)
    if os.path.exists(pathToFile):
        # file is there
        return True
    else:
        # file is not there
        return False


def playerMake(playerName):
    if fileCheck(playerName) == True:
        print("You already have a file with us please go to menu option 'c'")
    elif fileCheck(playerName) == False:
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "w")
        playerFile.write(playerName)
        print("File created successfuly!")
        time.sleep(1)


def checkStats(playerName):
    if fileCheck(playerName) == False:
        print("File does not exist! Please go to menu option 'd'")
    elif fileCheck(playerName) == True:
        print("Welcome back ", playerName)
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "r")
        # Find total of "Win"
        winWord = "Win"
        loseWord = "Lose"
        winTotal = 0
        loseTotal = 0
        for line in playerFile:
            words = line.split()
            for i in words:
                if i == winWord:
                    winTotal = winTotal + 1
                if i == loseWord:
                    loseTotal = loseTotal + 1
        return winTotal, loseTotal


def gameWon(playerName):
    if fileCheck(playerName) == False:
        print("You don't have a player file! We will make one and save your win!")
        playerMake(playerName)
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "a+")
        playerFile.write("\n")
        playerFile.write("Win")
    elif fileCheck(playerName) == True:
        print("Saving your win!")
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "a+")
        playerFile.write("\n")
        playerFile.write("Win")


def gameLost(playerName):
    if fileCheck(playerName) == False:
        print(
            "Hmm, looks like you dont have a player file! Lets fix that, so we can remeber this loss forever."
        )
        playerMake(playerName)
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "a+")
        playerFile.write("\n")
        playerFile.write("Lose")
    elif fileCheck(playerName) == True:
        print("Think of this as a learning opportunity")
        dir_path = Path("playerFiles/")
        pFileName = playerName + ".txt"
        pathToFile = dir_path.joinpath(pFileName)
        playerFile = open(pathToFile, "a+")
        playerFile.write("\n")
        playerFile.write("Lose")
