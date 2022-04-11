import copy

# Comment or uncomment the 2nd line to toggle debug
debug = True
debug = False


# output holds the output file
# output = open("frequencyOutput", "w")


# terminate() closes @output and ends the program
def terminate():

    # output.close
    quit()


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
        for j in range(5): # changed from range(4) to range(5)
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
    terminate()


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




def main():

    userInput = input('\nEnter list of words to check, separated by spaces: ')
    print("")
    
    # while ',' in userInput:
    #     userInput.remove(',')
    # debug = True
    

    # if debug:
    #     print(inputList)

    # print("\n. [", end="")
    # commas = 4
    # for i in inputList:
    #     if commas > 0:
    #         print(i, end= ", ")
    #         commas -= 1
    #     else:
    #         print(i, end= "] (24)")
    # print(inputList, end=" (24)")
    
    frequencyGen(userInput)





if(__name__ == '__main__'):
    main()