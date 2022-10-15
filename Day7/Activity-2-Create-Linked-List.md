# Create a Linked List

## Working with Linked Lists

Linked lists are common data structures. In an interview, you may be asked to implement a linked list as well as describe when to use a linked list.

Before we start, let's review what a linked list is.

## Linked List

### What is a linked list?

1. ~~Data structure that can map keys to values.~~
1. ~~Data structure where only the earliest added item can be accessed.~~
1. ~~Data structure where each element can be randomly accessed using its index number.~~
1. Data structure that contains nodes that contain a data field and reference link.

## Implement a Linked List

Now it is time to create a linked list. A linked list is not a built-in data structure, so we will learn how to build it. Implementing a linked list will help you understand the data structure theory better and prepare you for future job interviews. Since a linked list is not a built-in data structure in Python and there is no linked list module or library, we need to start by creating a linked list class.

Remember that a linked list is a data structure that contains nodes. Each node has a data field and a reference link to the next node. The first node is called the head node and the last node is called the tail node.

![Linked List Diagram](..\Day7\images\lessons-ppp-7-data-structures-Create-a-Linked-List.4.png)

[A Gentle Introduction to Linked Lists With MongoDB](https://www.mongodb.com/developer/languages/javascript/introduction-to-linked-lists-and-mongodb/)

### 1. Create a class for the nodes called `Node`

Each node will contain two fields: the data and the reference link. For now, set the reference to None at the start. This will set the reference to an empty value unless otherwise specified.

- Use the init method to initialize the attributes of the class. We want data and reference fields to be created for each node.
- Don't forget to use the `self` keyword to bind the attributes with the given arguments. This allows us to access the attributes and methods of the class in Python.

Your code should look something like this:

```python
class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference
```

Now we can create our first node. Create a node with a value of 5 (leave the reference as is). Print the node's data to check that it works.

Your code should look something like this:

```python
class Node:
    def __init__(self, data, reference=None):
        self.data = data
        self.reference = reference

    node1 = Node(5)
    print(node1.data)
```

When we run our program, we should see an output of 5. A node is created when we run the program (we can also create other nodes if we want). If you print the reference by running `print(node1.reference)`, you will see an output of `None`. A linked list is a chain of nodes, so next we need to link the nodes.

The image shows a visual example of what we just created. We created a node with a data value of 5 and a reference to 'None'.

![Example of node](..\Day7\images\lessons-ppp-7-data-structures-Create-a-Linked-List.3.png)

We can create a second node with a value of 11 and set the first node's reference to the second node. If we print the reference for the first node, it will no longer be empty. The output isn't very helpful, but we can see that the reference is no longer empty.

Sample code to test this:

```python
node2 = Node(11)
node1.reference = node2
print(node1.reference)
```

Sample output:

![Sample reference output](..\Day7\images\lessons-ppp-7-data-structures-Create-a-Linked-List.2.png)

It can be difficult to interpret what this output means, because it's giving us only a little more information than a memory address. That said, note the __main__.Node object at the beginning of the message. At the very least, this tells us that the program recognizes that the reference points to another instance of the Node class.

### 2. Create a class for the linked list called `LinkedList`

This class stores the head of the list. Initially we want to create an empty linked list by setting `head` equal to `None`.

- Use the `__init__` method to initialize the attributes of the class. We want a `head` field to be created in the linked list.
- Don't forget to use the `self` keyword to bind the attributes with the given arguments.
Your code should look something like this:

```python
class LinkedList: 
    def __init__(self, head=None):
        self.head = head
```

## Traverse a Linked List

We will define a method in the linked list class to traverse a linked list. In other words, define a method that will go through and print the data of each node. The traversal operation will start with the head of the linked list, access the data if the head is not null, go to the next node and access its data, and continue this process for every node in the linked list.

- If the linked list is empty, print a message.
- If the linked list is not empty, go to each node and print each node's data value.

### 3. Define a method called `print_linked_list()`

Write a conditional statement that checks if the linked list is empty. If it is, print a message saying, _The linked list is empty_.

```python
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
```

### 4. If the linked list is not empty, print each node's data and use the reference to access each node

- Set a variable called `c_node` (representing the current node) equal to `self.head`. This is not necessary, but will help. For example, `c_node.data` will be the current node's data. This is easier to read and type than `self.head.data`.
- Use a `while` loop since we know the end condition. When the reference is equal to `None`, stop the function. In other words, we want to print the node's data and set the current node equal to the reference link to go to the next node until the reference link is `None`.
- In the while loop, print the current node's data. Also, set `c_node` equal to `c_node.reference`. We do this so the reference of the node becomes the new current node. This allows us to access each node in the linked list.
  - Think of this like moving along the line of people spread out across a field. Say we have the list A -> B -> C -> D. We could say that we're at node `head.reference.reference.reference`, or that we're at node C. Which one is easier to keep track of and understand?

```python
class LinkedList: 
    def __init__(self, head=None):
        self.head = head

    def print_linked_list(self):
        if self.head is None:
            print("The linked list is empty")
        else:
            c_node = self.head
            while c_node is not None:
                print(c_node.data)
                c_node = c_node.reference
```

Create a linked list called `linked_list1`. Run the method we just created in steps 3 and 4.

If we run the following, we should see an output of 'The linked list is empty', because we have not added elements to the linked list:

```python
linked_list1 = LinkedList()
linked_list1.print_linked_list()
```

## Add a Node to the Beginning of a Linked List

### 5. Define a method to add a node to the beginning of a linked list

- Set a variable called `n_node` that will store the data from each new node created using the Node class (shown in green).
- Set the reference to the next node as the current head. In other words, set the reference as pointing to the current first node (shown in blue).
- Set the current head as the new node. In other words, set self.head equal to the n_node to make the new node the head/first node (shown in red).
  - Think about why this works. Try drawing a picture, as that often helps. Why are we setting the references to head the way and order described here? What would happen if we reversed the order of these lines?

```python
def add_to_start(self, data):
    n_node = Node(data)
    n_node.reference = self.head
    self.head = n_node
```

Test the method by creating a linked list and adding two nodes to the linked list. Here is possible code to test the newly created method:

```python
linked_list1 = LinkedList()
linked_list1.add_to_start(82)
linked_list1.add_to_start(15)
linked_list1.print_linked_list()
```

Here is a sample output:

![output](..\Day7\images\lessons-ppp-7-data-structures-Create-a-Linked-List.1.png)

Output after running program. The output shows the data values 15 and 82.

Note that when we run the program, we will see 15 first, then 82 as we add elements to the beginning of a linked list.

If you are stuck, you can check out [possible solutions here](https://github.com/HackerUSA-CE/PY-Choosing-and-Implementing-Data-Structures/tree/solution/bonus_linked_list). Several data structures are derived from arrays or linked lists, so having a foundation for working with these data structures will help in your software engineering journey.

## Bonus

If you want a further challenge, try making your linked list even more functional by adding the following functions to your `LinkedList` class:

1. `add_item()`
   - Accepts a value. Creates a node with that value, and adds the node to the end of the linked list.
2. `add_item_after()`
   - Accepts two values. Creates a node from the first value. Traverses the linked list to find the second value, and places the new node directly after the node containing the second value. If a node containing the second value is not already in the list, `raises` a `ValueError`.
3. `remove_item()`
   - Accepts a value. Traverses the linked list to find the first node containing that value, and removes the value from the linked list. Care should be taken not to lose the portion of the list that the removed node points to. If the value is not in the list, `raises` a `ValueError`.

## Solution

If you get stuck or would like to check your work, the solution can be found [here](https://github.com/HackerUSA-CE/PY-Choosing-and-Implementing-Data-Structures/blob/solution/bonus_linked_list/linked_list.py).
