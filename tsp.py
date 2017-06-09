import sys
from tsp_algos import *
from timeit import default_timer as timer


def read_file(filename):
    cities = []
    with open(filename, 'r') as input_file:
        for line in input_file:
            city = line.strip().split()
            cities.append((int(city[0]), int(city[1]), int(city[2])))
        return cities


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
