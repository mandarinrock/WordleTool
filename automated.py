# DELETE from os.path import exists
import copy
from sys import platform
if platform == "win32": import winsound


# Comment or uncomment the 2nd line to toggle debug
debug = True
# debug = False

# TEMP lists = "officialGuesses"
lists = "NewLists/defaultRunList"
baseFolder = "WordLists/"
listPath =  baseFolder + lists



# terminate() closes @output and ends the program
def terminate(): quit()

def alarm(frequency = None, duration = None, repeat = None):

    if repeat == None: repeat = 1
    if frequency == None: frequency = 350  # Set Frequency To 3500 Hertz
    if duration == None: duration = 100  # Set Duration To 100 ms == 0.1 second

    while repeat > 0:
        if platform == "win32": winsound.Beep(frequency, duration)
        else: print("\a")
        repeat -= 1


def loadList(name = None):

    global lists
    global listPath
    global baseFolder

    if name == None: name = lists
    else :
        if name == '1' or  name == 1: lists = "officialAnswers"
        elif name == '2' or  name == 2: lists = "officialGuesses"
        elif name == '3' or  name == 3: lists = "wordleAnswers"
        elif name == '4' or  name == 4: lists = "wordleGuesses"
        # elif name == '5' or  name == 5: lists = "zenList"
        else:
            lists = name
            baseFolder += "NewLists/"

    listPath = baseFolder + str(lists)

    # Open the specificied list
    with open(listPath) as listFile:

        # Copy the word list to memory to return
        WordList = listFile.read().splitlines()

    return WordList


# saveAnswers(String[] answers) prints a list of strings, copies to output, and calls terminate()
def saveAnswers(answers):

    if debug: print("Saving Answers: ", end="")

    # answerFile holds the output file
    # if lists == "officialAnswers":

    #     fileName = "OfficialAnswerCombos"

    # elif lists == "officialGuesses":

    #     fileName = "OfficialGuessCombos"

    # elif lists == "wordleAnswers":

    #     fileName = "WordleAnswerCombos"

    # elif lists == "wordleGuesses":

    #     fileName = "WordleGuessCombos"

    fileName = "Outputs/" + lists + "Combos"

    with open(fileName, "w") as answerFile:

        commas = 4
        if debug: print("[")
        for word in answers:

            if debug:
                if commas > 0:
                    commas -= 1
                    print(word, end=", ")
                else:
                    print(word, end="]\n")
            answerFile.write("%s " % word)

        answerFile.write("\n")

    # if debug: print("")

    # For each word in answers, copy the word to output file, followed by a comma and a space
    # for word in answers: output.write("'%s', " % word)

    # After copying the combination add a new line
    # else: output.write("\n")

    # output.close()


def saveProgress(comboSave):

    if debug: print("Saving Progress: ", end="")



    with open("guessSave", "w+") as saveFile:

        for saveValue in comboSave:

            if debug: print(saveValue, end=" ")
            saveFile.write("%s " % saveValue)

        saveFile.write("\n")

    if debug: print("")


def loadProgress():

    try:

        with open("guessSave", "r") as loadFile:

            loadLine = loadFile.readline()
            if debug: print("Loaded line: " + loadLine)
            loadList = loadLine.split()
            return loadList

    except:

        print("Save file does not exist")
        return



def makeBackup(newSave = None):

    with open("guessSave", "r") as oldFile: oldLine = oldFile.readline()

    if debug: print("Checking line: " + oldLine)

    oldSave = oldLine.split()
    makeSave = True

    if newSave == None:
        newSave = oldSave
        makeSave = False


    if oldSave[0] >= newSave[0]:

        if debug: print("Backing up: ", end="")

        with open("guessBackups", "a") as backupFile:

            for oldValue in oldSave:
                if debug: print(oldValue, end=" ")
                backupFile.write("%s " % oldValue)

            backupFile.write("\n")
            if debug: print("")

        if makeSave: saveProgress(newSave)







