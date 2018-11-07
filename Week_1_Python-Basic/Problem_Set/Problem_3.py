# Problem 3
# 15.0/15.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print:

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print:
# Longest substring in alphabetical order is: abc

# Note: This problem may be challenging. We encourage you to work smart. If you've spent more than a few hours on this problem, we suggest that you move on to a different part of the course. If you have time, come back to this problem after you've had a break and cleared your head.


morelength=0
present=s[0]
longest=s[0]
for i in range(len(s) - 1):
	# print (i)
    if s[i + 1] >= s[i]:
    	# print (s[i + 1])
        present = present + s[i + 1]
        # print (present)
        if len(present) > morelength:
            morelength = len(present)
            longest = present
            # print (longest)
    else:
        present=s[i + 1]
        # print (present)
print ('Longest substring in alphabetical order is: ', longest)


# Correct

