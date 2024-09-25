my_list = [
    [1, 3, 6, 11],
    [4, 2, 4],
    [9, 17, 16, 0],
]

for item in my_list:
    for number in item:
        if number % 2 == 0:
            print(number)

# Expected Output:
# 6
# 4
# 2
# 4
# 16
# 0