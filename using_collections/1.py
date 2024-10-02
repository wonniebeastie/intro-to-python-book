# Write Python code to print the seventh number of range(0, 25, 3).

print(range(0, 25, 3)[6]) # 18
print(list(range(0, 25, 3))) # [0, 3, 6, 9, 12, 15, 18, 21, 24]

# SOLUTION

# Solution 1 (easy to read)
my_range = range(0, 25, 3)
print(my_range[6])                      # 18

# Solution 2 (not so easy to read)
print(range(0, 25, 3)[6])               # 18