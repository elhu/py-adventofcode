"""2023 day 04"""

import sys
import re

def compute_score(left, right):
    match_count = len((set(left) & set(right)))
    if match_count > 0:
        return pow(2, match_count-1)
    else:
        return 0

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n')
    res = 0
    for line in data:
        parts = re.split(r'(?:: | \| )', line)
        left = [int(x) for x in re.split('\s+', parts[1].strip())]
        right = [int(x) for x in re.split('\s+', parts[2].strip())]
        res += compute_score(left, right)

    print(res)
