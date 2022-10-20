# Activity: Practice OOP Fundamentals

To better understand object-oriented programming through Python, we will work in a [Activity_1_Practice_OOP_Fundamentals.py](Activity_1_Practice_OOP_Fundamentals.py) to expand the features of a class, and practice writing our own classes.

## 1. Getting Started

First, let's explore the code we already have. Take a moment to recap the elements we see here and call some of the methods that exist on our `Car` class.

## 2. Building a Race

Next, let's try defining a class to represent a race. Our `Race` class will accept a name, to denote which race it is, a list of cars in the race, and a limit of cars that can be included (you can't have an unlimited number of cars in a race, we just call that traffic). Define the `Race` constructor with at least the following attributes:

- `name` - should be defined on instantiation
- `driver_limit` - should also be defined on instantiation
- `drivers` - can be instantiated as an empty list

Once you have built that, test your class to make sure it works.

```python
my_course = Race('Seattle 500', 4)
print(my_course.name, my_course.driver_limit, my_course.drivers)

# prints Seattle 500 4 []
```

Well done! You have successfully defined a class with attributes and generated an object: an instance of that class.

## 3. Building a Driver Class

Now let's build a Driver class. This class should have the following attributes:

- `name`
- `age`
- `ranking`

And the following **static** attribute:

- `number_of_drivers`

And be sure to update your constructor to increment the number_of_drivers by one (1) each time an instance of the class is instantiated.

Next, add a method to the driver class called get_ranking which **returns** that instance's specific ranking.

```python
my_driver = Driver('Dale Earnhardt', 29, 100)
print(my_driver.get_ranking())

# prints a returned value of "100"
```

## 4. Adding Methods to the Race Class

After you have defined your Race class, add the following methods:

- `add_driver`
  - If the number of drivers already assigned to the race does not exceed the driver_limit, it should add a driver to the drivers list.
- `get_average_ranking`
  - Returns the average ranking of drivers

Then test your code! Generate the following drivers:

| Name             | Age | Ranking |
|------------------|-----|---------|
| Lewis Hamilton   |  36 |      83 |
| Eliud Kipchoge   |  36 |      95 |
| Sebastian Vettel |  34 |      76 |
| Ayrton Senna     |  34 |      99 |

Then add them to your race. Finally, find the average ranking of drivers in your race!

```python
print(course.get_average_ranking())
# prints a returned value of 88.5
```

Couldn't get it done, or code simply isn't working? That's ok! Solution code can be found at [this Replit](Activity_1_Practice_OOP_Fundamentals_Solution.py).

## Bonus

If you finish early, try your hand at applying some of these bonus features:

- Try adding a class method to your `driver` class that returns the average rating of all drivers globally.
- Add logic to the `Race.add_driver` method that prevents a driver from being added to a race if they are not within 10 points of the current average ranking in that race.
