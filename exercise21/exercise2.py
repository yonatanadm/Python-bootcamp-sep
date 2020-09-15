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

"""
Uri's comments:
==============

* Very good! This code works.
* Line 14: When you start a comment, it's better to use the same indentation as the following
  line, or the line before - the line the comment is about:

# should print 10
print(MyCounter.count)

"""
