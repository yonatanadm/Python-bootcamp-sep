from random import randint

"""
Exercise 1
"""

x=int(input("Choose number 1: "))
maxN=x
for i in range(2,11):
    y = int(input(f"Choose number {i}: "))
    if y>maxN:
        maxN=y

print("--- The max number is: ",maxN)

"""
Uri's comments:
==============

* Very good! This code works.
* Python has the function "max", and it's better to use it than implementing
  your own solution. You don't have to "invent the wheel" each time again.
  You can just add y to a list, and then `max(<>list>)`.

"""

"""
Exercise 2
"""

while True:
    try:
      age = int(input("Enter your age: "))
      print(f" Your age in months is:  {x * 12}")
      break
    except ValueError:
      age = print("Sorry - you typed something that wasn't a number")

"""
Uri's comments:
==============

* You used age and then x, x is undefined - this raises an exception.
* Formatting - It's common and recommended to use 4 spaces for each indentation level.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.

"""
"""
Exercise 3
"""
lines=[]
while True:
    line = input("Write Something")
    if len(line) == 0:
        break
    lines.append(line)
for i in range(len(lines)-1,-1,-1):
 print(lines[i])

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to add spaces after "Write Something" ("Write Something: ")
  because what I write is attached to the last word.
* Notice that there is also a function to reverse a list in Python, 
  I think you can use it.

"""

"""
Exercise 4
"""
while True:
    x= randint(1, 1000000)
    if x%13==0 and x%15==0 and x%7==0:
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
minD=max(x,y)

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
print(x)
y=int(input("Enter your guess: "))
while y!=x:
    if y>x:
        print("Too big")
    else:
        print("Too small")
    y = int(input("Enter a new guess: "))
print("--- You succeeded")

"""
Uri's comments:
==============

* This code works, but there is no sense in printing the number
  and then asking the user to guess it.
* It's better to end a Python file with a line break.
  If you use PyCharm's Code -> Reformat Code feature, it will be done automatically.

"""
