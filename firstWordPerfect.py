# import math
import copy
from datetime import date
from sys import platform
if platform == "win32": import winsound

# Comment or uncomment the 2nd line to toggle debug
debug = True
debug = False

# lists = "officialAnswers"
# baseFolder = "WordLists/"
# listPath =  baseFolder + lists
guessCounter = 0
totalGuesses = 0
totalSuccess = 0
totalFail = 0


def alarm(frequency = None, duration = None, repeat = None):

    if repeat == None: repeat = 1
    if frequency == None: frequency = 350  # Set Frequency To 3500 Hertz
    if duration == None: duration = 100  # Set Duration To 100 ms == 0.1 second

    while repeat > 0:
        if platform == "win32": winsound.Beep(frequency, duration)
        else: print("\a")
        repeat -= 1


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


def checkWords(day = None):

    global usedList
    global remainingList

    if day == None:
        today = date.today()
        startingDate = date(2021, 6, 19)
        delta = today - startingDate
        day = delta.days
        print("#" + str(day)) # DEBUG

    if day > len(usedList):
        day = len(usedList)

    for i in range(day):
        remainingList.remove(usedList[i])

def remainingListGenerator():

    userInput = input("Enter puzzle # or press " + '\033[1m' + "enter" + '\x1B[0m' + ": ")

    if userInput == "": checkWords()
    else: checkWords(userInput)

# allAnswers = loadList("officialAnswers")
allAnswers = copy.copy(remainingList)
# curAnswer = allAnswers[0]

# answerList = loadList("officialAnswers")

def guessChecker(guess, results):

    # global answerList
    global guessCounter
    global totalGuesses
    global totalSuccess
    global totalFail
    totalGuesses += 1
    # guessCounter += 1
    previousList = copy.copy(answerList)

    if debug:
        print(previousList)

    greens = ['','','','','']
    yellows = {}
    blanks = {}

    gCount = 0
    yCount = 0
    bCount = 0

    for i in range(len(results)):

        if results[i] == 'b' or results[i] == 'B' or results[i] == '-':

            blanks.setdefault(guess[i], []).append(i)

        if results[i] == 'g' or results[i] == 'G' or results[i] == '+':

            greens[i] = guess[i]

        if results[i] == 'y' or results[i] == 'Y' or results[i] >= '0' and results[i] <= '9':

            yellows.setdefault(guess[i], []).append(i)


    for word in previousList:

        for letter in blanks:

            if letter in word:


                if letter in greens or letter in yellows:

                    if letter in greens:

                        for position in range(len(greens)):

                            if word[position] == letter and greens[position] != letter:

                                if word in answerList:

                                    answerList.remove(word)
                                    bCount += 1

                    if letter in yellows:

                        for position in yellows[letter]:

                            if word[position] == letter:

                                if word in answerList:

                                    answerList.remove(word)
                                    bCount += 1

                else:

                    if word in answerList:

                        answerList.remove(word)
                        bCount += 1

        for letter in yellows:

            if letter not in word:

                if word in answerList:

                    answerList.remove(word)
                    yCount += 1

            elif letter in word:

                for position in yellows[letter]:

                    if word[position] == letter:

                         if word in answerList:

                            answerList.remove(word)
                            yCount += 1

        for letter in range(len(greens)):


            if greens[letter] != '':
                if word[letter] != greens[letter]:

                    if word in answerList:

                        answerList.remove(word)
                        gCount += 1

    if debug:
        print(answerList)
        print("bCount: ", bCount)
        print("gCount: ", gCount)
        print("yCount: ", yCount)
        print("Remaining: ", len(answerList))

    if len(answerList) == 1:
        totalGuesses += 1
        totalSuccess += 1
        output = answerList[0]
        # totalGuesses += guessCounter
        if debug: print("The bot took", guessCounter, "tries to find:", output)

            # answerList = copy.copy(allAnswers) # DELETE
            # temp = guessChecker("saine",checkGuess("saine")) # DELETE
            # while temp != curAnswer: # DELETE
            #     temp = guessChecker(temp, checkGuess(temp)) # DELETE
        if guessCounter > 6:
            totalSuccess -= 1
            totalFail += 1
            totalGuesses -= guessCounter
            print("The bot took", guessCounter, "tries to find:", output)

        guessCounter = 1
        # answerList = loadList("officialAnswers")
        return output
        # quit()
    elif len(answerList) < 1:
        totalFail += 1
        # totalGuesses += guessCounter
        if debug: print("Something went wrong after", guessCounter, "tries")
        guessCounter = 1
        print(answerList)
        print(curAnswer)
        # answerList = loadList("officialAnswers")
        
        return(curAnswer) # TODO try returning nothing instead

    else:

        guessCounter += 1
        
        temp = frequency(answerList)
        if temp == curAnswer:
            if guessCounter == 1:
                if debug: print("The bot took", guessCounter, "tries to guess:", temp)
            totalSuccess += 1
            guessCounter = 1
            # totalGuesses += guessCounter
        return temp

def freqCalc(letterFreq, spotFreq, word):

    totalFreq = 0
    spotSum = 0

    for i in range(len(word)):

        totalFreq += letterFreq[ord(word[i]) - ord('a')]
        spotSum += spotFreq[ord(word[i]) - ord('a')][i]

    return[totalFreq, spotSum]



