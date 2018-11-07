# Problem 3 - Valid Words
# 10.0/10.0 points (graded)
# At this point, we have written code to generate a random hand and display that hand to the user. We can also ask the user for a word (Python's input) and score the word (using your getWordScore). However, at this point we have not written any code to verify that a word given by a player obeys the rules of the game. A valid word is in the word list; and it is composed entirely of letters from the current hand. Implement the isValidWord function.

# Testing: Make sure the test_isValidWord tests pass. In addition, you will want to test your implementation by calling it multiple times on the same hand - what should the correct behavior be? Additionally, the empty string ('') is not a valid word - if you code this function correctly, you shouldn't need an additional check for this condition.

# Fill in the code for isValidWord in ps4a.py and be sure you've passed the appropriate tests in test_ps4a.py before pasting your function definition here.

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    hand_1 = hand.copy()
    word_check = False
    if word in wordList:
        word_check = True

    if set(list(word)) <= set(hand_1.keys()):      
        letter_check = True
    else:
        letter_check = False

    for i in word:
        if i in hand_1.keys():
            hand_1[i] = hand_1.get(i, 0) -1

    values_check = all(i >= 0 for i in hand_1.values())        

    if word_check == True and letter_check == True and values_check == True:
        return True
    else:
        return False


# Correct
