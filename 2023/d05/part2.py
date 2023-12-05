"""2023 D05"""

import re
import sys
import itertools

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
        self.seeds = []
        seed_parts = [int(n) for n in data[0].split(' ')[1:]]
        for i in range(0, len(seed_parts), 2):
            self.seeds.append(range(seed_parts[i], seed_parts[i]+seed_parts[i+1]))

    def in_seed_range(self, source):
        for seed in self.seeds:
            if source in seed:
                return True
        return False

    def find_location_source(self, seed):
        for m in reversed(self.maps):
            for mapping in m.mappings:
                if seed in mapping.destination:
                    seed = mapping.origin.start + (seed - mapping.destination.start)
                    break
        return seed

    def find_first_location(self):
        for i in itertools.count():
            source = self.find_location_source(i)
            if self.in_seed_range(source):
                return i

with open(sys.argv[1], 'r', encoding='utf8') as file:
    data = file.read().strip().split('\n\n')
    almanac = Almanac(data)
    print(almanac.find_first_location())
