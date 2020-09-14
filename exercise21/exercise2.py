class MyCounter:
    count = 0

    def __init__(self):
        MyCounter.count += 1

    def print(self):
        print(MyCounter.count)


for _ in range(10):
    c1 = MyCounter()

    # should print 10
print(MyCounter.count)