# TODO add function description
def comboGen(comboLen = None, openFrom = None):

    makeBackup()

    # If a number of words in combination is not provided
    if comboLen is None:
        # Then default to 4 words
        comboLen = 4

        

    # Open a word list
    # OLD with open("WordLists/officialGuesses") as listFile:
    # with open("WordLists/officialAnswers") as listFile:

        # Copy the word list to memory as wordList
        # OLD wordList = listFile.read().splitlines()

    # ---------------------- NOTE -----------------------
    # If we think of our combination as a comboLen digit
    # variable with n = length(wordList) possible values
    # for each digit. We can increment the first digit
    # until it reaches n and rolls over to the next digit
    # ---------------------- NOTE -----------------------

    wordList = loadList()

    # Initialize the combination
    combination = [0] * comboLen
    # combination = [0, 0, 0, 0, 0]
    # Initialize the alphabet
    alphabet = []

    if openFrom == None:

        combination = loadProgress()

    elif openFrom != None:

        if debug: print("Printing openFrom in comboGen()", openFrom)

        # if openFrom[-1] >= 0 and openFrom[-1] <= 9:
        j = 0
        for i in openFrom:
            if type(i) is int:
                combination[j] = i
            elif type(i) is str:
                combination.index(i)
            j += 1

    # combination[0] = 99
    # combination

    firstWord = 1 + combination[0]

    printCounter = 0
    answerCount = 0
    counter = 0

    if debug: print(len(wordList)) # DEBUG


    while(combination[0] < len(wordList)):

        counter += 1
        if counter % 1000000 == 1:
            saveProgress(combination)
            # DELETE if debug: print("Printing loadProgress from comboGen()" + loadProgress())

        if firstWord < combination[0]: firstWord = combination[0]
            

        # Clear the alphabet
        alphabet.clear()

        # For every guess in the current combination
        for guess in range(comboLen):

            i = guess
            while combination[i] >= len(wordList):

                if i == 0:
                    print("All combinations checked")
                    if debug: print("Front of the combo reached") # DEBUG
                    quit()
                
                # if debug: print("Rolling Over") # DEBUG
                combination[i] = firstWord
                if combination[i-1] < len(wordList)-1 and combination[i-1] > firstWord:
                    combination[i] = 0 + combination[i-1]
                i -= 1
                combination[i] += 1
                


            # For every letter in the guessed word
            for letter in wordList[combination[guess]]:

                # If the letter has already been used
                if letter in alphabet:

                    # Then skip this word
                    # if(debug):
                    #     print("Skipping word: ", wordList[combination[guess]]) # DEBUG

                    combination[guess] = 1 + combination[guess]
                    break

                else:

                    # Otherwise add the letter to the alphabet
                    alphabet.append(letter)

                    if len(alphabet) >= 23:

                        alarm(450, 200, 1)

                        answerCount += 1

                        answerList = []
                        
                        for answer in combination:

                            answerList.append(wordList[answer])

                        if printCounter <= 0:

                            print(len(alphabet), end= ": ")
                            print(answerList, end=" #")
                            print(answerCount)
                            
                        else:
                            printCounter -= 1

                        print(len(alphabet), end= ": ")
                        print(answerList)
                        # output.write(str(len(alphabet)))
                        # output.write(": ")
                        saveAnswers(answerList)

                        if len(alphabet) == 24:

                            outputPath = "Outputs/" + lists
                            outputPath += " 24+ Unique Letters.txt"

                            with open(outputPath, "a") as quickSave:

                                for values in combination: quickSave.write("%d " % values)
                                quickSave.write("\n")

                                for values in answerList: quickSave.write("%s " % values)
                                quickSave.write("\n")

                            
                            # alarm(350, 150, 3)

                            # printCounter = 10
                            # for jackpot in range(5):
                            print("  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
                            print("   ///////////////////////////////////////\n")
                            print(" ", end="")
                            print(len(alphabet), end= ": ")
                            print(answerList)
                            print("\n   ///////////////////////////////////////")
                            print("  \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ \n")

                        elif len(alphabet) == 25:

                            outputPath = "Outputs/" + lists
                            outputPath += " 25+ Unique Letters.txt"

                            with open(outputPath, "a") as quickSave:

                                for values in combination: quickSave.write("%d " % values)
                                quickSave.write("\n")

                                for values in answerList: quickSave.write("%s " % values)
                                quickSave.write("\n")

                            
                            # alarm(600, 100, 2)

                            # printCounter = 10
                            # for jackpot in range(5):
                            print("///////////////////////////////////////")
                            print("///////////////////////////////////////")
                            
                            print("   ///////////////////////////////////////")
                            print("   ///////////////////////////////////////\n")
                            print(" ", end="")
                            print(len(alphabet), end= ": ")
                            print(answerList)
                            print("\n   ///////////////////////////////////////")
                            print("   ///////////////////////////////////////")
                            
                            print("///////////////////////////////////////")
                            print("///////////////////////////////////////\n")





        
        



    # while len(alphabet) < 25:

        
    # # For each word in the combination
    # for digit in range(comboLen, 0):






def main():

    # print("\nEnable Debugging?")
    # userInput = input("[Y/N]: ")

    # # TODO may need to change this to not [0]
    # if userInput[0] == 'Y':
    #     global debug
    #     debug = True


    # print("\n(1) officialAnswers[2309]\t(3) wordleAnswers[2315]")
    # print("(2) officialGuesses[10638]\t(4) worldeGuesses[10657]")
    # print("\n(1) officialAnswers[", len(loadList(1)), "]\t(3) wordleAnswers[", len(loadList(3)), "]\t(5) zenList[", len(loadList(5)), "]")
    print("\n(1) officialAnswers[", len(loadList(1)), "]\t(3) wordleAnswers[", len(loadList(3)), "]")
    print("(2) officialGuesses[", len(loadList(2)), "]\t(4) worldeGuesses[", len(loadList(4)), "]")

    print("Choose a list to search.")
    # userInput = input("[1/2/3/4]: ")

    loadList("defaultRunList")
    # loadList(userInput)


    comboGen(5, [0,0,0,0,0])



if(__name__ == '__main__'):
    main()