# Exercise: gcd iter
# 5.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 5 minutes

# The greatest common divisor of two positive integers is the largest integer that divides each of them without remainder. For example,

# gcd(2, 12) = 2

# gcd(6, 12) = 6

# gcd(9, 12) = 3

# gcd(17, 12) = 1

# Write an iterative function, gcdIter(a, b), that implements this idea. One easy way to do this is to begin with a test value equal to the smaller of the two input arguments, and iteratively reduce this test value by 1 until you either reach a case where the test divides both a and b without remainder, or you reach 1.

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    divisor = b;
    result = 0;
    while 1 <= divisor :
    	if a%divisor == 0 and b%divisor == 0:
    		if divisor >= result :
    			result = divisor;
    			return result;
    		else :
    			result = result;	
    	else :
    		result = 0; 	 
    	divisor -=1;	
    	# return result;

# Correct