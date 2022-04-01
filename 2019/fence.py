def cross_prod(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


def diff(v1, v2):
    return [v2[0] - v1[0], v2[1] - v1[1]]


def main(coordinates):
    southest = min(coordinates, key=lambda t: t[1])
    starting_point = coordinates.index(
        min([c for c in coordinates if c[1] == southest[1]])
    )
    n_turns = 0
    cur_point = starting_point
    for i in range(len(coordinates)-2):
        next_point = (i + starting_point + 1) % len(coordinates)
        if next_point == 0:
            next_point = 1
        next_next_point = (next_point + 1) % len(coordinates)
        if next_next_point == 0:
            next_next_point = 1
        diff1 = diff(coordinates[cur_point], coordinates[next_point])
        diff2 = diff(coordinates[next_point], coordinates[next_next_point])
        if cross_prod(diff1, diff2) > 0:
            n_turns += 1
        cur_point = next_point
    return n_turns


if __name__ == "__main__":
    n = int(input())
    coordinates = []
    for i in range(n+1):
        coordinates.append(list(map(int, input().split())))
    print(main(coordinates))
