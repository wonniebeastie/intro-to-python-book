text = "It's probably pining for the fjords!"

print(text[21:35].rfind('f'))     # 8
print(text.rfind('f', 21, 35))    # 29

# Explain why the code below prints different values on lines 3 and 4.

# MY SOLUTION
print(text[21:35]) # for the fjords
# `text[21:35]` on line 3 returns the string `for the fjords"`;
# THEN the `rfind` method is called on this extracted substring,
# finding the value `'f'` at index 8 of that shorter string.

# On line 4, the string `'f'` is looked for from index 21 to index 35
# of the entire string using the `rfind` method. This method returns
# 29 because the entirety of the string is taken into account.

# SOLUTION
# Line 3 first extracts a slice from text ranging from index 21 through 
# index 35. That returns the string 'for the fjords'. rfind then returns 
# 8, the index of the rightmost instance of an 'f'.

# On the other hand, line 4 does a search for the rightmost f between 
# indexes 21 and 35. Since the f occurs at index 29, that's what the 
# method returns.

