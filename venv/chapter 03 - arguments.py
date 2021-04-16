# args and kwargs, or arguments and keyword arguments


# args - arguments

def user_info(name, age, city):

    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info("Janet", 58, "Oklahama City")
# user_info(34, "New York") -> returns error

# These are positional arguments because Python is reading these arguments_ in order_,
# in the position that they are given in the function definition.

# The *args allows a function to take any number of positional arguments.

# kwargs - keyword arguments

def user_info_kwargs(name, age=0, city="Tucson"):

    '''This functoin prints name, age, and city from an argument provided to the function.'''

    print("{} is {} years old, from {}".format(name, age, city))

user_info_kwargs("Janet", 58, "Oklahama City")
user_info_kwargs("Micah")

# And with keyword arguments, you don't need to follow the positional order of the argument.

user_info_kwargs(age=56, name="Kadeem")

# The **kwargs allows a function to take any number of keyword arguments.

# Any formal or required arguments that you wish to pass into a function, must be passed before *args and **kwargs.


# *args and **kwargs
def application(fname, lname, email, company, salary, hire_date):
    print("{} {} works at {}. Her email is {}".format(fname, lname, company, email))
    print("Her salary is {}".format(salary))
    print("She was hired {}".format(hire_date))

application("Jess", "Ingrass", "mail @ mail.com", "Teach Code", 75000, hire_date = "September 2010")