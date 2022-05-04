from random import randrange
import colorama
from colorama import Fore


def CreateList():
    wordList = []
    with open("wordList.txt", "r") as fileObject: #open file
        for line in fileObject:     #loop through file line by line. one line contains the word plus a useless newline char at the end 
            wordList.append(removeNewline(line)) #insert word into wordList
    return wordList

def removeNewline(line):
    word = ""
    x = 0
    while(line[x] and line[x] != '\n'):
        word = word + line[x]
        x = x + 1
    return word

#returns updated wordList with words that dont contain a certain letter
def removeWords(letter, wordList):
    size = len(wordList)
    newwordList = []
    for x in range(size):
        word  = wordList[x]
        if(contains(word,letter)):
            continue
        else:
            newwordList.append(word)
    return newwordList

def contains(word, letter):
    for x in range(len(word)):
        if(letter in word[x]):
            return 1
    return 0

def containsPosition(word, letter, pos):
    if(word[pos] == letter):
        return 1
    else:
        return 0

#returns a list of words that contains a certain letter in a certain position
def NarrowGreen(letters, wordList): #returns a list with the words that contain a certain letter in a certain position
    newList = []
    for i in range(len(letters)):
        sizeOfList = len(wordList)
        if(i % 2 == 0):
            newList.clear()
            letter = letters[i]
            pos = int(letters[i+1])
            pos = pos - 1
            for x in range(sizeOfList):
                if(containsPosition(wordList[x], letter, pos) == 1):
                    newList.append(wordList[x])
            wordList = newList.copy()
    return newList

#returns a list of all the words that dont contain certain letters
def NarrowGray(letters, wordList):
    tempList = []
    for i in range(len(letters)):
        tempList.clear()
        for x in range(len(wordList)):
            if(contains(wordList[x], letters[i]) == 0):
                tempList.append(wordList[x])
        wordList = tempList.copy()
    return wordList

#returns a list that contains words with that letter except the letter in the certain pos
#Used for the main func when receiving yellow letters from the user.
def NarrowYellow(letters, wordList):
    tempList = []
    
    for i in range(len(letters)):
        if(i % 2 == 0):
            tempList.clear()
            letter = letters[i]
            pos = int(letters[i+1])
            pos = pos - 1
            
            for x in range(len(wordList)):
                if(containsPosition(wordList[x], letter, pos) == 0): #create new list of words that dont have that letter in that pos
                    tempList.append(wordList[x])
            wordList = tempList.copy()
            tempList.clear()
            for x in range(len(wordList)):
                if(contains(wordList[x], letter) == 1): #create a new list that contains the letter 
                    tempList.append(wordList[x])
            
    wordList = tempList.copy()
    return wordList
                    
#MAIN
wordList = CreateList()
proceed = 1
tempList = []
temp = ""
print("Hello and welcome to Worlde Solver v1.0!")
print("This solver will most likely solve the word in 4-5 tries.")
print("---------------------------------------\n")
starterWord = input("What's your starter word gonna be today boss?\n-")
wordList.remove(starterWord)
while(proceed == 1):
    print("If there are any", end=" ")
    print(Fore.GREEN + "GREEN", end=" ")
    print(Fore.WHITE + "letters type in the letter followed by the positon no spaces (Ex. a2b4c1)\n")
    greenletters = input("If there are none type none\n-")
    if(greenletters != "none"):
        templist = NarrowGreen(greenletters, wordList).copy()
        wordList = templist.copy()
        tempList.clear()

    grayLetters = input("If there are any GRAY letters type them in all together(Ex. abc). \nIf there are none type none\n-")
    if(grayLetters != "none"):
        for x in range(len(grayLetters)): #loop through the grayletters to see if any letters is already contained in greenletters 
            if(contains(greenletters, grayLetters[x]) == 0):
                temp = "".join((temp,grayLetters[x]))
        grayLetters = temp
        tempList = NarrowGray( grayLetters, wordList).copy()
        wordList = tempList.copy()
        tempList.clear()

    print("If there are any", end=" ")
    print(Fore.YELLOW + "YELLOW",end=" ")
    yellowLetters = input(Fore.WHITE + "letters, type the letter followed by the position no spaces(Ex. a2b4c1)\nIf there are none type none\n-")
    if(yellowLetters != "none"):
        tempList = NarrowYellow(yellowLetters, wordList).copy()
        wordList = tempList.copy()
        tempList.clear()
    randomNum = randrange(len(wordList))
    randomWord = wordList[randomNum]
    print("My calculations indicate to use the word \"" + randomWord + "\"")
    wordList.remove(randomWord)

#END OF MAIN

