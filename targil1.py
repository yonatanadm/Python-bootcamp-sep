"""
Exercise 1
"""

age=int(input("Enter your age: "))
ageMonth=age*12
print("Your age in months is: ",ageMonth)

"""
Uri's comments:
==============

* Very good! This code works.
* I recommend styling your code according to PEP-8. You can also use PyCharm's
  Code -> Reformat Code feature. For example, spaces around "=", a space after comma etc.
  This is relevant to all your exercises.
* Here is how your code looks reformatted:

age = int(input("Enter your age: "))
ageMonth = age * 12
print("Your age in months is: ", ageMonth)

* In Python it's common to use variable names in lowercase. You can use "_" to separate between words.
  For example, use "age_month" instead of "ageMonth".
  
"""

"""
Exercise 2
"""
ageMonth=int(input("Enter your age in months: "))
age=ageMonth/12
print("Your age is: ",age)

"""
Uri's comments:
==============

* Very good! This code works.
* It's better to round the number of years, for example to 2 or 3 digits.

"""

"""
Exercise 3
"""

x=int(input("Choose a number: "))
if x%7==0:
    print("Boom")

"""
Uri's comments:
==============

* Very good! This code works.

"""

"""
Exercise 4
"""
x=(input("Choose a number: "))
if x.__contains__('7') or int(x)%7==0 :
    print("Boom")

"""
Uri's comments:
==============

* Very good! This code works.
* Although you can use __contains__, in Python it's common to use "in"
  instead, so you can write `'7' in x` instead of `x.__contains__('7')`.
  I think in the background, `in` calls `__contains__`.

"""

"""
Exercise 5
"""
x=int(input("Choose the first number: "))
y=int(input("Choose the second number: "))
z=int(input("Choose the third number: "))
print("The max num you choose is: ", max(x,y,z))

"""
Uri's comments:
==============

* Very good! This code works.

"""

"""
Exercise 6
"""
a=int(input("Choose the first number in the series: "))
d=int(input("Choose the series difference: "))
n=int(input("Choose the number of organs in the series: "))
print("The sum of the series is: ", n*((2*a)+(d*(n-1)))/2)

"""
Uri's comments:
==============

* Very good! This code works.

"""
