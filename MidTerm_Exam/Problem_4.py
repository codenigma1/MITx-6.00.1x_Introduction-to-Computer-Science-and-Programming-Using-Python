	
def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    #YOUR CODE HERE
    def calculate(x):
    	v = 0
    	for i in L:
    		v = x*v + i
    	return v
    return calculate		

L = [1,2,3,4,5,6,7]