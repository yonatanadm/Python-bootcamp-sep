"""
Exercise 1
"""

age = int(input("Enter your age: "))
ageMonth = age * 12
print("Your age in months is: ", ageMonth)

"""
Exercise 2
"""
age_month = int(input("Enter your age in months: "))
age = age_month / 12
print("Your age is: ", age)

"""
Exercise 3
"""

x = int(input("Choose a number: "))
if x % 7 == 0:
    print("Boom")

"""
Exercise 4
"""
x = (input("Choose a number: "))
if '7' in x or int(x) % 7 == 0:
    print("Boom")

"""
Exercise 5
"""
x = int(input("Choose the first number: "))
y = int(input("Choose the second number: "))
z = int(input("Choose the third number: "))
print("The max num you choose is: ", max(x, y, z))

"""
Exercise 6
"""
a = int(input("Choose the first number in the series: "))
d = int(input("Choose the series difference: "))
n = int(input("Choose the number of organs in the series: "))
print("The sum of the series is: ", n * ((2 * a) + (d * (n - 1))) / 2)
