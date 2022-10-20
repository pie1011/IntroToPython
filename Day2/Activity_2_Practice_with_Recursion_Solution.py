# 1.  Write a program that takes a positive number as an argument and prints the numbers from n to zero.

def count_down(n):
    # Base case
    if n==0:
        return

    # Recursive case
    else:
        print(n)
        count_down(n-1)

# test case
n=8
count_down(n)


# 2. Write a function that prints the natural numbers from 1 to n.

def natural_numbers(x,i=1):
    #base case
    if i > x:
        return
  #recursive case
    else:
        print(i)
        natural_numbers(x,i+1)

natural_numbers(3)
#output: 1 2 3

# 3. Write a function that returns the first n elements in the Fibonacci Sequence.

def nth_fibbonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return nth_fibbonacci(n-1)+nth_fibbonacci(n-2)

print("2nd fib number:")
print(nth_fibbonacci(2))
print("4th fib number:")
print(nth_fibbonacci(4))
print("8th fib number:")
print(nth_fibbonacci(8))

# 4. Write a function that calculates the value of 'a' to the power of 'b'.

def a_to_b(a,b):
    if b < 1:
        print("invalid input")
    elif b == 1:
        return a
    else:
        return a * a_to_b(a,b-1)

print("2^4:")
print(a_to_b(2,4))

# 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not.

def is_palindrome(str):
    if len(str) == 1 or len(str) == 0:
        return True
    else:
        return (str[0] == str[-1]) and is_palindrome(str[1:-1])

print("is 'apple' a palindrome?")
print(is_palindrome('apple'))
print("is 'tacocat' a palindrome?")
print(is_palindrome('tacocat'))

# Bonus. Write a function that when given two numbers, finds their greatest common divisor.

def gcd(x,y):
    if y == 0:
        return x
    else:
        return gcd(y, x % y)

print("gcd of 15 and 10:",gcd(15,10))
print("gcd of 46 and 12:",gcd(46,12))