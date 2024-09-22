# What does the following code print?

def scream(words):
    words = words + '!!!!'
    return
    print(words)

scream('Yipeee')

# This doesn't print anything as the `return` statement ends the program
# on line 5, where it stops executing the rest of the function. 