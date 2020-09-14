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
