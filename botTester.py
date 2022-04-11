import math
import copy
# from time import perf_counter

# Comment or uncomment the 2nd line to toggle debug
debug = True
debug = False

lists = "officialAnswers"
baseFolder = "WordLists/"
listPath =  baseFolder + lists
guessCounter = 1
totalGuesses = 0
totalSuccess = 0
totalFail = 0
divider = 1


def loadList(name = None):

    global lists
    global listPath
    global baseFolder

    if name == None: name = lists
    else :
        if name == '1' or  name == 1 or name == "officialAnswers": lists = "officialAnswers"
        elif name == '2' or  name == 2 or name == "officialGuesses": lists = "officialGuesses"
        elif name == '3' or  name == 3 or name == "wordleAnswers": lists = "wordleAnswers"
        elif name == '4' or  name == 4 or name == "wordleGuesses": lists = "wordleGuesses"
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

allAnswers = loadList("officialAnswers")
curAnswer = allAnswers[0]

answerList = loadList("officialAnswers")

def guessChecker(guess, results):

    global answerList
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
    # return n[1] + n[0]
    # return n[1]
    # return n[0]
    # return n[1]/2 + n[0]/5 # NOTE best so far
    # return n[0] * n[0] + n[1] * n[1]
    # return math.sqrt(n[0]) + math.sqrt(n[1])
    # return n[0]/10 + n[1]/5
    # return n[0] - n[1]*2
    return n[0]/divider + n[1]


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


def frequencyGen(input):

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
    global allAnswers
    global answerList
    global divider
    global totalGuesses
    global totalSuccess
    global totalFail

    answerList = copy.copy(allAnswers)



    # while temp != curAnswer:
    #     temp = guessChecker(temp, checkGuess(temp))

    averageSuccess = 0.0
    
    while averageSuccess < 99.9:
        divider += 1
        totalGuesses = 0
        totalFail = 0
        totalSuccess = 0

        count = 0
        
        for curAnswer in allAnswers:
            count += 1
        
            answerList = copy.copy(allAnswers)
            temp = guessChecker("saine",checkGuess("saine"))

            while temp != curAnswer:
                temp = guessChecker(temp, checkGuess(temp))


            if count % 500 == 0:
                # print(count, " Answers found:", totalSuccess, "Answers failed:", totalFail, "Current Answer:", curAnswer)
                averageGuesses = totalGuesses / count
                # print("The bot has taken an average of", format(averageGuesses, ".3f"),"guesses to find", totalSuccess, "of", count, "words so far")
        else:
            averageGuesses = totalGuesses / (count - totalFail)
            averageSuccess = 100 * totalSuccess / count
            print("\nThe bot had an average of", format(averageGuesses, ".3f"), "guesses for", totalSuccess, "of", len(allAnswers), "total words\nAmounting to a success rate of ", str(format(averageSuccess, ".2f")), "%\n")
            print("Divider = ", divider)


def main():

    wordleBot()


if(__name__ == '__main__'):
    main()