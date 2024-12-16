from copy import Error, deepcopy
from aoc_input_fetcher import fetch_input
from traitlets import default


ROBOT = '@'
BOX = 'O'
WALL = '#'
EMPTY = '.'


def main():
    data = fetch_input(__file__)
    data = parse_input(data)
    print(part1(data))
    print(part2(data))

def parse_input(data):
    d = [[],[]]
    i = 0
    for line in data.splitlines():
        if line == '':
            i += 1
            continue
        elif i == 0:
            d[i].append(list(line))
        else:
            d[i] += list(line)
    return d


def part1(data):
    map_area , commands = data

    rob = find(ROBOT, map_area)[0]
    for command in commands:
        map_area = move_robot(rob, command, map_area)
    boxes = find(BOX,map_area)
    print(len(boxes))
    return sum(box[0] * 100 + box[1] for box in boxes)

def find(obj_to_find, map_area):
    obj_list = []
    for y, row in enumerate(map_area):
        for x, obj in enumerate(row):
            if obj == obj_to_find:
                obj_list.append((x,y))
    return obj_list

def move_robot(pos, dir, map_area):
    moves = {'>': (1,0), '<' : (-1,0), '^': (0,1), 'v' : (0,-1)}
    curr_obj = ROBOT
    updated_map_area = deepcopy(map_area)
    curr_pos = pos
    while(curr_obj == ROBOT or curr_obj == BOX):
        x,y = tuple(a + b for a, b in zip(curr_pos, moves[dir]))
        curr_obj = map_area[y][x] # can't think if this is always correct : double check
        if map_area[y][x] == EMPTY:
            return updated_map_area
        if map_area[y][x] == WALL:
            return map_area
        updated_map_area[y][x] = curr_obj
        curr_pos = x,y
    raise Error("Unidentified Object")

    


def part2(data):
    pass


main()
