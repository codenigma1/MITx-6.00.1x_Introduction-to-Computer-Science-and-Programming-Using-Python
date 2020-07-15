# Problem 7
# 20.0/20.0 points (graded)
# Write a function called general_poly, that meets the specifications below. For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 because  1∗103+2∗102+3∗101+4∗100 .


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def calculate(x):
    	k = 0
    	for i in L:
    		k = x*k + i
    	return k
    return calculate


# If you are getting "exception thrown", you should read the specification CAREFULLY for what you need to return.