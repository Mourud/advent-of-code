from aoc_input_fetcher import fetch_input

def main():
    data = fetch_input(__file__)
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
                antinodes.update( find_antinodes(i, j, data))
    return len(antinodes)


def find_antinodes(i, j, data):

    antinodes = set()

    for index in range(j+1, len(data)):
        if data[i][j] == data[i][index]:
            print("HOR")
            dist = index - j
            if index + dist < len(data):
                antinodes.add((i, index + dist) )# 2in - j
            if j - dist >= 0:
                antinodes.add((i, j - dist)) # 2j - in
    for index in range(i+1, len(data)):
        if data[i][j] == data[index][j]:
            dist = index - i
            if index + dist < len(data):
                antinodes.add((index + dist, j))
            if i - dist >= 0:
                antinodes.add((i - dist, j))
    for dist in range(len(data) - max(i,j)):
        if data[i][j] == data[i+dist][j+dist]:

            if i - dist >= 0 and j - dist >= 0:
                antinodes.add((i- dist, j- dist))
            if i + (2*dist) < len(data) and j + (2*dist) < len(data):
                antinodes.add((i + (2*dist), j + (2*dist)))
            
    return antinodes

def part2(data):
    pass


main()
