# Without running the following code, identify the numbers that are 
# included in each of the following ranges:

range(7)        # 0, 1, 2, 3, 4, 5, 6
range(1, 6)     # 1, 2, 3, 4, 5
range(3, 15, 4) # 3, 7, 11
range(3, 8, -1) # Empty range
range(8, 3, -1) # 8, 7, 6, 5, 4

# SOLUTION
range(7)            # [0, 1, 2, 3, 4, 5, 6]
range(1, 6)         # [1, 2, 3, 4, 5]
range(3, 15, 4)     # [3, 7, 11]
range(3, 8, -1)     # []
range(8, 3, -1)     # [8, 7, 6, 5, 4]

# Most important: Ranges never include the "stop" value.
# Negative step value counts downwards from the start to the stop value.
# Thus, the start value should typically be larger than the stop value
# when the step value is negative.