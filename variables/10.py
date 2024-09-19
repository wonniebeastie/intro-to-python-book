# Assume that obj already has a value of 42 when the code below starts 
# running. Which of the subsequent statements reassign the variable? 
# Which statements mutate the value of the object that obj references? 
# Which statements do neither? If necessary, you can read the documentation.

# Reassign the variable or mutate?

obj = 'ABcd'       # reassigns
obj.upper()        # neither
obj = obj.lower()  # reassigns
print(len(obj))    # niether
obj = list(obj)    # reassigns
obj.pop()          # mutates
obj[2] = 'X'       # neither
obj.sort()         # mutates
set(obj)           # neither
obj = tuple(obj)   # reassigns


# SOLUTION
obj = 'ABcd'      # Reassignment
obj.upper()       # Neither
obj = obj.lower() # Reassignment
print(len(obj))   # Neither
obj = list(obj)   # Reassignment
obj.pop()         # Mutation
obj[2] = 'X'      # Mutation ((<-- Reassigning an element is a mutating act!))
obj.sort()        # Mutation
set(obj)          # Neither
obj = tuple(obj)  # Reassignment

# A simple assignments like var = something is always either an 
# initialization or a reassignment. Since obj has already been 
# initialized (it has a value of 42 before this code was reached), 
# lines 1, 3, 5, and 10 perform reassignment. In a few situations, 
# mutation and reassignment can happen in the same statement. None 
# of the above statements do both.

# obj.upper does not mutate the caller, so line 2 does neither. Likewise, 
# since print, len, and set don't mutate their arguments, lines 4 and 9 
# are neither.

# The remaining statements all mutate the object referenced by obj. pop 
# removes the last element of the list. obj[2] = 'X' reassigns the 
# element at index 2, but it mutates obj itself. Finally, sort mutates 
# the object when it performs an in-place sort.