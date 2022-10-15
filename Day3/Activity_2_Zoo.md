# Activity: Zoo

To better understand the four pillars of object-oriented programming, use [Activity_2_Zoo.py](Activity_2_Zoo.py) classes to code up a zoo simulator.

## 1. Getting Started

First, let's explore the code we already have. Take a moment to recap the elements we see here and call on some of the methods that exist on our `Person`, `Zoo`, and `Animal` classes.

## 2. Building a Customer

Next, let's try defining a class to represent a customer. A customer is a person, so the `Customer` class inherits from the `Person` class, and should call the `Person` constructor inside the `Customer` constructor. In addition to their name and age, a customer should have two `Booleans`, one each for whether they have a ticket for the zoo, and whether they are currently in the zoo. Initialize these `Booleans` to false in the constructor for your `Customer` class.

## 3. Adding Methods to Our Customer Class

After you have defined your `Customer` class and written the constructor, add the following methods to your class:

- `buy_ticket`
  - The Customer's `hasTicket` attribute should be set to `True`, and an appropriate message should be printed out. As a bonus, print a different message depending on whether an adult or child's ticket is purchased.
- `enter_zoo`
  - This method should accept the `Zoo` object of the zoo the customer is attempting to enter. If the `Customer`'s `hasTicket` attribute is `True`, it is set to `False`, the `Zoo`'s `add_customer` method is called, and the `Customer`'s `inZoo` attribute is set to `True`. If the `Customer`'s `hasTicket` attribute is `False`, print a message prompting the customer to purchase a ticket before attempting to enter the zoo.
- `exit_zoo`
  - Accepts the `Zoo` object of the zoo the customer is attempting to leave. If the `Customer`'s `inZoo` attribute is `True`, set it to `False` and call the `Zoo`'s `remove_customer` method.

## 4. Adding Animal Subclasses

Now that your `Customer` class is complete, let's create some animal classes. Each subclass should call the `Animal` constructor in its own constructor and should override the `make_noise` and `eat_food` methods to print appropriate messages.

Make sure to create at least three different `Animal` subclasses. We suggest `Fish`, `Bird`, and `Chimp`.

## 5. Testing Your Code

When all of the classes are complete, use the provided code to test your class implementations.

```python
nycZoo = Zoo("NYC Zoo")

salmon = Fish("salmon")
robin = Bird("robin")
bonobo = Chimp("bonobo")

nycZoo.add_animals([salmon, robin, bonobo])

alice = Customer("Alice",25)
bob = Customer("Bob",20)
charlie = Customer("Charlie",10)
dave = Customer("Dave",30)

for c in [alice, bob, charlie, dave]:
    c.buy_ticket()
    c.enter_zoo(nycZoo)

nycZoo.visit_animals()
for c in [alice, bob, charlie, dave]:
    c.exit_zoo(nycZoo)
```

This should result in several lines being printed to your terminal, detailing people purchasing tickets and entering the zoo, visiting the animals and learning some facts, and then exiting the zoo.

## Solution

If you need extra help, the solution code can be found [here](https://replit.com/@SD-Team/zooSimulatorSolution#main.py).
