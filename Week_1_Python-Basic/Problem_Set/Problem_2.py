# Problem 2
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. For example, if s = 'azcbobobegghakl', then your program should print
# Number of times bob occurs is: 2


# Paste your code into this box
count = 0
for b in range(len(s)):
	if s[b:].startswith('bob'):
		count = count + 1
print ('Number of times bob occurs is:', count)

# Correct