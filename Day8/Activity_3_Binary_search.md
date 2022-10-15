# Activity: Binary Search Algorithm

You will write a binary search algorithm in Python using iteration. As a bonus, you can rewrite the binary search algorithm using recursion.

## Setup

Write your `binary_search()` function in [Activity_3_Binary_search.py](Activity_3_Binary_search.py)

## Divide-and-Conquer Algorithms

Binary search is an example of a divide-and-conquer algorithm. Divide-and-conquer is a problem-solving technique.

The steps of this problem-solving strategy can be generalized as follows:

1. Divide the steps and break the problem into smaller, simpler problems.
2. Conquer each smaller step and solve the smaller sub-problem. Repeat the process until a condition is met.
3. Combine the smaller steps and solve the larger original problem.

For a binary search, we divide the elements, conquer the sub-problems by repeating the process of checking the midpoint for the desired value, and split the elements until the desired value is found.

## Write a Binary Search Algorithm

Binary search is an efficient way to find an item in a sorted list or array of items. In this activity, we will be searching lists.

A binary search algorithm repeatedly halves the list that could contain the item. The process of cutting the list in half repeats until the desired element is found.

We are going to write a binary search algorithm. If the desired element is found, we want the function to return `True`. If the desired element is not found, we want the function to return `False`.

To understand the algorithm before jumping into the code, look at the following visual example with a list containing seven numbers. Let the desired element that we are searching for be 12.

|  |   |    |    |    |    |    |
|--|---|----|----|----|----|----|
| 5| 8 | 12 | 14 | 19 | 22 | 27 |

In our algorithm, we will set two variables, first and last, equal to the first and last indices for the remaining elements. We also will set a variable called mid equal to the middle element's index.

| first |   |    | mid  |    |    | last |
|-------|---|----|------|----|----|------|
| `5`   | 8 | 12 | `14` | 19 | 22 | `27` |

The middle element's index will be found by adding the first and last indices and dividing the result by two. This calculation finds the midpoint of the list. In this example, the element with value of 5 would have index of 0, and the element with value of 27 would have index of 6. So (0+6)/2 = 6/2, which makes mid equal to 3. In other words, the middle element would have an index or position of 3 and the value of the element with index of 3 is 14.

```python
mid = (first + last) // 2
```

**We want to use the `//` division operator so that an integer value is returned. If we used `/`, we would be working with a floating point value.**

Now that we have our middle element's index, we want to check if the middle element's value is equal to the desired value. If it is, we are done.

Otherwise, if the value of our desired value is less than the middle element's value, set the last variable equal to mid-1 (to continue to search the lower half). Otherwise, set the first variable equal to mid+1 (to continue to search the upper half).

In this example, the middle element's value is not equal to our desired element. The desired value is less than the middle element's value (12 is less than 14). Therefore, we need to set 'last' equal to one less than the middle element's index, mid-1. In this example, mid-1 would have the value of 3-1, or 2. We can see this in the following image.

| first |   | last |    |    |    |    |
|-------|---|------|----|----|----|----|
| `5`   | 8 | `12` | 14 | 19 | 22 | 27 |

The middle element's index would now become 1, so the middle element's value would be 8. The process would repeat until the desired element is found or there are no more items in the list to search.

| first | mid | last |
|-------|-----|------|
|   5   | `8` |  12  |

In this case, the element with value of 12 is in the list and would be found.

If there is an even number of elements in the list or array that you are searching, then there is no exact midpoint. Does binary search still work in this case? Yes, the idea of splitting the data approximately in half is still able to occur and the binary search algorithm still works (one 'half' of the data will just be slightly larger or smaller than the other 'half').

Now that we have a general understanding of how the algorithm will work, let's write the code. We will start with writing the binary search algorithm using iteration and then use recursion as a bonus.

## Iterative Process

- Define a function called `binary_search` that takes a list and an element. Name the parameters data and el, respectively.
- Create two variables called `first` and `last` to store the index values of the first and last positions in the list.
- Create a variable called found and set equal to False. We will use this variable to store True if the desired element is found later on.

Our code should look something like this:

```python
def binary_search(data, el):
    first = 0
    last  = len(data)-1 
    found = False
```

**Note that `last = len(data)-1` because indexing starts at 0.**

- Create a while loop that runs when `first` is less than or greater than `last` and the element is not found (found is `False`).
- Inside the while loop, declare a variable called mid that will store the middle element's index by adding the first and last position and dividing by two.

```python
def binary_search(data, el):
    first = 0
    last  = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2
```

- In the while loop, check if the middle element's value is equal to the desired element. If it is, set found to True. Otherwise, we need to decide if we are using the left or right half.

```python
while first <= last and not found:
    mid = (first+last)//2

    if data[mid] == el:
        found = True
```

- Write the case for the left half. If the desired element is less than the middle element's value, set last equal to one less than the index of the middle element (mid-1).
- Otherwise, deal with the right half. Set `first` equal to one more than the index of the middle element `(mid+1)`.

```python
while first <= last and not found:
    mid = (first+last)//2

    if data[mid] == el:
        found = True
    else:
        if el < data[mid]: 
            last = mid-1
        else: 
            first = mid+1
```

- Outside of the while loop, return the variable found.
- Create a list and test your function! If the element we are searching for is in the list, we expect an output of True. If the element is not in the list, we expect an output of False.

Possible code to accomplish this is shown here:

```python
def binary_search(data, el):
    first = 0
    last  = len(data)-1 
    found = False

    while first <= last and not found:
        mid = (first+last)//2

        if data[mid] == el:
            found = True
        else:
            if el < data[mid]: 
                last = mid-1
            else: 
                first = mid+1

    return found

test_list = [5, 8, 12, 14, 19, 22, 27, 30, 31]

print(binary_search(test_list, 12))
```

When the program is run, the output is True. If we change the desired element from 12 to 11, then the output is False.

## Summary

Congrats on writing a binary search algorithm! Having a solid understanding of how this algorithm works will help you with more complex algorithms.

## Bonus

1. Now that we have written a binary search algorithm using iteration, how could we rewrite the algorithm using recursion? Let's try it!
   - Remember that recursion is a way of solving a problem where the solution depends on smaller iterations of itself. In other words, a recursive algorithm calls itself repeatedly until a condition is met. A recursive algorithm needs a base and recursive case. Look over your binary search algorithm and think through how you could rewrite parts of the algorithm using recursion.
   - If unsure of where to begin, here are steps to help:
     - Define a new function named recursive_bsearch that takes in two parameters, a list and an element.
     - Check if the list is empty. If it is, return False.
     - Otherwise, we want the following to happen:
   - Define a variable called mid and set it equal to the index of the middle element in the list. In this case, we can find the length of the list and divide the length by two.
   - Check if the middle element's value is equal to the desired value. If it is, return True.
   - Otherwise, we need to check if the desired value is less than the middle element's value. If it is, we want to call the function again. However, this time the first parameter will represent the adjusted list. We can use index slicing to pass in the half of the list we want to recursively pass through. In this case, it will be the lower half of the elements in the array. Otherwise, if the desired value is greater than the middle element's value, it would be the upper half of the elements in the array.
2. Given a sorted integer list of n elements and a target value, write a function that searches for a target. If the target exists, return the index; otherwise, return -1.

If stuck, you can check out [solutions to the activity and bonus here](https://github.com/HackerUSA-CE/PY-Binary-Search-Algorithm/tree/solution).
