from aoc_input_fetcher import fetch_input

def main():
    data = fetch_input(__file__)
    # data = f"............\n........0...\n.....0......\n.......0....\n....0.......\n......A.....\n............\n............\n........A...\n.........A..\n............\n............"
    data = parse_data(data)
    print(part1(data))
    print(part2(data))

def parse_data(data):
    return [[ant for ant in row] for row in data.splitlines()]


def part1(data):
    antinodes = set()

    for i, row in enumerate(data):
        for j, antenna in enumerate(row):
            if antenna != '.':
                s = find_antinodes(i, j, data)
                if (s):
                    print(s)
                antinodes.update(s)
    return len(antinodes)


def find_antinodes(i, j, data):
    antinodes = set()
    for x in range(i, len(data)):
        for y in range(len(data)):
            if x == i and y == j:
                continue
            if data[i][j] == data[x][y]:
                v_dist = x - i
                h_dist = y - j
                an1 = (i - v_dist , j - h_dist)
                if is_in_bounds(an1, len(data)):
                    antinodes.add(an1)
                an2 = (x + v_dist, y + h_dist)
                if is_in_bounds(an2, len(data)):
                    antinodes.add(an2)
                     
    return antinodes

def is_in_bounds(pos, size):
    for p in pos:
        if p < 0 or p >= size:
            return False
    return True
            


def part2(data):
    pass


main()
