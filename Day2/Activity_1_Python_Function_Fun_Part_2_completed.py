# 1. Takes in any number of arguments and prints them one at a time.

def arb_args(*args):
    for a in args:
        print(a)

arb_args(1, 2, 3)

# 2. Takes in two integers. Two nested functions should perform separate, distinct math operations using the integers. The result of both nested functions should then be added together and printed.

def inner_func(a, b):

    def mult(a, b):
        return a * b

    def sub(a, b):
        return a - b

    return mult(a, b) +  sub(a, b)

print(inner_func(10, 2))

# 3. Takes in two strings: a student's name and their lunch preference. The function should print both strings. If a lunch preference is not given, "Mystery Meat" should be printed instead.

def lunch_lady():
    pass

# 4. Accepts two integers and returns both the sum and the product.

def sum_n_product(a, b):
    sum = a + b
    product = a * b

    return sum, product

x, y = sum_n_product(10, 5)
print(x, y)

# 5. Should be arb_args but assigned an alias. Remember, variables can hold functions in Python just like they can in JS. Alternatively, you can call a function from inside another function.
# NOT THAT BUT ANOTHER TRY
def alias_arb_args(*args):
    print(*args)

alias_arb_args('one', 'two', 'three')

# 6. Accepts any number of integers and prints their average.

def arb_mean(*args):
    total = args
    return sum(total) / 2

print(arb_mean(1, 2, 3, 4, 5))

# 7. Accepts any number of strings and returns the longest one.

def arb_longest_string(*args):
    longest = len(args[0])
    for each in args:
        if len(each) > longest:
            longest = len(each)
        
