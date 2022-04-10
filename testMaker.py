import random
import copy

lists = "officialGuesses"
listPath = "WordLists/" + lists

def loadList(name = None):

    global lists
    global listPath

    if name == None: name = lists
    else :
        if name == '1' or  name == 1: lists = "officialAnswers"
        elif name == '2' or  name == 2: lists = "officialGuesses"
        elif name == '3' or  name == 3: lists = "wordleAnswers"
        elif name == '4' or  name == 4: lists = "wordleGuesses"
        # elif name == '5' or  name == 5: lists = "zenList"
        else: lists = name

    listPath = "WordLists/" + lists

    # Open the specificied list
    with open(listPath) as listFile:

        # Copy the word list to memory to return
        WordList = listFile.read().splitlines()

    return WordList

def makeSet():

    alphabet = []
    testSet = []

    for i in range(26):
        alphabet.append(chr(ord('a') + i))
        random.shuffle(alphabet)

    for i in range(5):

        testWord = ""

        for j in range(5):

            random.shuffle(alphabet)
            randomLetter = alphabet.pop()

            testWord += randomLetter

            # randomLetter = random.choice(alphabet)
            # alphabet.remove(randomLetter)
            # testWord.append(randomLetter)
            # testWord.pop(alphabet)


        testSet.append(testWord)

    return testSet


def writeList(target, modulo, additional):

    targetPath = "WordLists/NewLists/" + target
    additional.sort()

    with open(targetPath, 'w') as targetFile:
        count = 0
        for i in loadList(lists):
            while len(additional) > 0 and additional[0] < i:
                print(additional[0], end="\n")
                targetFile.write(additional.pop(0))
                targetFile.write("\n")


            count += 1
            if count % modulo == 1:
                # output.writeLine(i)
                targetFile.write(i)
                targetFile.write("\n")

    quit()


def customRun():

    print("\n(1) officialAnswers[", len(loadList(1)), "]\t(3) wordleAnswers[", len(loadList(3)), "]")
    print("(2) officialGuesses[", len(loadList(2)), "]\t(4) worldeGuesses[", len(loadList(4)), "]")

    print("Choose a source list.")
    userInput = input("[1/2/3/4]: ")
    WordList = loadList(userInput)

    # TEMP userInput = input("Name the new list: ")
    newName = "tempTest"

    print("Choose a value greater than 1 for n in 1/n to reduce how many terms are used from the original list")
    userInput = int(input("Or enter 1 or 0 to use all words from the original list: "))
    # print(ord(userInput))
    if userInput > 1 and userInput < len(WordList):
        compression = userInput
    else:
        compression = 1


    userInput = int(input("How many test sets should be added to the list? "))
    setNum = userInput

    print("Want to set the random seed? Enter a seed or enter 'Y' for complete random or 'N' a default seed")
    userInput = input("[Seed] or [Y/N]: ")

    if userInput[0] == 'N' or userInput[0] == 'n':
        random.seed(5)
    elif userInput[0] != 'Y' or userInput[0] != 'y':
        random.seed(userInput)

    testWords = []

    for set in range(setNum):
        testWords.extend(makeSet())

    writeList(newName, compression, testWords)
    

def defaultRun():

    WordList = loadList("officialAnswers")

    newName = "defaultRunList"

    compression = 3

    setNum = 3

    random.seed(5)

    testWords = []

    for set in range(setNum):
        testWords.extend(makeSet())

    writeList(newName, compression, testWords)



def main():

    print("Enter 'Y' to start a custom run")
    userInput = input("[Y/N]: ")

    if userInput == 'Y' or userInput == 'y':
        customRun()
    else:
        defaultRun()




if(__name__ == '__main__'):
    main()