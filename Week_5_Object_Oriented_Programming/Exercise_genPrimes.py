# Exercise: genPrimes
# 5.0/5.0 points (graded)
# ESTIMATED TIME TO COMPLETE: 10 minutes

# Write a generator, genPrimes, that returns the sequence of prime numbers on successive calls to its next() method: 2, 3, 5, 7, 11, ...

# Hints
# Ideas about the problem
# Have the generator keep a list of the primes it's generated. A candidate number x is prime if (x % p) != 0 for all earlier primes p.


def genPrimes():
	num = 2
	def isPrime(x):

		if x > 1:
			for i in range(2, x):
				if (x % i) == 0:
					return False
			else:
				return True
	while True:
		if isPrime(num)==True:
			yield num
		num += 1


# Correct