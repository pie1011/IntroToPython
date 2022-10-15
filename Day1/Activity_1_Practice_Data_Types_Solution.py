## Section 1 - variables and functions: 

# Question 1: Create two variables. One should be a string data type, and the other should be of type int.

#note that your variables could be named anything, and can have any string and int value you want
first = "hello"
second = 5

# Use a single print statement to print both variables:

#both of the following methods are acceptable
print(first, second)
print(f"{first} {second}")

# Question 2: Create a Python function that prints a greeting with a name as the parameter.

def greeting(name):
  print("hello,", name)

# Invoke the function with a name argument of your choosing:
greeting("Alejandro")


## Section 2 - lists:

# Question 3: Create a list of your favorite movies with  at least 4 elements:

my_list = ["12 Angry Men", "Memento", "The Drak Knight", "Inception"]

# Question 4: Use a print statement to print the list item at the index of 1:
print(my_list[1])

# Question 5: Append a movie to the end of your list:
my_list.append("Encanto")

# Use a print statement to print this ammended list:
print(my_list)


## Section 3 - dictionaries:

# Question 6: Create a dictionary named 'cellphone' with 2 key:value pairs that are the properties of your cellphone.
#The keys should be: "color" and "number".
#Fill out the values on your own:

cellphone = {
    "color": "yellow",
    "number": 1234567890
}  

# Question 7: Access a value from inside the dictionary (Try to print the value of the 'color' property).

print(cellphone["color"])


## Section 4 - strings:

# Question 8: Create a variable and store a string with multiple words in it:

my_string = "panic at the disco"

# Question 9: Utilize the method that capitalizes the first letter of each word in your string - store this new string in a new variable:

band = my_string.title()

# Use a print statement to print the new string:

print(band)


#Bonus:

# Question 10: Uncomment and look into this nested dictionary - try to relate your knowledge of objects and arrays in JavaScript.

students_in_order = {
  1: {'name': 'Esteban', 'age': '27', 'eye color': 'blue'},
  2: {'name': 'Jackson', 'age': '22', 'eye color': 'brown'},
  3: {'name': 'Zayn', 'age': '26', 'eye color': 'green'}
}

# Question 10 A: Write a print function that outputs the second student in the dictionary
print(students_in_order[2]) 

# Question 10 B: Write a print statement that outputs the name "Zayn" using the dictionary
print(students_in_order[3]["name"]) 

# Question 10 C: Write a print statment that outputs the age of Esteban from the dictionary
print(students_in_order[1]['age'])