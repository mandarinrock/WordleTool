# Comment or uncomment the 2nd line to toggle debug
debug = True
# debug = False


# output holds the output file
output = open("answerList", "w")


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
    # with open("WordLists/officialGuesses") as listFile:
    with open("WordLists/officialAnswers") as listFile:

        # Copy the word list to memory as wordList
        wordList = listFile.read().splitlines()

    # ---------------------- NOTE -----------------------
    # If we think of our combination as a comboLen digit
    # variable with n = length(wordList) possible values
    # for each digit. We can increment the first digit
    # until it reaches n and rolls over to the next digit
    # ---------------------- NOTE -----------------------

    # Initialize the combination
    combination = [0] * comboLen

    # firstWord = 0

    # # TEMP
    # combination[0] = 2050
    # combination[1] = 2050
    # combination[2] = 2050
    # combination[3] = 2050
    firstWord = 1 + combination[0]
    # Initialize the alphabet
    alphabet = []

    printCounter = 0
    answerCount = 0

    if debug:
        print(len(wordList)) # DEBUG


    while(combination[0] < len(wordList)):

        if firstWord < combination[0]:
            firstWord = combination[0]

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

                if i == 0:
                    print("All combinations checked")
                    quit()
                
                # if debug:
                #     print("End of list reached") # DEBUG
                combination[i] = firstWord
                if combination[i-1] < len(wordList)-1 and combination[i-1] > firstWord:
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

                        answerCount += 1

                        answerList = []
                        
                        for answer in combination:

                            answerList.append(wordList[answer])

                        if printCounter <= 0:
                            print(len(alphabet), end= ": ")
                            print(answerList, end=" #")
                            print(answerCount)
                            # printCounter += 1
                        else:
                            printCounter -= 1
                        if len(alphabet) > 23:
                            output.write(str(len(alphabet)))
                            output.write(": ")
                            saveAnswers(answerList)
                            # printCounter = 10
                            for jackpot in range(10):
                                print("===================================================")
                                print("  ===============================================")
                                print("   ============================================\n")
                                print(" ", end="")
                                print(len(alphabet), end= ": ")
                                print(answerList)
                                print("\n   ============================================")
                                print("  ===============================================")
                                print("===================================================\n")


                        # terminate()
                        
                    
                    # if debug:
                    #     if len(alphabet) > 24:

                    #         # guessList = []
            
                    #         for thisGuess in combination:

                    #             print(wordList[thisGuess], end= ", ") # DEBUG

                    #         print("") # DEBUG

            # else:
            #     if debug:
            #         print("Completed combination[", guess, "]") # DEBUG





        
        



    # while len(alphabet) < 25:

        
    # # For each word in the combination
    # for digit in range(comboLen, 0):






def main():

    comboGen(5)



if(__name__ == '__main__'):
    main()