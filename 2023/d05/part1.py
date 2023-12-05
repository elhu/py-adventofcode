"""2023 D05"""

import re
import sys

class Mapping:
    def __init__(self, line):
        matches = re.match(r'(\d+) (\d+) (\d+)', line)
        dest, orig, size = int(matches.group(1)), int(matches.group(2)), int(matches.group(3))
        self.destination = range(dest, dest+size)
        self.origin = range(orig, orig+size)

class Map:
    def __init__(self, data):
        self.mappings = [Mapping(line) for line in data]

class Almanac:
    def __init__(self, data):
        self.maps = []
        for map_data in data[1:]:
            self.maps.append(Map(map_data.split('\n')[1:]))
        self.seeds = [int(n) for n in data[0].split(' ')[1:]]

    def find_seed_location(self, seed):
        for m in self.maps:
            for mapping in m.mappings:
                if seed in mapping.origin:
                    seed = mapping.destination.start + (seed - mapping.origin.start)
                    break
        return seed

    def find_first_location(self):
        locations = [self.find_seed_location(seed) for seed in self.seeds]
        return min(locations)


with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n\n')
    almanac = Almanac(data)
    print(almanac.find_first_location())