def comboSort(n):
    return n[0]/2 + n[1]


def frequency(inputCombo):

    alphabet = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # Count frequency of all letters in each position
    for word in answerList:


        for letter in range(len(word)):
            alphabet[ord(word[letter]) - ord('a')][letter] += 1

    # Count total frequency of each letter
    totals = [0] * 26
    for i in range(26):

        for j in range(5):

            totals[i] += alphabet[i][j]

    totalSum = 0
    spotSum = 0

    order = []

    for guess in inputCombo:

        temp = freqCalc(totals, alphabet, guess)

        temp.append(guess)

        order.append(temp)

    order.sort(key = comboSort)

    best = order[-1]
    
    for combo in order:

        unique = True

        for i in range(len(combo[2])):
            for j in range(len(combo[2])):

                if combo[2][i] == combo[2][j] and i != j:
                    unique = False

        if unique:
            best = combo

    return best[2]


def listParser(input):

    if "', '" in input:
        inputList = input.split(', ')
        if debug:
            print("Splitting with: ', '")
    elif ', ' in input:
        inputList = input.split(', ')
        if debug:
            print("Splitting with: ,")
    elif '\' ' in input:
        inputList = input.split('\' ')
        if debug:
            print("Splitting with: \'")
    elif '; ' in input:
        inputList = input.split('; ')
        if debug:
            print("Splitting with: ; ")
    elif '. ' in input:
        inputList = input.split('. ')
        if debug:
            print("Splitting with: . ")
    elif ': ' in input:
        inputList = input.split(': ')
        if debug:
            print("Splitting with: : ")
    elif '][' in input:
        inputList = input.split('][')
        if debug:
            print("Splitting with: ][")
    elif '|' in input:
        inputList = input.split('|')
        if debug:
            print("Splitting with: |")
    else:
        inputList = input.split()
        if debug:
            print("Splitting with spaces")

    frequency(inputList)

def checkGuess(guess):

    result = ['b','b','b','b','b']
    greens = []

    # a letter can be marked yellow even if it exists in more than 1 location and 

    for i in range(len(guess)):
        # if guess[i] not in curAnswer:
        #     result[i] = 'b'
        # else:
        if guess[i] in curAnswer:
            if guess[i] == curAnswer[i]:
                result[i] = 'g'
            else:
                result[i] = 'y'

    return result



def wordleBot():

    global curAnswer
    # global allAnswers
    global answerList
    global totalFail
    global totalGuesses
    global totalSuccess


    
    # seconds = []
    commonFails = []

    # possibleGuesses = loadList("officialGuesses")
    
    # Traverse potential first words backwards to try to speed it up
    # for firstWord in reversed(allAnswers):
    for firstWord in remainingList:
        # firstWord = "party"
        print(firstWord)
    # for firstWord in possibleGuesses:
        answerList = copy.copy(remainingList)
        count = 0
        totalFail = 0
        totalGuesses = 0
        totalSuccess = 0

        for curAnswer in commonFails:

            answerList = copy.copy(remainingList)
            temp = guessChecker(firstWord,checkGuess(firstWord))

            while temp != curAnswer:
                temp = guessChecker(temp, checkGuess(temp))

            if totalFail > 0:
                break

        if totalFail > 0:
                continue
        else:
            answerList = copy.copy(remainingList)
            totalFail = 0
            totalGuesses = 0
            totalSuccess = 0


        for curAnswer in remainingList:
            count += 1
        
            answerList = copy.copy(remainingList)
            temp = guessChecker(firstWord,checkGuess(firstWord))
            # print("Results:", checkGuess("saine"), "->", temp)
            # if temp not in seconds:
            #     seconds.append(temp)
            

            while temp != curAnswer:
                temp = guessChecker(temp, checkGuess(temp))

            if totalFail > 0:
                if curAnswer not in commonFails:
                    commonFails.append(curAnswer)
                    with open("WordLists/NewLists/CommonFails", 'a') as common:
                        common.write(curAnswer)
                        common.write(", ")
                    break



            # if count % 1000 == 0:
            #     # print(count, " Answers found:", totalSuccess, "Answers failed:", totalFail, "Current Answer:", curAnswer)
            #     averageGuesses = totalGuesses / count
            #     print("The bot has taken an average of", format(averageGuesses, ".3f"),"guesses to find", totalSuccess, "of", count, "words so far")
        else:
            # print(listParser(seconds))
            # seconds.sort()
            # print(seconds)

            if totalFail < 2:
                averageGuesses = totalGuesses / (count - totalFail)
                averageSuccess = 100 * totalSuccess / count
                outputStr = "The word: \'" + firstWord +  "\' took " + str(format(averageGuesses, ".3f")) + " guesses on average for " + str(totalSuccess) + " of " + str(len(remainingList)) + " total words. Amounting to a success rate of " + str(format(averageSuccess, ".2f")) + "%\n"
                print(outputStr)
                with open("Outputs/perfectfirstWords", 'a') as firstWordOutput:
                    firstWordOutput.write(outputStr)

def main():

    remainingListGenerator()

    wordleBot()


if(__name__ == '__main__'):
    main()