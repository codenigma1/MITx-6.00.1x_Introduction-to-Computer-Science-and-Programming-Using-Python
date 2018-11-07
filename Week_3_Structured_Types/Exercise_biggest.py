# Exercise: biggest
# 5.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 7 minutes

# Consider the following sequence of expressions:

# animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

# animals['d'] = ['donkey']
# animals['d'].append('dog')
# animals['d'].append('dingo')
# We want to write some simple procedures that work on dictionaries to return information.

# This time, write a procedure, called biggest, which returns the key corresponding to the entry with the largest number of values associated with it. If there is more than one such entry, return any one of the matching keys.

# Example usage:

# >>> biggest(animals)
# 'd'
# If there are no values in the dictionary, biggest should return None.


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    
    values = aDict.values()
    big = max(values)
    result = "";
    # print(big)
    for read in aDict:
    	if aDict[read] == big:
    		result = read;
    return result;		


# Correct
# Important: If you are getting a message Incorrect: Something went wrong: tests don't match up. please click Check until you get a different error message or you get the green Correct. We apologize for the inconvenience.
