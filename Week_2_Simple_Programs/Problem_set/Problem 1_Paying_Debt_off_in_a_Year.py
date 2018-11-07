# Problem 1 - Paying Debt off in a Year
# 10.0/10.0 points (graded)
# Write a program to calculate the credit card balance after one year if a person only pays the minimum monthly payment required by the credit card company each month.

# The following variables contain values as described below:

# balance - the outstanding balance on the credit card

# annualInterestRate - annual interest rate as a decimal

# monthlyPaymentRate - minimum monthly payment rate as a decimal

# For each month, calculate statements on the monthly payment and remaining balance. At the end of 12 months, print out the remaining balance. Be sure to print out no more than two decimal digits of accuracy - so print

# Remaining balance: 813.41
# instead of

# Remaining balance: 813.4141998135 
# So your program only prints out one thing: the remaining balance at the end of the year in the format:

# Remaining balance: 4784.0
# A summary of the required math is found below:

# Monthly interest rate= (Annual interest rate) / 12.0
# Minimum monthly payment = (Minimum monthly payment rate) x (Previous balance)
# Monthly unpaid balance = (Previous balance) - (Minimum monthly payment)
# Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

# We provide sample test cases below. We suggest you develop your code on your own machine, and make sure your code passes the sample test cases, before you paste it into the box below.


# Test Cases to Test Your Code With. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

# Click to See Problem 1 Test Cases
# Note: Depending on where you round in this problem, your answers may be off by a few cents in either direction. Do not worry if your solution is within +/- 0.05 of the correct answer. Be sure to test these on your own machine - and that you get the same output! - before running your code on this webpage!

# Test Cases:

# 	      # Test Case 1:
# 	      balance = 42
# 	      annualInterestRate = 0.2
# 	      monthlyPaymentRate = 0.04
	      
# 	      # Result Your Code Should Generate Below:
# 	      Remaining balance: 31.38
                    
#           # To make sure you are doing calculation correctly, this is the 
#           # remaining balance you should be getting at each month for this example
#             Month 1 Remaining balance: 40.99
#             Month 2 Remaining balance: 40.01
#             Month 3 Remaining balance: 39.05
#             Month 4 Remaining balance: 38.11
#             Month 5 Remaining balance: 37.2
#             Month 6 Remaining balance: 36.3
#             Month 7 Remaining balance: 35.43
#             Month 8 Remaining balance: 34.58
#             Month 9 Remaining balance: 33.75
#             Month 10 Remaining balance: 32.94
#             Month 11 Remaining balance: 32.15
#             Month 12 Remaining balance: 31.38

                

# 	      Test Case 2:
# 	      balance = 484
# 	      annualInterestRate = 0.2
# 	      monthlyPaymentRate = 0.04
	      
# 	      Result Your Code Should Generate Below:
# 	      Remaining balance: 361.61


# Paste your code into this box
i = 1;
while i <= 12:
    balance = balance - (balance * monthlyPaymentRate);
    balance = balance + (balance * annualInterestRate/12.0)
    # print ("Month", i, "Remaining balance: ", round(balance, 2));
    i = i + 1;
print("Remaining balance:", round(balance, 2))

# Correct