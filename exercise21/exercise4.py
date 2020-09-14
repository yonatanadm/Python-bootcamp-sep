class Clerk:

    def __init__(self, name):
        self.name = name
        self.clerk = []

    def add_to_clerk(self, customer):
        self.clerk.append(customer)

    def remove_form_clerk(self):
        customer = self.clerk[0]
        print(customer)
        self.clerk.pop(0)


def wait(input_c, clerks_d):
    if input_c[1] in clerks_d:
        clerks_d.get(input_c[1]).add_to_clerk(input_c[2])
    else:
        clerks_d[input_c[1]] = Clerk(input_c[1])
        clerks_d[input_c[1]].add_to_clerk(input_c[2])


def next_c(input_c, clerks_d):
    if len(clerks_d.get(input_c[1]).clerk) > 0:
        clerks_d.get(input_c[1]).remove_form_clerk()
    else:
        for c in clerks_d.values():
            if len(c.clerk) > 0:
                c.remove_form_clerk()
                break


commands = {
    "wait": wait,
    "next": next_c,

}
clerks = {}
input_user = str(input())
command = input_user.split(' ')
while command[0] in commands:
    commands[command[0]](command, clerks)
    input_user = str(input())
    command = input_user.split(' ')
