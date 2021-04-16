# comment

# Variables can either be named with lower-case or upper-case letters or numbers.
# And they can start with an underscore also.

# If you’re using a multi-name variable,
# you need to make sure that you’re using underscores between each of the words.

_cars = 23
cars = 24
CARS = 25

number_of_cars = 23
kind_of_cars = "Ferrari"

print(_cars)
print(cars)
print(CARS)

print(number_of_cars)
print(kind_of_cars)

"""
multi-line comment
3 quotes to start and 3 quotes to end
"""

'''
another multiline comment
'''

name = "Janelle Jones"
type_of_car = "Rolls Royce"
school = "Foundation Elementary School"

print(name + school)
print(name + " " + school)
print(name + " works at " + school + ".")
#python string.format()
print("{} works at {}.".format(name, school))