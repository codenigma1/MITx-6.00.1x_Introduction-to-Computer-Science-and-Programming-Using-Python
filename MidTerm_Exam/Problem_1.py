def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    # Here I am checking exponential value what it will be. run the program!

    exp = 2;
    if b**exp < x:
    	while b**exp < x:
    		exp = exp + 1
    	if b**exp == x:	
    		return exp
    	else:
    		return exp-1    		
    else:
    	return 0



print(myLog(15, 3))		
