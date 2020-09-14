import sys

if len(sys.argv) == 1:
    print("You need to pass at least one computer name through the command line")
    exit(1)
hosts = tuple(sys.argv[1::])
hosts_ne = []
map = {}
with open('files/host.txt', 'r', encoding='UTF-8') as f:
    for line in f:
        (host_name, ip) = line.split("=")
        map[host_name] = ip
for name in hosts:
    if name in map:
        print(f"The ip of {name} is: {map.get(name)}", end='')
    else:
        print(f"The host {name} does not exist")
