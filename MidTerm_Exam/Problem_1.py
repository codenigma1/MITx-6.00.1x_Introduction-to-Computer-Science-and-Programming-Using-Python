# Problem 3
# 10.0/10.0 points (graded)
# Implement a function called closest_power that meets the specifications below.

# For example,

# closest_power(3,12) returns 2
# closest_power(4,12) returns 2
# closest_power(4,1) returns 0

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    cls_pwr = 0
    if base > num:
        cls_pwr = 0
    elif base == num:
        cls_pwr = 1
    else:
        for i in range(1, int(num)):
            if abs(base**i - num) <= abs(base**(i + 1) - num):
                cls_pwr = i
                break
    return cls_pwr


print(closest_power(2, 9))