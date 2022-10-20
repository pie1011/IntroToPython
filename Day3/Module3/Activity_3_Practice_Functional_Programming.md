# Practice with Functional Programming

An important part of understanding functional programming is practicing it. You have already done a lot of functional programming in the past as you have learned JavaScript and Python so far. In this activity, pay close attention to the functional programming concepts covered in this lesson as you complete each prompt. They were:

- Functional purity (no side effects)
- Declarative
- Avoid state change and mutable data

With these things in mind, try to complete the following tasks. You may create a new GitHub repository or use Replit for this activity. If you choose to use Replit, fork this assignment.

## Function Prompts

- Write a function flatten_dict() to flatten a nested dictionary by joining the keys with . character.
  - `flatten_dict({'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4})`
  - returns `{'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4}`
  - Hint: You can assume that all dictionary keys will be of type string, and that nested dictionaries will only be nested one layer deep (a dictionary of dictionaries will not have another dictionary nested inside it).
- Write a function unflatten_dict() to do reverse of flatten_dict.
  - `unflatten_dict({'a': 1, 'b.i': 2, 'b.j': 3, 'c': 4})`
  - returns `{'a': 1, 'b': {'i': 2, 'j': 3}, 'c': 4}`
  - Hint: You can assume that the keys for the dictionary will all be of type string, and that you never need to create more than one layer of nested dictionary. It may be helpful to create an empty dictionary as the value for the outer key ('b' in this example), then fill it in iteratively as you find keys that belong to that dictionary.
- Write a function treemap() to map a function over nested list.
  - `treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])`
  - returns `[1, 4, [9, 16, [25]]]`
  - Hint: Using recursion may make this function easier to code. Don't forget to check the type of the element you are iterating over.

## Solution

If you get stuck or want to check your work, see the [solution guide](Activity_3_Practice_Functional_Programming_Solution.py).
