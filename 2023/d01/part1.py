"""2023 D01E01"""
import sys
import re

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().split('\n')[:-1]
    res = 0
    for line in data:
        digits = re.findall(r'(\d)', line)
        res += int(digits[0]) * 10 + int(digits[-1])
    print(res)
