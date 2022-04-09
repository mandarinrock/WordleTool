import copy

# Comment or uncomment the 2nd line to toggle debug
debug = True
debug = False


# output holds the output file
output = open("frequencyOutput", "w")


# terminate() closes @output and ends the program
def terminate():

    output.close
    quit()


# saveAnswers(String[] answers) prints a list of strings, copies to output, and calls terminate()
def saveAnswers(answers):

    # if debug:
    #     print("Printing answers") # DEBUG

    # Write @answers to console
    # print(answers) # DEBUG

    # For each word in answers
    for word in answers:

        # Copy the word to output file, followed by a comma and a space
        output.write("'%s', " % word)

    # After copying the combination
    else:
        # Add a new line
        output.write("\n")


# TODO add function description
def comboGen(comboLen = None):

    # If a number of words in combination is not provided
    if comboLen is None:
        # Then default to 4 words
        comboLen = 4

    # Open a word list
    with open("WordLists/officialGuesses") as listFile:
    # with open("WordLists/officialAnswers") as listFile:

        # Copy the word list to memory as wordList
        wordList = listFile.read().splitlines()

    # Initialize the combination
    combination = [0] * comboLen
    # Initialize the alphabet
    alphabet = []

    if debug:
        print(len(wordList)) # DEBUG


    while(combination[0] < len(wordList)):

        # if debug:
        #     # if len(alphabet) > 4:

        #         # guessList = []

        #         for thisGuess in combination:

        #             print(wordList[thisGuess], end= ", ") # DEBUG

        #         print("") # DEBUG

        # Clear the alphabet
        alphabet.clear()

        # For every guess in the current combination
        for guess in range(comboLen):

            i = guess
            while combination[i] >= len(wordList):
                
                # if debug:
                #     print("End of list reached") # DEBUG
                combination[i] = 0
                if combination[i-1] < len(wordList)-1:
                    combination[i] = 0 + combination[i-1]
                i -= 1
                combination[i] += 1
            # else:
            #     for i in range(comboLen-1):
            #         for j in range(i+1, comboLen):
            #             if combination[i] > combination[j]:
            #                 if debug:
            #                     print("combination[", i+1,"]: ", combination[i], " -> combination[", j+1,"]: ", combination[j])
            #                 combination[j] = 0 + combination[i]
            #             else:
            #                 break




            # if debug and guess > 0:
            #     print(guess) # DEBUG


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

                        answerList = []
                        
                        for answer in combination:

                            answerList.append(wordList[answer])

                        print(len(alphabet), end= ": ")
                        print(answerList)
                        output.write(str(len(alphabet)))
                        output.write(": ")
                        saveAnswers(answerList)
                        if len(alphabet) > 23:
                            for jackpot in 50:
                                print(len(alphabet), end= ": ")
                                print(answerList)


def frequency():

    with open("WordLists/officialAnswers") as listFile:

        wordList = listFile.read().splitlines()

    with open("WordLists/officialGuesses") as guessFile:

        guessList = guessFile.read().splitlines()

    # alphabet = [[0] * 5] * 26
    alphabet = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

    # Count frequency of all letters in each position
    for word in wordList:

        if debug:
            print(word)

        for letter in range(len(word)):

            if debug:
                # print(chr(ord(word[letter]) - ord('a')))
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
        print(chr(ord('A') + i), end=": [\t")
        for j in range(4):
            print(alphabet[i][j], end="\t")
            totals[i] += alphabet[i][j]
        print(alphabet[i][4], end="\t]\n")
        # print("] ")

    # Print and save results
    for i in range(26):

        print(chr(ord('A') + i), end=": ")
        print(totals[i])

    # Try to find the word with the most overall frequency
    maxOverall = 0
    spotTotal = 0
    frequentWord = copy.copy(guessList[0])
    for word in guessList:

        tempMax = 0
        tempSpot = 0

        for i in range(len(word)):
            tempMax += totals[ord(word[i]) - ord('a')]
            tempSpot += alphabet[ord(word[i]) - ord('a')][i]
        
        if tempMax > maxOverall:
            frequentWord = copy.copy(word)
            maxOverall = tempMax
            spotTotal = tempSpot

    print("")
    print("Total letter frequency:", maxOverall)
    print("Spot frequency:", spotTotal)
    print(frequentWord)
    print("")


    maxOverall = 0
    spotTotal = 0
    for word in guessList:

        # if word == "china":
        #     for i in range(len(word)):
        #         print(word[i], end=" freq =")
        #         print(totals[ord(word[i]) - ord('a')])
        
        
        unique = True
        tempMax = 0
        tempSpot = 0

        for i in range(len(word)):

            for j in range(i+1, len(word)):
                if word[i] == word[j] and i != j:
                    unique = False
                    # break

            # if unique == False:
            #     break
            # else:
            # if word == "china":
            # # for i in range(len(word)):
            #     print(word[i], end=" freq =")
            #     print(totals[ord(word[i]) - ord('a')])
            tempMax += totals[ord(word[i]) - ord('a')]
            tempSpot += alphabet[ord(word[i]) - ord('a')][i]
        
        if unique:
            if tempMax > maxOverall:

                # if debug:
                # print(word)
                # print(tempMax)
            
                frequentWord = copy.copy(word)
                maxOverall = tempMax
                spotTotal = tempSpot

    print("Total unique letter frequency:", maxOverall)
    print("Spot frequency:", spotTotal)
    print(frequentWord)
    print("")

    # Try to find the word with the most frequency in each spot
    maxOverall = 0
    spotTotal = 0
    frequentWord = copy.copy(guessList[0])
    for word in guessList:

        tempMax = 0
        tempSpot = 0

        for i in range(len(word)):
            tempMax += alphabet[ord(word[i]) - ord('a')][i]
            tempSpot += totals[ord(word[i]) - ord('a')]
        
        if tempMax > maxOverall:
            frequentWord = copy.copy(word)
            maxOverall = tempMax
            spotTotal = tempSpot

    print("Total spot frequency:", spotTotal)
    print("Spot frequency:", maxOverall)
    print(frequentWord)
    print("")


    # Try to find the word with the most frequency in each spot
    maxOverall = 0
    spotTotal = 0
    frequentWord = copy.copy(guessList[0])
    for word in guessList:

        unique = True
        tempMax = 0
        tempSpot = 0


        for i in range(len(word)):

            for j in range(i+1, len(word)):
                if word[i] == word[j] and i != j:
                    unique = False
                    
            tempMax += alphabet[ord(word[i]) - ord('a')][i]
            tempSpot += totals[ord(word[i]) - ord('a')]
        
        if unique:
            if tempMax > maxOverall:
                frequentWord = copy.copy(word)
                maxOverall = tempMax
                spotTotal = tempSpot

    print("Total unique spot frequency:", spotTotal)
    print("Unique spot frequency:", maxOverall)
    print(frequentWord)
    print("")








def main():

    frequency()



if(__name__ == '__main__'):
    main()