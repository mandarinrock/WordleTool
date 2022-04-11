import copy

# Comment or uncomment the 2nd line to toggle debug
debug = True
# debug = False

lists = "officialAnswers"
# lists = "NewLists/defaultRunList"
baseFolder = "WordLists/"
listPath =  baseFolder + lists




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

answerList = loadList("officialAnswers")

def guessChecker(guess, results):

    global answerList
    previousList = copy.copy(answerList)

    greens = ['','','','','']
    yellows = {}
    blanks = {}

    gCount = 0
    yCount = 0
    bCount = 0

    for i in range(len(results)):

        if results[i] == 'b' or results[i] == 'B' or results[i] >= '-':

            blanks.setdefault(guess[i], []).append(i)

        if results[i] == 'g' or results[i] == 'G' or results[i] >= '+':

            greens[i] == guess[i]

        if results[i] == 'y' or results[i] == 'Y' or results[i] >= '0' and results[i] <= '9':

            yellows.setdefault(guess[i], []).append(i)


    for word in previousList:

        for letter in blanks:

            if letter in word:

                if letter in greens or letter in yellows:

                    if letter in greens:

                        for position in range(len(green)):

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


    print(answerList)
    if debug:
        print("bCount: ", bCount)
        print("gCount: ", gCount)
        print("yCount: ", yCount)
        print("Remaining: ", len(answerList))

    return(answerList)

        

# DELETE guessChecker.answerList = loadList("officialAnswers")

def freqCalc(letterFreq, spotFreq, word):

    totalFreq = 0
    spotSum = 0

    for i in range(len(word)):

        totalFreq += letterFreq[ord(word[i]) - ord('a')]
        spotSum += spotFreq[ord(word[i]) - ord('a')][i]

    return[totalFreq, spotSum]



def comboSort(n):
    return -n[1]


def frequency(inputCombo):

    with open("WordLists/officialAnswers") as listFile:

        wordList = listFile.read().splitlines()

    with open("WordLists/officialGuesses") as guessFile:

        guessList = guessFile.read().splitlines()

    alphabet = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # Count frequency of all letters in each position
    for word in wordList:

        if debug:
            print(word)

        for letter in range(len(word)):

            if debug:
                if debug:
                    print(chr(ord(word[letter]) - ord('a')))
                print("word[letter] = ", end="")
                print(word[letter])
                print("\nord(word[letter]) - ord('a') = ", end="")
                print(ord(word[letter]) - ord('a'))
                print("")
                print(alphabet[ord(word[letter]) - ord('a')])

            alphabet[ord(word[letter]) - ord('a')][letter] += 1

            if debug:
                print(alphabet[ord(word[letter]) - ord('a')])

    # Count total frequency of each letter
    totals = [0] * 26
    for i in range(26):
        if debug:
            print(chr(ord('A') + i), end=": [\t")
        for j in range(4):
            if debug:
                print(alphabet[i][j], end="\t")
            totals[i] += alphabet[i][j]
        if debug:
            print(alphabet[i][4], end="\t]\n")
            print("] ")

    totalSum = 0
    spotSum = 0

    order = []

    for guess in inputCombo:


        temp = freqCalc(totals, alphabet, guess)

        temp.append(guess)

        order.append(temp)

        totalSum += temp[0]
        spotSum += temp[1]

    print("\n    Total Combination Frequency: " + str(totalSum) + "\n    Total Spot Frequency: " + str(spotSum))

    order.sort(key = comboSort)


    print("\n. [", end="")
    commas = 4
    for combo in order:
        if commas > 0:
            print(combo[2], end= ", ")
            commas -= 1
        else:
            print(combo[2], end= "]\n")

    for combo in order:
        print(combo[2] + ": Total Frequency = " + str(combo[0]) + ", Spot Frequency = " + str(combo[1]))

    print("")


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


def secondGuess():

    first = ['s','a','i','n','e']
    wordList = loadList(1)

    printLine = 0

    lastLetter = 'a'
    
    for word in wordList:

        for letter in first:

            if letter in word:

                if word in wordList:
                    wordList.remove(word)

        else:
            if word in wordList:

                printLine += 1

                if printLine % 10 == 0 or word[0] is not lastLetter:
                    printLine = 0
                    lastLetter = word[0]
                    # print("")
                print(word, end=", ")





def main():

    guessChecker("saine", "bbbyb")
    quit()

    guessCounter = 0

    while len(answerList) > 1 and guessCounter < 9:
        guessCounter += 1
        print("Enter guess #", guessCounter, end= ": ")
        userInput = input()
        userGuess = userInput

        userInput = input("Enter results as [B/G/Y]: ")
        userResults = userInput
        guessChecker(userGuess, userResults)

    
    # secondGuess()



if(__name__ == '__main__'):
    main()