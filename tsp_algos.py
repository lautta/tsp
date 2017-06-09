import math


def find_distance(a, b):
    dx = a[1] - b[1]
    dy = a[2] - b[2]
    result = int(round(math.sqrt(dx * dx + dy * dy)))
    return result


# Greedy nearest neighbor algorithm
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


# Repeated greedy nearest neighbor algorithm
def repeated_nearest(cities):
    if len(cities) >= 5000:
        iterations = 500
    else:
        iterations = len(cities)
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


# 2-opt algorithm
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
