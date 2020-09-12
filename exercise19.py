"""
Exercise 1
"""

login = {
    'apple': 'red',
    'lettuce': 'green',
    'lemon': 'yellow',
    'orange': 'orange',
}
name = input("Enter your name: ")
password = input("Enter your password: ")
if (name, password) in login.items():
    print("Welcome Master")
else:
    print("INTRUDER ALERT")

"""
Exercise 2
"""

import sys
grades = tuple(map(int, sys.argv[1::]))
avg = (sum(grades) / len(grades))
final_grades = []
for grade in grades:
    if grade > avg:
        final_grades.append(grade)
print(final_grades)

"""
Exercise 3
"""
hosts = tuple(sys.argv[1::])
hosts_ne = []
map = {}
with open('host.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        (host_name, ip) = line.split("=")
        map[host_name] = ip
for name in hosts:
    if name in map:
        print(f"The ip of {name} is: {map.get(name)}", end='')
    else:
        print(f"The host {name} does not exist")

"""
Exercise 4
"""


def check(s1, s2):
    # the sorted strings are checked
    if sorted(s1) == sorted(s2):
        return True
    return False


words = []
flag = 0
with open('host.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        words.append(line)
size = len(words)

for i in range(size):
    if '' == words[i]:
        continue
    for j in range(i + 1, size):
        if '' == words[j]:
            continue
        if check(words[i], words[j]):
            print(words[j], end='')
            words[j] = ''
    print(words[i])
