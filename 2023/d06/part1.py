"""2023 D06"""

from functools import reduce
import operator
import re
import sys

def winning_combinations(race_info):
    (time, distance) = race_info
    res = 0
    for i in range(time+1):
        if (time - i)*i > distance:
            res += 1
    return res

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    rounds = []
    times = [int(n) for n in re.split('\s+', data[0])[1:]]
    distances = [int(n) for n in re.split('\s+', data[1])[1:]]
    results = [winning_combinations(race_info) for race_info in zip(times, distances)]
    print(reduce(operator.mul, results))
