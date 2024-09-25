# GOAL
# Write a function that returns an all-caps version of a string when
# said string is longer than 10 chars.

# INPUTS & OUTPUTS
# I: A String
# O: The string in all-caps OR the original string

# EXAMPLE(S)
# I: 'hello world'
# O: 'HELLO WORLD'

# I: 'goodbye'
# O: 'goodbye'

# RULES (EXPLICIT/IMPLICIT)
# - Length of the string must be determined.
# - Only strings longer than 10 chars should be changed.
# - If shorter than 10 chars, the string should be returned as is.

# STEPS
# Set function named `all_caps_if_long()` that takes 1 string argument.
# Inside the function:
#      - Find the length of `string`; Assign it to a variable.
#      - If the length is longer than 10 chars, convert it to all uppercase
#      letters and return it.
#      - Otherwise, return as is.

def all_caps_if_long(str):
	str_length = len(str)
	if str_length > 10:
		upped_string = str.upper()
		return upped_string
	else:
		return str

print(all_caps_if_long('hello world')) # HELLO WORLD
print(all_caps_if_long('goodbye')) # goodbye
print(repr(all_caps_if_long(''))) # ''

# SOLUTION
def caps_long(string):
    if len(string) > 10:
        return string.upper()
    else:
        return string

print(caps_long("Sue Smith"))     # Sue Smith
print(caps_long("Sue Roberts"))   # SUE ROBERTS
print(caps_long("Joe Shea"))      # Joe Shea
print(caps_long("Joe Stevens"))   # JOE STEVENS

# NOTES
# It's not necessary to create variables for every single thing in the 
# function. Save lines & memory and just call functions and methods 
# directly on the argument.