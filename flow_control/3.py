# Without running the following code, what does it print? Why?
def bar_code_scanner(serial):
    match serial:
        case '123':
            print('Product1')
        case '113':
            print('Product2')
        case '142':
            print('Product3')
        case _:
            print('Product not found!')

bar_code_scanner('113')
bar_code_scanner(142)

# This prints:
# ```
# Product2
# Product not found!
# ```

# The function `bar_code_scanner()` uses a match statement to compare the
# value of `serial` with multiple values. 

# `Product2` is printed because the argument `'113'` on line 13 is matched
# to `case '113'` on line 6, which causes the body on line 7 to be printed.

# As for `Product not found!` there is no matching case (the `'142'` on
# line 8 is a string, not an integer), so it is matched to the "default"
# case on line 10.