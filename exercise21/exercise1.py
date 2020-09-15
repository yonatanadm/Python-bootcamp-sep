class Summer:
    def __init__(self):
        self.sum = 0

    def add(self, *nums):
        for num in nums:
            self.sum += num

    def print_total(self):
        print(self.sum)


s = Summer()
t = Summer()

s.add(10, 20)
t.add(50)
s.add(30)

# should print 60
s.print_total()

# should print 50
t.print_total()
