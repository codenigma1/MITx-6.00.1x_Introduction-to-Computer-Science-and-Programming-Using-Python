# Problem 5 - Playing a Hand
# 10.0/10.0 points (graded)
# In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. This pseudocode is provided to help guide you in writing your function. Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode before you start coding your solution.

# Note: Do not assume that there will always be 7 letters in a hand! The parameter n represents the size of the hand.

# Testing: Before testing your code in the answer box, try out your implementation as if you were playing the game. Here is some example output of playHand:

# Test Cases
# Case #1
# Function Call:
# wordList = loadWords()
# playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)
# Output:
#   Current Hand:  a c i h m m z
#   Enter word, or a "." to indicate that you are finished: him
#   "him" earned 24 points. Total: 24 points
 
#   Current Hand:  a c m z
#   Enter word, or a "." to indicate that you are finished: cam
#   "cam" earned 21 points. Total: 45 points
 
#   Current Hand:  z
#   Enter word, or a "." to indicate that you are finished: .
#   Goodbye! Total score: 45 points.    
# Case #2
# Function Call:
# wordList = loadWords()
# playHand({'w':1, 's':1, 't':2, 'a':1, 'o':1, 'f':1}, wordList, 7)
# Output:
#   Current Hand:  a s t t w f o
#   Enter word, or a "." to indicate that you are finished: tow
#   "tow" earned 18 points. Total: 18 points
 
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: tasf
#   Invalid word, please try again.
 
#   Current Hand:  a s t f
#   Enter word, or a "." to indicate that you are finished: fast
#   "fast" earned 28 points. Total: 46 points 
 
#   Run out of letters. Total score: 46 points.    
# Case #3
# Function Call:
# wordList = loadWords()
# playHand({'n':1, 'e':1, 't':1, 'a':1, 'r':1, 'i':2}, wordList, 7)
# Output:
#   Current Hand: a r e t i i n
#   Enter word, or a "." to indicate that you are finished: inertia
#   "inertia" earned 99 points. Total: 99 points

#   Run out of letters. Total score: 99 points.
# Additional Testing
# Be sure that, in addition to the listed tests, you test the same basic test conditions with varying values of n. n will never be smaller than the number of letters in the hand.


def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """
    # BEGIN PSEUDOCODE (download ps4a.py to see)
    score = 0
    # As long as there are still letters left in the hand:
    while calculateHandlen(hand) > 0:

        # Display the hand
        print("Current hand:", end = " ")
        displayHand(hand)
        
        # Ask user for input
        inp = input("Enter word, or a '.' to indicate that you are finished: ", )
        
        # If the input is a single period:
        if inp == ".":

            # End the game (break out of the loop)
            break
   
        # Otherwise (the input is not a single period):

        else:

            # If the word is not valid:
            if isValidWord(inp, hand, wordList) == False:
                print("Invalid word, please try again.")
                print(" ")

                # Reject invalid word (print a message followed by a blank line)

            # Otherwise (the word is valid):
            else:
                score += getWordScore(inp, n)

                # Tell the user how many points the word earned, and the updated total score, in one line followed by a blank line

                print(inp, "earned", getWordScore(inp, n), "points.", "Total: ", score)
                print(" ")
                
                # Update the hand 
                hand = updateHand(hand, inp)
               

    # Game is over (user entered a '.' or ran out of letters), so tell user the total score
    if inp == ".":
        print("Goodbye! Total score: ", score, "point")   
    else:  
        print("Run out of letters. Total score: ", score, "points.")

# Correct