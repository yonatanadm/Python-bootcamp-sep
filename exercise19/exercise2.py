import sys

if len(sys.argv) == 1:
    print("You need to pass a list of grades through the command line")
    exit(1)
grades = tuple(map(int, sys.argv[1::]))
avg = (sum(grades) / len(grades))
final_grades = []
for grade in grades:
    if grade > avg:
        final_grades.append(grade)
print(final_grades)

"""
Uri's comments:
==============

* Very good! This code works.
* Notice that the assignment expects exactly 20 grades. You should check that
  the number of grades is 20 and display an error message if not.

"""
