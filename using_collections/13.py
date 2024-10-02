# Without running the following code, determine what each `print` statement
# should print.

cats = ('Cocoa', 'Cheddar',
        'Pudding', 'Butterscotch')

print('Butterscotch' in cats) # True
print('Butter' in cats) # False, string has to be exact, `in` is not a substring search.
print('Butter' in cats[3]) # True, `'Butter'` exists in `'Butterscotch'`
print('cheddar' in cats) # False, case-sensitive