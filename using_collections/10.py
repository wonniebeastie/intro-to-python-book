# Consider the following nested collection:
cats = {
    'Pete': {
        'Cheddar': {
            'color': 'orange',
            'enjoys': {
                'sleeping',
                'snuggling',
                'meowing',
                'eating',
                'birdwatching',
            },
        },
        'Cocoa': {
            'color': 'black',
            'enjoys': {
                'eating',
                'sleeping',
                'playing',
                'chewing',
            },
        },
    },
}

# Write one line of code to print the activities that Cocoa enjoys.

# print(len(cats)) # 1
print(cats['Pete']['Cocoa']['enjoys']) 
# {'playing', 'sleeping', 'eating', 'chewing'}

# NOTE
# Remember that dictionaries are key-based, not index-based.