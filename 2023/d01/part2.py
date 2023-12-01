"""2023 D01E01"""
import sys
import re

def convert(number):
    return {
        'one': 1, 'two': 2, 'three': 3, 
        'four': 4, 'five': 5, 'six': 6, 
        'seven': 7, 'eight': 8, 'nine': 9
    }.get(number) or int(number)

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().split('\n')[:-1]
    res = 0
    for line in data:
        digits = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        res += convert(digits[0]) * 10 + convert(digits[-1])
    print(res)
