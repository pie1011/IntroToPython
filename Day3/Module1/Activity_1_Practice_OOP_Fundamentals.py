class Car:
    def __init__(self, name, max_speed):
        self.name      = name
        self.max_speed = max_speed

    def start(self):
        print('Vroom!')

    def talk(self, driver):
        print(f'Hello, {driver}, I am {self.name}.')

myCar      = Car('Kitt',   180)
myOtherCar = Car('Speedy',  55)

myCar.talk('Michael')

"""
Create Driver Class
"""



"""
Create Race Class
"""



"""
Test Code
"""

s0 = Driver('Dale Earnhardt',   29, 100)
s1 = Driver('Lewis Hamilton',   36,  83)
s2 = Driver('Eliud Kipchoge',   36,  95)
s3 = Driver('Sebastian Vettel', 34,  76)
s4 = Driver('Ayrton Senna',     34,  99)

course = Race('Seattle 500', 4)

course.add_driver(s0)
course.add_driver(s1)
course.add_driver(s2)
course.add_driver(s3)
course.add_driver(s4)

print(course.get_average_ranking())
