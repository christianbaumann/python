# for loop

fruits = ["apple", "orange", "pears", "cherries", "grapes"]

for fruit in fruits:
    print("Would you like {}?".format(fruit))

# prints 1 to 10
for number in range(1,11):
    print("Number {}".format(number))


# while loop

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1

# loop control
# The _break_ statement indicates that when you see it, the loop should end and go on to the next statement in the
# program that is outside of the loop.
# The _continue_ statement skips the current part of the loop and moves on to the next part of the loop.
# The _pass_ statement skips any part of the loop where pass appears. This is best used for testing code,
# but make sure you don't forget to remove the pass statement when you're ready for your code to go into production.

temp_f = 40
while temp_f > 32:
    print("The water is {} degrees.".format(temp_f))
    temp_f -= 1
    if temp_f == 33:
        break

for number in range(1,11):
    if number == 7:
        print("We're skipping number 7.")
        continue
    print("This is the number {}.".format(number))

for number in range(1,11):
    if number == 3:
        pass
    else:
        print("The number is {}.".format(number))