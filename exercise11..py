from random import randint

"""
Exercise 1
"""

# x = int(input("Choose number 1: "))
# max_n = x
# for i in range(2, 11):
#     y = int(input(f"Choose number {i}: "))
#     if y > max_n:
#         max_n = y
#
# print("--- The max number is: ", max_n)

"""
Uri's comments:
==============

* Why did you comment this exercise?

"""

"""
Exercise 2
"""

while True:
    try:
        age = int(input("Enter your age: "))
        print(f" Your age in months is:  {age * 12}")
        break
    except ValueError:
        age = print("Sorry - you typed something that wasn't a number")

"""
Uri's comments:
==============

* Very good! This code works.
* print doesn't return a value so there is no sense in assigning its return value
  into a variable.
  PyCharm warns about it.

"""

"""
Exercise 3
"""
lines = []
while True:
    line = input("Write Something: ")
    if len(line) == 0:
        break
    lines.append(line)
lines.reverse()
for i in range(len(lines)):
    print(lines[i])

"""
Uri's comments:
==============

* Very good! This code works.
* You don't need i in the for loop. You can do just:

for line in lines:
    print(line)

"""

"""
Exercise 4
"""
while True:
    x = randint(1, 1000000)
    if x % 13 == 0 and x % 15 == 0 and x % 7 == 0:
        print(x)
        break

"""
Uri's comments:
==============

* Very good! This code works.

"""

"""
Exercise 5
"""
x = randint(1, 10)
y = randint(1, 10)
minD = max(x, y)

while not ((minD % x == 0) and (minD % y == 0)):
    minD += 1
print(f"The smallest multiplier of {x} and {y} is  {minD}")

"""
Uri's comments:
==============

* Very good! This code works.
* Just a note - this works for numbers <= 10, but if the numbers would be
  bigger (~6 digits or more), then this algorithm is very unefficient,
  and there are algorithms which are much more efficient.

"""

"""
Exercise 6
"""

x = randint(1, 100)
y = int(input("Enter your guess: "))
while y != x:
    if y > x:
        print("Too big")
    else:
        print("Too small")
    y = int(input("Enter a new guess: "))
print("--- You succeeded")

"""
Uri's comments:
==============

* Very good! This code works.

"""
