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