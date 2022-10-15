# Code Along: Create a BST

In this activity, you will code along with your instructor to create a BSTNode class to hold the data for each node in a Binary Search Tree (BST), and then develop a BST class to perform a variety of tree operations.

## Setup

### Instructions

1. Click HERE for the link to the repo.
1. Fork (not clone) it to your OWN GitHub account.
1. Now to clone the repo to your machine, click the green 'Code' button and then copy the URL.
1. In a new terminal, or Git Bash, go to where you want to clone the repo.
1. Type git clone in the terminal or Git Bash, then a space, then paste the URL you copied from your repo. Example:

undefinedClick here to copy

6. Hit "Enter" or "Return", whichever is on your keyboard.
6. Now, in your terminal, change to your repository directory (cd repo name)
6. Open your repository in Visual Studio Code.
6. Open terminal in your Visual Studio Code.
6. Do the assignment in Visual Studio Code and stage your changes using the git add -A command.
6. Make at least one commit by using the git commit -m "write your message here" command. Example:

6. Finally, push your changes using the git push command. Example:

undefinedClick here to copy
Review: Linked Lists vs BSTs
In our last activity, we created a LinkedList class from a Node class. The node class for the linked list looked something like this:

undefinedClick here to copy
This very simple class helped us to organize our linked list so that it was made of a bunch of nodes. Our linked list had a head, which pointed to the first node, and each node's next attribute pointed to the next node in the list.

When creating a BST, we are going to follow a similar process. We will first create a BSTNode class, and then we will create our BST class using BSTNodes. However, there are some key differences. Let's review the structure of a linked list and of a BST.

A linked list can be thought of as looking like this:

A linked list with three nodes: "cat", "dog", and "bird"
Each box is a node, and each node has two parts: the data, and the "next", or pointer to the next node.

On the other hand, a BST may look like this:

A binary search tree with 4 levels. 8 is the root of the tree.
Geeks for Geeks

There are two key differences here between a linked list and a BST. First, each node of a BST has up to two children, not just one. Because there can never be more than two children, we often denote them as "left" and "right", rather than "next".

The second key difference has to do with the order in which elements are stored in a BST. To simplify our understanding, we will only deal with numerical data in this activity, but the same principle applies to any type of data.

In a BST, the data is kept "balanced" by enforcing certain rules.

If the tree is empty (root points to None), put the new node at the top of the tree
If the tree is not empty, start at the root. Compare the new node's value to the current node's value. If the new node is bigger, move to the right. If the new node's value is smaller, move to the left. When there is no node at the current position, put the new node there.
Note: You can have a Binary Tree that is not a Binary Search Tree. A Binary Tree only means that there are no more than two children, while a BST has the added order imposed on it.

Part 1: Writing a BSTNode Class
With all of this in mind, we will start out by creating a BSTNode class.

After cloning the activity repository, open the BST.py file and write your BSTNode class. This class will look very similar to the Node class we wrote for our linked list, but should fulfill the following requirements:

The constructor should accept up to three arguments: data, left, and right
If any of the arguments are not specified, they should default to None.
Don't forget to include the self argument.
Write two magic methods (__str__() and __repr__() ) to allow the nodes to be printed. These two magic methods should return strings that represent the node. They should both return the same thing, the value of the node's data as a string.
Refer back to the magic methods activity if you need help remembering how to create magic methods for classes.
To test that these work, a node with the value 3 for its data should output 3 when printed.
Use the following code to test whether your BSTNode is functioning correctly.

undefinedClick here to copy
Part 2: Writing a BST Class
Our BST, just like our linked list, will start with a reference to the beginning. The key difference is that the beginning of the list we called head, and the beginning (or top) of our BST is called the root. The root of our tree can only point to one node.

Create a BST class that fulfills the following requirements:

The constructor should accept one argument, root.
If root is not specified, it should default to None.
Don't forget to include the self argument.
Write two magic methods (__str__() and __repr__() ) to allow the tree to be printed. These two magic methods should return strings that represent the nodes in the tree, printed in a readable format. They should both return the same thing.
If the tree is empty, return "The tree is empty".
Otherwise, do the following:
Initialize a variable self.output to an empty string
Call the self.print_tree() function (given below) with node set to root. Note that this function doesn't return any value, but rather edits self.output as it runs.
Return the self.output variable
undefinedClick here to copy
Try to understand what the print_tree() method does and how it works before using it. Feel free to implement a different printing method if you would like, but remember that printing trees can be a difficult task. Make sure to leave enough time for the other parts of the activity.

Use the following code to test whether your BST is functioning correctly.

undefinedClick here to copy
Expected output of test code
Part 3: Add Functionality to the BST Class
In this portion of the activity, we will be implementing the add() method for the BST class to improve its functionality. Using your understanding of BSTs and how they work, implement the add() method:

