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
    start_city = cities[0]
    unvisited = cities[1:]
    path = [start_city]
    path_distance = 0
    while unvisited:
        min_distance = float('inf')
        for city in unvisited:
            distance = find_distance(path[-1], city)
            if min_distance > distance:
                nearest_city = city
                min_distance = distance
        path_distance += min_distance
        unvisited.remove(nearest_city)
        path.append(nearest_city)
    distance = find_distance(nearest_city, start_city)
    path_distance += distance
    return path, path_distance


def repeated_nearest(cities):
    if len(cities) <= 500:
        iterations = len(cities)
    elif len(cities) >= 5000:
        iterations = 5
    else:
        iterations = 50
    best_distance = float('inf')
    for i in range(0, iterations):
        unvisited = cities[:]
        start_city = cities[i]
        path = [start_city]
        unvisited.remove(start_city)
        path_distance = 0
        while unvisited:
            min_distance = float('inf')
            for city in unvisited:
                distance = find_distance(path[-1], city)
                if min_distance > distance:
                    nearest_city = city
                    min_distance = distance
            path_distance += min_distance
            unvisited.remove(nearest_city)
            path.append(nearest_city)
        distance = find_distance(nearest_city, start_city)
        path_distance += distance
        if path_distance < best_distance:
            best_path = path
            best_distance = path_distance
    return best_path, best_distance


def get_total_distance(cities):
    total_distance = 0
    last_city = None

    for i in xrange(len(cities) - 1):
        current_city = cities[i]
        next_city = cities[i + 1]

        total_distance += find_distance(current_city, next_city)
        last_city = next_city

    # Add the distance to go back to the starting city
    total_distance += find_distance(last_city, cities[0])

    return total_distance


def two_opt_swap(route, i, j):
    new_route = route[0:i]
    new_route.extend(reversed(route[i:j + 1]))
    new_route.extend(route[j + 1:])

    return new_route


def two_opt(cities):
    isImproved = True

    best_route = cities
    best_distance = get_total_distance(best_route)

    while isImproved:
        isImproved = False

        for i in xrange(len(best_route) - 1):
            for j in xrange(i + 1, len(best_route)):
                new_route = two_opt_swap(best_route, i, j)
                new_distance = get_total_distance(new_route)

                if new_distance < best_distance:
                    best_distance = new_distance
                    best_route = new_route
                    isImproved = True
                    break

            if isImproved:
                break

    return best_route, best_distance


def write_results(filename, path, distance):
    with open(filename, 'wb') as output:
        output.write(str(distance) + '\n')
        for city in path:
            output.write(str(city[0]) + '\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: python tsp.py { nn || rnn || 2opt } { filename.txt }')
        exit(1)

    input_file = str(sys.argv[2])
    output_file = input_file + '.tour'

    start = timer()
    input_cities = read_file(input_file)

    if str(sys.argv[1]) == 'nn':
        (final_path, final_distance) = nearest_neighbor(input_cities)
    elif str(sys.argv[1]) == 'rnn':
        (final_path, final_distance) = repeated_nearest(input_cities)
    elif str(sys.argv[1]) == '2opt':
        (final_path, final_distance) = two_opt(input_cities)
    else:
        print('Usage: python tsp.py { nn || rnn || 2opt } { filename.txt }')
        exit(1)

    write_results(output_file, final_path, final_distance)
    end = timer()
    print('Time: %s seconds' % str(end - start))
