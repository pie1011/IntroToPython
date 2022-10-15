# Activity: Practice with Recursion

You will practice writing algorithms using recursion in Python. Recursion can be a complicated concept, but with practice and time you will see the advantages of using recursion in certain situations.

## Setup  Instructions

Write your answers in [Activity_2_Practice_with_Recursion.py](Activity_2_Practice_with_Recursion.py).

## Algorithms

Code a solution for the following algorithms using direct recursion.

### 1. Write a program that takes a positive number as an argument and prints the numbers from n to zero

Before we begin coding, we want to break down this problem and think about it recursively.

We want to define a function that takes a number, let's say n , prints it, and calls itself again with the value of n-1. The function will keep calling itself until the base case is met. One way to do this is to determine if the number is equal to 0 and when it is, stop the function. Think about what the base case and recursive case would be.

#### Base Case

What could be a base case for this problem?

- [ ] If n equals 5, print the number
- [ ] If n is greater than 0, print n and run the function again for the value of n-1.
- [ ] If n equals 0, stop the function.

Try to code the desired program.

**Note that there are many ways to solve a problem so when working with algorithms there is always more than one way to do it. Some solutions may be more efficient or more DRY than others, but it is important to remember that there is always more than one way to do something.**

Here is a possible solution:

```python
def count_down(n):

  #  Base case
  if n==0:
      return

  #  Recursive case
  else:
      print(n)
      count_down(n-1)

# test case
n=8
count_down(n)
```

For example, this could have also worked:

```python
def count_down(n):
    #inherent base case
    #(will stop if n <= 0)
    if n>0:
        #recursive case
        print(n)
        count_down(n-1)

#test case
n=8
count_down(n)
```

### 2. Write a function that prints the natural numbers from 1 to n

For example:

```python
def natural_numbers(x,i):
    #your code here
natural_numbers(3)
#output: 1 2 3
```

- A natural number is a positive whole number.
- Here is [more information on natural numbers](https://www.mathsisfun.com/definitions/natural-number.html).

#### Base Case

What could be a base case for this problem?

- [ ] If n is less than 1, return n.
- [ ] If n is greater than 0, print n.
- [ ] If the number we are trying to print is greater than n, stop the function.

### 3. Write a function that returns the nth elements in the Fibonacci Sequence

- The Fibonacci Sequence is the series of numbers where the next number is found by adding up the two numbers before it: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
- For example, if n=4, then the result would be '2' and if n=2, the result would be '1'
- Here is [more information on the Fibonacci Sequence](https://www.mathsisfun.com/numbers/fibonacci-sequence.html).
- Hint: Look back at the factorial example as the structure of the algorithm may help you.

#### Base Case

What could be a base case for this problem?

- [ ] If the numerical input, n, is less than or equal to 1, call the function.
- [ ] If the numerical input, n, is less than or equal to 1, return the value of n.
- [ ] If the numerical input, n, is greater than 1, return the sum of the two calls of the function with inputs of n-1 and n-2.

**Identifying the base case is a great habit to develop when working with recursion. Try to do this before starting to code the remaining algorithms.**

### 4. Write a function that calculates the value of 'a' to the power of 'b'

- For example if a=2 and b=4, then power(2,4) would be calculating 2^4=2*2*2*2 so the result would be 16.
- Here is [more information on exponents](https://www.mathsisfun.com/exponent.html).

### 5. Write a function that checks whether a string is a palindrome or not. The program should take in a string and return True if the string is a palindrome and False if not

- A palindrome is a word that is the same when it is reversed, such as madam, radar, kayak, or tacocat.
- Here is [more information on palindromes](https://en.wikipedia.org/wiki/Palindrome).

## Summary

Nice job so far. Throughout this course you will continue to work with different data structures and write more algorithms. You will become better and more comfortable with problem solving and coding possible solutions.

**If stuck, do not panic. Problem solving and understanding advanced computer science concepts, such as recursion, takes time!**

## Bonus

Write a function that when given two numbers, finds their greatest common divisor.

- The greatest common divisor of two integers is the largest positive integer that divides both of the integers. For example, look at the numbers 10 and 15: 10 can be divided by 1, 5, and 10, 15 can be divided by 1, 3, 5, and 15.
- When we say 'can be divided' here we mean divided evenly, so in other words there is no remainder. For example when 15 is divided by 6, there is a remainder of 3 because 15=6(2)+3 so 6 is not a divisor of 15.
- The greatest common divisor of 15 and 10 is 5 since both numbers can be divided by 5.
- Here is [more information on greatest common divisors](https://en.wikipedia.org/wiki/Greatest_common_divisor).

## Extra Bonus

Try solving the algorithms using an iterative approach and compare your code.

You can [read more about recursion here](https://en.wikipedia.org/wiki/Recursion_(computer_science)).

## Solution

If you get stuck or want to check your work, feel free to check out the [solution guide](https://replit.com/@SD-Team/1022-solution#main.py).
