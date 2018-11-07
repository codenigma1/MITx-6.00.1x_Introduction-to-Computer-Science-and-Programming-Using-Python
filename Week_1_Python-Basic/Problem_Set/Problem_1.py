# Problem 1
# 10.0/10.0 points (graded)
# Assume s is a string of lower case characters.

# Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

count = 0
for vow in s:
    if vow == "a" or vow == "e" or vow == "i" or vow == "o" or vow == "u":
        count = count + 1
print("Number of vowels: " + str(count))


# Correct