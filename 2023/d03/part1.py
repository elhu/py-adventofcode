"""2023 D03"""
import itertools
import re
import sys

class SurroundingCoords:
    """Iterator that returns all coords surrounding a rectangle."""
    def __init__(self, top_left, bottom_right):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.x = top_left[0]-1
        self.y = top_left[1]-1

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.x > self.bottom_right[0]:
            raise StopIteration

        value = (self.x, self.y)
        self.y += 1
        if self.y > self.bottom_right[1] + 1:
            self.y = self.top_left[1]-1
            self.x += 1

        if value[1] >= self.top_left[1] and value[1] <= self.bottom_right[1] and value[0] >= self.top_left[0] and value[0] < self.bottom_right[0]:
            return next(self)
        return value

def solve(lines):
    res = 0
    for i, line in enumerate(lines[1:-1], 1):
        matches = re.finditer(r'(\d+)', line)
        for match in matches:
            for coord in SurroundingCoords((match.start(), i), (match.end(), i)):
                if lines[coord[1]][coord[0]] != '.':
                    res += int(match.group())
                    break
    return res

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    lines = list(itertools.chain(['.' * (len(data[0])+2)], map(lambda line: f'.{line}.', data), ['.' * (len(data[0])+2)]))
    print(solve(lines))
