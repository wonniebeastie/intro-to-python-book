# The `randrange` method returns a randomly selected element from the
# specified range.

# The while loop keeps running until it finds a random number that
# matches the last number in the range. 

# Refactor the code so it doesn't require two different invocations of
# `randrange`.

import random

highest = 10
# number = random.randrange(highest + 1)
# print(number)

# while number != highest:
#     number = random.randrange(highest + 1)
#     print(number)

while True:
    number = random.randrange(highest + 1)
    print(number)
    
    if number == highest:
        break

# SOLUTION
# Same as above.

# This problem needs a do/while loop, but Python doesn't have one. So
# we can combine a `while True` loop with a `break` statement to 
# emulate it.