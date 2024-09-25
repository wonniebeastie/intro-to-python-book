# To what values do the following expressions evaluate?

False or (True and False) # False
True or (1 + 2) # True, short circuit evaluation
(1 + 2) or True # 3, short circuit eval
True and (1 + 2) # 3, the last one evaluated
False and (1 + 2) # False
(1 + 2) and True # True, last one evaluated
(32 * 4) >= 129 # False
False != (not True) # False, inequality operator checks if 
True == 4 # False, equality operator checks for exact value
False == (847 == '847') # True

# Correct