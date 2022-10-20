# Accepts any number of named arguments and prints them in the pattern key : value one at a time.

def name_args(**kwargs):
    for key in kwargs:
        print(f"{key} : {kwargs[key]}")

name_args(a=1, b=True, c='hi')

# Returns True if all the elements in an iterable are true. Hint: there is an existing built-in function that could be very helpful here.

def all_true(iter):
    return all(iter)

print(all_true([True, True, True, False]))

# Returns True if one of the elements in an iterable is true. Hint: there is an existing built-in function that could be very helpful here.

def one_true(iter):
    return any(iter)

print(one_true([True, True, True, False]))

# Uses recursion to find the factorial of an integer.

def recursive_factorial():
    pass

# Recursively removes all adjacent duplicate letters from a string.
# Input: AABBCCDD
# Output: ABCD

def recursive_deduplicate():
    pass

# Uses recursion to reverse a string.

def recursive_reverse():
    pass
