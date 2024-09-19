# Write a program named `greeter.py`. The program should ask for your 
# name, then output `Hello, NAME!` where `NAME` is the name you entered:

# $ python greeter.py
# What is your name? Sue
# Hello, Sue!

NAME = input("What is your name? ")

print(f'Hello, {NAME}!')

# SOLUTION

# 1
name = input('What is your name? ')
print('Hello, ' + name + '!')

#2 
name = input('What is your name? ')
print(f'Hello, {name}!')

