# Write some code that determines and prints whether the number `3` 
# appears inside each of these lists:

numbers1 = [1, 3, 5, 7, 9, 11]
numbers2 = []
numbers3 = [2, 4, 6, 8]
numbers4 = ['1', '3', '5']
numbers5 = ['1', 3.0, '5']

# You should print True or False depending on each result.

# 1
def contains_3(list):
	if 3 in list:
		return True
	else:
		return False

print(contains_3(numbers1)) # True - `3`
print(contains_3(numbers2)) # False, empty list
print(contains_3(numbers3)) # False
print(contains_3(numbers4)) # False, `'3'` is not counted
print(contains_3(numbers5)) # True, the float `3.0` is counted

# SOLUTION
print(3 in numbers1)          # True
print(3 in numbers2)          # False
print(3 in numbers3)          # False
print(3 in numbers4)          # False (3 != '3')
print(3 in numbers5)          # True  (3 == 3.0)