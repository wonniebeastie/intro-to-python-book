# On reflection, we've decided that we don't want to rely on using a global 
# variable in the code we wrote in the previous example. To fix this, we're 
# going to nest the code from the previous example into an outer function:

# def all_actions():
#     counter = 0

#     def increment_counter():
#         global counter
#         counter += 1

#     print(counter)                # 0

#     increment_counter()
#     print(counter)                # 1

#     increment_counter()
#     print(counter)                # 2

#     counter = 100
#     increment_counter()
#     print(counter)                # 101

# all_actions()


def all_actions():
    counter = 0

    def increment_counter():
        nonlocal counter
        counter += 1

    print(counter)                # 0

    increment_counter()
    print(counter)                # 1

    increment_counter()
    print(counter)                # 2

    counter = 100
    increment_counter()
    print(counter)                # 101

all_actions()

"""
When the code was run, an error was thrown: 

NameError: name 'counter' is not defined

So that pointed to the bug being the `counter` variable not being initialized 
in the global scope.

Python assumes that the `counter` variable inside the `increment_counter()`
function is a local variable; The `nonlocal` statement tells it to look at the
nearest enclosing scope that is not global, for the variable. 
"""