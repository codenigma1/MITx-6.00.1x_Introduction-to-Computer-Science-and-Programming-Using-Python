# Problem 6
# 20.0/20.0 points (graded)
# Write a function called gcd that calculates the greatest common divisor of two positive integers. The gcd of two or more integers, when at least one of them is not zero, is the largest positive integer that divides the numbers without a remainder.

# One way is recursively, where the greatest common denominator of a and b can be calculated as gcd(a, b) = gcd(b, a mod b). Hint: remember the mod symbol is % in Python. Do not import anything.

# For example, the greatest common divisor (gcd) between a = 20 and b = 12 is:
# gcd(20,12) is the same as gcd(12, 20 mod 12)	= gcd(12,8)
# gcd(12,8) is the same as gcd(8, 12 mod 8)	= gcd(8,4)
# gcd(8,4)	is the same as gcd(4, 8 mod 4) = gcd(4,0)
# The gcd is found (and the gcd is equal to a) when we reach 0 for b.

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    #YOUR CODE HERE
    if b == 0:
    	return a
    else:
    	return gcd(b, a%b)    	

print(gcd(20, 12))

# Correct