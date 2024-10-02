# Write Python code to replace all the `:` characters in the string below 
# with `+`.

info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'

# MY SOLUTION 1
# Split string into a list of words using `':'` as the delimiter.
# Join them together again using `'+'` as the joiner string.
info = info.split(':')
# print(info) # ['xyz', '*', '42', '42', 'Lee Kim', '/home/xyz', '/bin/zsh']
info = '+'.join(info)
print(info) # xyz+*+42+42+Lee Kim+/home/xyz+/bin/z

# MY SOLUTION 2
info = 'xyz:*:42:42:Lee Kim:/home/xyz:/bin/zsh'
info = info.replace(':', '+')
print(info) # xyz+*+42+42+Lee Kim+/home/xyz+/bin/zsh

# SOLUTION
# Correct