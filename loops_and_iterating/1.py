# The following code causes an infinite loop (a loop that never stops 
# iterating). Why?
counter = 0

while counter < 5:
    print(counter)

# This code causes an infinite loop because the `counter` variable is
# never incremented inside the `while` loop. So `counter` will always 
# be `0`, causing the body of the `while` loop to go again and again.

# The loop will stop only when the conditional expression `counter < 5`
# evaluates to `False`.