# Activity: Sorting and Problem Solving

You will use the Python built-in sort functions as well as practice writing algorithms to continue to improve your programming and problem-solving skills.

## Setup

Write your answers in [Activity_2_Sorting_Problem_Solving.py](Activity_2_Sorting_Problem_Solving.py)

## Python Sorting Functions

It is helpful to understand various sorting algorithms, such as bubble sort, insertion sort, merge sort, etc. It is always important to consider the situation when determining which sorting algorithm is best to use. However, we also want to be aware of the built-in sorting functions in Python. Python sorting functions are often the best-performing option in a general sense.

It is often recommended to use Python sorting functions for speed and usability, but it is also important to know how other common sorting algorithms work. This is why we learned about common sorting algorithms before learning about Python's built-in functions.

### Overview of sorting functions in Python

- `sort()` method: modifies and sorts a list
- `sorted()` function: creates a new sorted list

You can assume that we are sorting in ascending order unless otherwise specified.

## Algorithms

View the [Python documentation on sorting functions](https://docs.python.org/3/howto/sorting.html) in order to write the following algorithms. Remember that part of becoming a software engineer is becoming a lifelong learner and getting good at reading documentation and other online resources!

1. Write an algorithm that takes in an unsorted numerical list as an argument and sorts the list (use the `sort()` method).
2. Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list (use the `sorted()` function).
   - The `sort()` method is usually less convenient than the `sorted()` function, but if we do not need the original list, then it can be more efficient. As stated in the documentation, the `sort()` method is only defined for lists, whereas the `sorted()` function can work for more than just lists.
3. Write an algorithm that takes in an unsorted numerical list as an argument and creates a new sorted list in descending order (use the `sorted()` function).
   - The `sorted()` function sorts in ascending order, but it can sort in descending order by adding a reverse parameter with a boolean value of `True`.

Remember that there is always more than one way to write an algorithm and solve a problem!

## Bonus

4. Write an algorithm that takes in a string and sorts the words in the string in alphabetical order. The comparison should be case-insensitive.
   - Sample input: 'I love software engineering'
   - Sample output: ['engineering', 'I', 'love', 'software']
   - Note that a key parameter will need to be used here in order for the sorting to be case-insensitive (sort in alphabetical order regardless of whether string is uppercase or lowercase).
5. Write an algorithm that takes in an unsorted integer array and finds a pair with a given sum.
   - For example, for input: [5, 10, 4, 7, 6, 2] and target = 9, the output would be 7, 2.
   - If there are no pairs with sum equal to the target number, then the output should be 'no pairs sum to the target'.
   - **If stuck, here are helpful steps for algorithm 5**
   - Sort the list in ascending order.
   - Set a variable called `left` equal to 0 and another variable called `right` equal to one less than the length of the list. These variables should be initially set to the indices for the first and last element in the list.
   - Write a `while` loop that runs the following code when `left` is less than `right`.
     - If the value of the element at index or `left` plus the value of the element at index or `right` equals the target number, then print the pair and return.
     - If the sum of the two elements is less than the target number, then increment `left` by 1.
     - Otherwise, increment `right` by 1.
   - Print 'no pairs sum to the target' if no two numbers sum to the target number.

## Summary

In this lesson, you have learned and used Python built-in sort functions and have discussed three more types of common sorting algorithms (selection sort, insertion sort, and merge sort). In the next lesson, you will solve problems and answer questions related to data structures and algorithms to help prepare you for future software engineering positions.

If stuck, check out [possible solutions here](https://github.com/HackerUSA-CE/PY-Sorting-and-Problem-Solving/tree/solution).
