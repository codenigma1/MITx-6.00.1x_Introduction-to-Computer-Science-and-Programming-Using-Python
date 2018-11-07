def primes_list(N):
    '''
    N: an integer
    '''
    # Your code here
    primes_no = []
    for i in range(2, N+1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
        	primes_no.append(i)        
        	        
    primes_no.sort()
    return primes_no
    

print(primes_list(20))