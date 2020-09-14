import queue


class Clerk:

    def __init__(self, name):
        self.name = name
        self.queue = []

    def add_to_queue(self, customer):
        self.queue.append(customer)

    def remove_form_queue(self):
        customer = self.queue[0]
        print(customer)
        self.queue.pop(0)


flag = False
free_clerk = False
clerks = []
input_user = str(input())
command = input_user.split(' ')
while command[0] == 'wait' or command[0] == 'next':
    if command[0] == 'wait':
        for clerk in clerks:
            if command[1] == clerk.name:
                clerk.add_to_queue(command[2])
                flag = True
                break
        if not flag:
            clerks.append(Clerk(command[1]))
            clerks[len(clerks) - 1].add_to_queue(command[2])
        flag = False
    else:
        for clerk in clerks:
            if command[1] == clerk.name:
                if len(clerk.queue) != 0:
                    clerk.remove_form_queue()
                    break
                else:
                    free_clerk = True
        if free_clerk:
            for clerk in clerks:
                if len(clerk.queue) > 0:
                    clerk.remove_form_queue()
                    break
        free_clerk = False
    input_user = str(input())
    command = input_user.split(' ')
