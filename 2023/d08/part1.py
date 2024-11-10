import sys
import re

def parse_node(node):
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', node)
    return [m[1], m[2], m[3]]

with open(sys.argv[1], 'r') as file:
    parts = file.read().strip().split('\n\n')
    instructions = parts[0].strip()

    nodes = {parse_node(n)[0]: parse_node(n)[1:] for n in parts[1].split('\n')}
    curr_node = 'AAA'
    c = 0
    while curr_node != 'ZZZ':
        if instructions[c%len(instructions)] == 'L':
            curr_node = nodes[curr_node][0]
        else:
            curr_node = nodes[curr_node][1]
        c += 1
    print(c)
