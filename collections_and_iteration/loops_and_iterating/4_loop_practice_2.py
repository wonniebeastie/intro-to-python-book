my_list = [6, 3, 0, 11, 20, 4, 17]

# while loop to print even values
index = 0

while index < len(my_list):
    element = my_list[index]
    if element % 2 == 0:
        print(element)
    index += 1

print()

# for loop to print odd numbers

for number in my_list:
    if number % 2 != 0:
        print(number)