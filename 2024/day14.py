from aoc_input_fetcher import fetch_input

# area = [11, 7]
area = [101, 103]

def main():
    data = fetch_input(__file__)
    # data = f"p=0,4 v=3,-3\np=6,3 v=-1,-3\np=10,3 v=-1,2\np=2,0 v=2,-1\np=0,0 v=1,3\np=3,0 v=-2,-2\np=7,6 v=-1,-3\np=3,0 v=-1,-2\np=9,3 v=2,3\np=7,3 v=-1,2\np=2,4 v=2,-3\np=9,5 v=-3,-3"
    data = parse_data(data)

    area = [103,101]
    # area = [7, 11]
    print(part1(data))


def parse_data(data):
    robots = []
    for line in data.splitlines():
        pos, vel = line.split(" ")
        pos = pos.split("p=")[1]
        pos = pos.split(",")
        pos = [int(p) for p in pos]
        vel = vel.split("v=")[1]
        vel = vel.split(",")
        vel = [int(v) for v in vel]
        robots.append([pos, vel])
    return robots


def part1(data):
    for t in range(100):
        for robot in data:
            robot[:] = update(robot)
            print(robot)
    for robot in data:
        add_into_q(robot[0])
    total = 1
    for row in quarters:
        for num_of_robots in row:
            total *= num_of_robots
    return total


quarters = [[0, 0], [0, 0]]


def add_into_q(pos):
    i = 0
    j = 0
    i_mid = (area[0]) // 2
    j_mid = (area[1]) // 2
    if pos[0] != i_mid and pos[1] != j_mid:
        if pos[0] > i_mid:
            i = 1
        if pos[1] > j_mid:
            j = 1
        quarters[i][j] += 1


def update(robot):
    pos, vel = robot
    for i in range(2):
        pos[i] += vel[i]
        pos[i] %= area[i]
    return [pos, vel]


main()
