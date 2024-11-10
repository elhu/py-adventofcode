import sys

def all_zeros(chain):
    return all([c == 0 for c in chain])

def reduce_diffs(chain):
    chains = [chain]
    while not all_zeros(chains[-1]):
        new_chain = []
        i = 1
        while i < len(chains[-1]):
            new_chain.append(chains[-1][i] - chains[-1][i-1])
            i += 1
        chains.append(new_chain)
    return chains

def compute_next(chains):
    i = len(chains) - 1
    chains[i].append(0)
    while i > 0:
        chains[i-1].append(chains[i-1][-1] + chains[i][-1])
        i -= 1
    return chains[0][-1]

with open(sys.argv[1], 'r') as file:
    data = file.read().strip().split('\n')
    values = [[int(v) for v in value.split()] for value in data]
    res = 0
    for value in values:
        res += compute_next(reduce_diffs(value))
    print(res)
