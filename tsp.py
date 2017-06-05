import math
import sys


def read_file(filename):
    cities = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            city = line.strip().split()
            cities.append((int(city[0]), int(city[1]), int(city[2])))
        print(cities)
        return cities

def find_distance(a, b):
    dx = a[1] - b[1]
    dy = a[2] - b[2]
    result = int(round(math.sqrt(dx * dx + dy * dy)))
    return result


if __name__ == '__main__':
    # input_file = str.argv[2]
    input_file = 'tsp_example_1.txt'
    output_file = input_file + '.tour'

    cities = read_file(input_file)