add(): This function should accept an int or a BSTNode and add it to the BST.
If the input is of any type other than BSTNode or int, raise a ValueError.
If the input is an int, create a BSTNode with that int as the value.
If the node with the same value is already in the tree, change nothing.
It may be helpful to add a class attribute called self.contents to keep track of the contents of the tree. This could be a list of integers. Each time a node is added, the value of the node is added to the list. Then you only need to check whether the data you want to add is in self.contents.
If the tree is empty (root == None), set the root equal to the new node.
The node must be added in the correct spot on the tree. Use a helper function, add_node(), to do this.
To help you think through how the adding algorithm works, we will go through a detailed example with pictures.

Let's start with an empty tree. If we add a node with the value 8 to the tree, it should look like this:

undefined
Now we add a node with the value 14 to the tree. Because the tree isn't empty, we have to start at the root of the tree. In this case, the root is 8. 14 is bigger than 8, so we look at 8's right child. It's empty (or None), so we add 14 as the right child of 8.

Remember, as we show the tree growing in these images, that the way we wrote our printing code, children shown above their parents are "right" children, and childen shown below their parents are "left" children.

undefined
Next we want to add 3. Again, the tree isn't empty, so we start with the root, 8. 3 is smaller than 8, so we look at 8's left child. It's empty, so we add 3 as the left child of 8.

undefined
The last example is the hardest. We want to add the value 13 to the tree. We start at the root, 8. 13 is bigger than 8, so we move right. Now we are at node 14. 13 is smaller than 14, so we look left. 14's left child is empty, so we put 13 there.

undefined
Do you see how the last example, of adding 13, is essentially a repeat of the first problems? We can use recursion to move to the correct spot on the tree, then place our node correctly.

In order to traverse and add the new node, create a helper function called add_node().

The helper function should accept a "current node" as well as the "new node".
If the new node is bigger than the current node, recursively call the helper function with current.right. If the new node is bigger than the current node, recursively call the helper function with current.left. Continue traversing this way until the spot in the direction you want to go is empty.
When you find that the direction you want to go is empty, set the current node's correct direction equal to the new node to add it.
Make sure to add the (value of) the node to self.contents once it has been added to the tree.
Once you have used our earlier example to test your code, use the following code to test whether your BST.add() method is functioning correctly.

undefinedClick here to copy
Expected output of BST code.
Solution
If you get stuck or would like to check your work, refer to the solution guide.

Bonus
If you would like an additional challenge, try to implement a remove() method for your BST. This function should do the following:

remove(): This function should accept an int or a BSTNode, and remove the node with that value from the BST.
If the input is of any type other than BSTNode or int, raise a ValueError.
If the input is a BSTNode, extract the int value from it to use for comparisons.
If a node with the requested value is not in the tree (remember to check self.contents), raise a ValueError.
After checking each of the above conditions, create a helper function to recursively traverse the tree and remove the correct node.
The helper function should accept a current node, a value to remove, and a previous node that defaults to None.
There are two conditions: We have found the node we want to remove (current.data == remove_value), or we have not.
When you find the node you're looking for, there are three conditions: the node to remove (current) has 0 children, 1 child, or 2 children.
If current has 0 children, then check whether current is the right child of previous or the left child of previous. Set previous.right or previous.left (whichever child current is) to None.
If current has 1 children, there are 2 cases: current has a right child or current has a left child.
If current has a left child, check whether current is the right child of previous or the left child of previous. Set previous.right or previous.left (whichever child current is) to current.left.
If current has a right child, check whether current is the right child of previous or the left child of previous. Set previous.right or previous.left (whichever child current is) to current.right.
If current has 2 children, do the following:
Create a class attribute called self.nodes and set it equal to an empty list.
Create a new helper function called traverse_tree to fill in self.nodes.
self.traverse_tree should accept a node to start from.
Use a similar logic to how we print the tree: if the node we pass in is not None, call traverse_tree on node.right, then add node.data to self.nodes, then call traverse_tree on node.left.
Once self.nodes is filled (it should be full of int values, not BSTNodes), use list.remove() to remove the value of the node we're deleting from the list of nodes.
Use list.remove() to remove the value of the node we're deleting from self.contents.
Check whether current is the right child of previous or the left child of previous. Set previous.right or previous.left (whichever child current is) to None.
Loop through the list self.nodes, and use self.add() to add each value into the tree. This will make sure that no descendants are lost.
If the current node is not the node we're looking for, there are two conditions: the node we want has a value lower than current, or a value higher than current.
If the value to remove is higher than current, recursively call self.remove_node with current.right, remove_value, and prev = current.
If the value to remove is lower than current, recursively call self.remove_node with current.left, remove_value, and prev = current.
Use the following code to test whether your BST.remove() method is functioning correctly.

undefinedClick here to copy
output of removing 1 from tree
undefinedClick here to copy
output of removing 10 from tree