from datetime import date

# Comment or uncomment the 2nd line to toggle debug
debug = True
debug = False


def loadList(name):

    if name == '1' or  name == 1: name = "officialAnswers"
    elif name == '2' or  name == 2: name = "officialGuesses"
    elif name == '3' or  name == 3: name = "wordleAnswers"
    elif name == '4' or  name == 4: name = "wordleGuesses"

    listPath = "WordLists/" + name

    # Open the specificied list
    with open(listPath) as listFile:

        # Copy the word list to memory to return
        WordList = listFile.read().splitlines()

    return WordList


remainingList = loadList("officialAnswers")
usedList = loadList("usedAnswers")


def writeRemaining():

    global remainingList

    with open("WordLists/remainingAnswers", 'w') as remainingFile:

        for unused in remainingList:
            remainingFile.write(unused)
            remainingFile.write("\n")

    with open("Outputs/remainingAnswers", 'w') as remainingFile:

        for unused in remainingList:
            remainingFile.write(unused)
            remainingFile.write("\n")

    print("Remaining answer list generated")


def checkWords(day = None):

    global usedList
    global remainingList

    if day == None:
        today = date.today()
        startingDate = date(2021, 6, 19)
        delta = today - startingDate
        day = delta.days
        if debug: print(day) # DEBUG

    if day > len(usedList):
        day = len(usedList)

    for i in range(day):
        remainingList.remove(usedList[i])

    writeRemaining()


def remainingListGenerator():

    userInput = input("Enter puzzle # or press " + '\033[1m' + "enter" + '\x1B[0m' + ": ")

    if userInput == "": checkWords()
    else: checkWords(userInput)


def main():

    remainingListGenerator()


if(__name__ == '__main__'):
    main()