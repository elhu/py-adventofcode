import sys

PIPES = {
    '|': lambda prev, curr: (curr[0], curr[1] + 1) if prev[1] < curr[1] else (curr[0], curr[1] - 1),
    '-': lambda prev, curr: (curr[0] + 1, curr[1]) if prev[0] < curr[0] else (curr[0] - 1, curr[1]),
    'L': lambda prev, curr: (curr[0], curr[1] - 1) if prev[0] > curr[0] else (curr[0] + 1, curr[1]),
    '7': lambda prev, curr: (curr[0], curr[1] + 1) if prev[0] < curr[0] else (curr[0] - 1, curr[1]),
    'J': lambda prev, curr: (curr[0], curr[1] - 1) if prev[0] < curr[0] else (curr[0] - 1, curr[1]),
    'F': lambda prev, curr: (curr[0], curr[1] + 1) if prev[0] > curr[0] else (curr[0] + 1, curr[1]),
    '.': lambda prev, curr: (_ for _ in ()).throw(ValueError(f"Invalid pipe at position prev: {prev}, curr: {curr}"))
}


START_POS = [('|', '7', 'F'), ('L', '-', 'F'), ('L', 'J', '|'), ('-', '7', 'J')]
START_POS_MAP = {
    '|': [True, False, True, False],
    '-': [False, True, False, True],
    'L': [True, True, False, False],
    '7': [False, False, True, True],
    'J': [True, False, False, True],
    'F': [False, True, True, False],
}

# def move(prev, curr):
#     return PIPES[pipe](curr, pos)

def match_type(to_check, types):
    for i in range(4):
        if types[i] and not to_check[i] in START_POS[i]:
            return False
    return True

def start_pos_pipe_by_type(data, pos):
    to_check = [data[pos[1]-1][pos[0]], data[pos[1]][pos[0]+1], data[pos[1]+1][pos[0]], data[pos[1]][pos[0]-1]]
    matched_type = None
    for k, v in START_POS_MAP.items():
        if match_type(to_check, v):
            matched_type = k
    if matched_type in ('L', '|', 'J'):
        return {'pos': (pos[0], pos[1] - 1), 'pipe': matched_type}
    elif matched_type in ('7', 'F'):
        return {'pos': (pos[0], pos[1] + 1), 'pipe': matched_type}
    return {'pos': (pos[0] - 1, pos[1]), 'pipe': matched_type}


with open(sys.argv[1], 'r') as file:
    data = file.read().strip().split('\n')
    loop = [bytearray('.' * len(line), 'utf8') for line in data]
    prev = (0, 0)
    for y, l in enumerate(data):
        if 'S' in l:
            prev = (l.index('S'), y)
            break
    target = prev
    pt = start_pos_pipe_by_type(data, prev)
    curr = pt['pos']
    s = pt['pipe']
    while curr != target:
        loop[curr[1]][curr[0]] = ord(data[curr[1]][curr[0]])
        prev, curr = curr, PIPES[data[curr[1]][curr[0]]](prev, curr)
    loop[curr[1]][curr[0]] = ord(s)
    count = 0
    for line in loop:
        state = False
        prev = None
        for idx, c in enumerate(line):
            if c == ord('.'):
                if state:
                    count += 1
            elif c == ord('|'):
                state = not state
            elif c == ord('L'):
                state = not state
                prev = 'L'
            elif c == ord('J') and prev == 'L':
                state = not state
                prev = None
            elif c == ord('F'):
                state = not state
                prev = 'F'
            elif c == ord('7') and prev == 'F':
                state = not state
                prev = None
    print(count)

