import math
import sys
from timeit import default_timer as timer


def read_file(filename):
    cities = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            city = line.strip().split()
            cities.append((int(city[0]), int(city[1]), int(city[2])))
        return cities


def find_distance(a, b):
    dx = a[1] - b[1]
    dy = a[2] - b[2]
    result = int(round(math.sqrt(dx * dx + dy * dy)))
    return result


def nearest_neighbor(cities):
    start = cities[0]
    unvisited = cities[1:]
    path = [start]
    path_distance = 0
    while unvisited:
        min_distance = float('inf')
        for neighbor in unvisited:
            distance = find_distance(path[-1], neighbor)
            if min_distance > distance:
                nearest = neighbor
                min_distance = distance
        path_distance += min_distance
        unvisited.remove(nearest)
        path.append(nearest)
    distance = find_distance(nearest, start)
    path_distance += distance
    return (path, path_distance)


if __name__ == '__main__':
    # input_file = str.argv[2]
    input_file = 'test-input-7.txt'
    output_file = input_file + '.tour'

    start = timer()
    cities = read_file(input_file)
    print(nearest_neighbor(cities))
    end = timer()
    print('Time: %s seconds' % str(end - start))
