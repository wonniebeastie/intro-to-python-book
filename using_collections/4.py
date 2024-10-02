# 3 part question

pets = {
    'Cat':  'Meow',
    'Dog':  'Bark',
    'Bird': 'Tweet',
}

# PART 1
# Write some code to print `Bark` by accessing the element associated 
# with the key `Dog`.

print(pets['Dog'])

# PART 2
# Write some code to print `None` when you try to print the value 
# associated with the non-existent key, `Lizard`.

print(pets.get('Lizard'))

# PART 3
# Write some code to print `<silence>` when you try to print the value 
# associated with the non-existent key, `Lizard`.


print(pets.get('Lizard', '<silence>'))

# SOLUTION
# Correct

# Since the pets dictionary doesn't have a Lizard key, we need to use 
# the `dict.get` method so we don't get an error. In Part 2, we don't 
# specify a default value, so `get` returns `None`. In Part 3, we set 
# <silence> as the default value.

