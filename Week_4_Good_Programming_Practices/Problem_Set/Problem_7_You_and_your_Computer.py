# **Part B is dependent on your functions from ps4a.py, so be sure to complete ps4a.py before working on ps4b.py**
# Now that you have completed your word game code, you decide that you would like to enable your computer (SkyNet) to play the game (your hidden agenda is to prove once and for all that computers are inferior to human intellect!) In this part, you will be able to compare how you as a user succeed in the game compared to the computer's performance.

# You should look at the following two functions: compChooseWord and compPlayHand, before moving on to Problem 7 on the next page.

# compChooseWord
# If you follow the pseudocode for compChooseWord, you'll see that the code creates a computer player that is legal, but not always the best. Try to walk through and understand our implementation.

# A Note On Runtime: You may notice that things run a bit slowly when the computer plays. This is to be expected - the wordList has 83667 words, after all! 

# Test Cases to Understand the Code: 
# >>> compChooseWord({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6) 
# appels 
# >>> compChooseWord({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5) 
# acta 
# >>> compChooseWord({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12) 
# immanent 
# >>> compChooseWord({'x': 2, 'z': 2, 'q': 2, 'n': 2, 't': 2}, wordList, 12) 
# None
# compPlayHand
# Now that we have the ability to let the computer choose a word, we need to set up a function to allow the computer to play a hand - in a manner very similar to Part A's playHand function. This function allows the computer to play a given hand and is very similar to the earlier version in which a user selected the word, although deciding when it is done playing a particular hand is different.

# Test Cases to Understand the Code: 

# compPlayHand({'a': 1, 'p': 2, 's': 1, 'e': 1, 'l': 1}, wordList, 6)
# Current Hand: a p p s e l
# "appels" earned 110 points. Total: 110 points
# Total score: 110 points.

# compPlayHand({'a': 2, 'c': 1, 'b': 1, 't': 1}, wordList, 5)
# Current Hand: a a c b t "acta" 
# earned 24 points. Total: 24 points 
# Current Hand: b Total score: 24 points. 

# compPlayHand({'a': 2, 'e': 2, 'i': 2, 'm': 2, 'n': 2, 't': 2}, wordList, 12)
# Current Hand: a a e e i i m m n n t t
# "immanent" earned 96 points. Total: 96 points
# Current Hand: a e t i
# "ait" earned 9 points. Total: 105 points
# Current Hand: e
# Total score: 105 points.


# Problem 7 - You and your Computer
# 20.0/20.0 points (graded)
# Now that your computer can choose a word, you need to give the computer the option to play. Write the code that re-implements the playGame function. You will modify the function to behave as described below in the function's comments. As before, you should use the HAND_SIZE constant to determine the number of cards in a hand. Be sure to try out different values for HAND_SIZE with your program.

# Sample Output and Hints
# Here is how the game output should look...

# Hints about the output

# A Note On Runtime
# You may notice that things run slowly when the computer plays. This is to be expected. If you want (totally optional!), feel free to investigate ways of making the computer's turn go faster - one way is to preprocess the word list into a dictionary (string -> int) so looking up the score of a word becomes much faster in the compChooseWord function.

# Be careful though - you only want to do this preprocessing one time - probably right after we generate the wordList for you (at the bottom of the file). If you choose to do this, you'll have to modify what inputs your functions take (they'll probably take a word dictionary instead of a word list, for example).

# IMPORTANT:Don't worry about this issue when running your code in the checker below! We load a very small sample wordList (much smaller than 83667 words!) to avoid having your code time out. Your code will work even if you don't implement a form of pre-processing as described.

# Entering Your Code
# Be sure to only paste your definition for playGame from ps4b.py in the following box. Do not include any other function definitions.

def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function

    while True:
        user_input = input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ", )
        if user_input == 'e':
            break
        elif user_input == 'n':    
            while True:

                if user_input == 'n':
                    inp = input("Enter u to have yourself play, c to have the computer play: ", )

                    if inp == 'u':

                        hand = dealHand(HAND_SIZE)
                        playHand(hand, wordList, HAND_SIZE)
                        break

                    elif inp == 'c':

                        hand = dealHand(HAND_SIZE)
                        compPlayHand(hand, wordList, HAND_SIZE)
                        break
            
                    else:
                        print("Invalid command.")                

        elif user_input == 'r':
            try:
                hand
                inp = input("Enter u to have yourself play, c to have the computer play: ", )

                if inp == 'u':
                    playHand(hand, wordList, HAND_SIZE)

                elif inp == 'c':
                    compPlayHand(hand, wordList, HAND_SIZE)

                else:
                    print("Invalid command.")                    
            except:
                print("You have not played a hand yet. Please play a new hand first!")
        else:
            print("Invalid command.")


# Correct