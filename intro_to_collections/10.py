# Bob expects the following code to print the names in alphabetical 
# order. Without running the code, can you say whether it will? Explain 
# your answer.

names = { 'Chris', 'Clare', 'Karis', 'Karl',
        'Max', 'Nick', 'Victor' }
print(names)

# These should not print in alphabetic order because this is a set,
# and sets are unordered by default.


# SOLUTION

# This code probably won't print the names alphabetically. Sets, by 
# definition, are unordered collections. Thus, the order in which 
# members are shown when printing or iterating is arbitrary. Bob's 
# code may print the names alphabetically on rare occasions, but it 
# would do so only once every 5040 times.