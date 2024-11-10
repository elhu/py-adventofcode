import sys
import re
import math

def parse_node(node):
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', node)
    return [m[1], m[2], m[3]]

with open(sys.argv[1], 'r') as file:
    parts = file.read().strip().split('\n\n')
    instructions = parts[0].strip()

    nodes = {parse_node(n)[0]: parse_node(n)[1:] for n in parts[1].split('\n')}
    curr_nodes = [n for n in nodes.keys() if n[-1] == 'A']

    rounds = []
    for curr_node in curr_nodes:
        c = 0
        while curr_node[-1] != 'Z':
            if instructions[c%len(instructions)] == 'L':
                curr_node = nodes[curr_node][0]
            else:
                curr_node = nodes[curr_node][1]
            c += 1
        rounds.append(c)
    print(math.lcm(*rounds))
