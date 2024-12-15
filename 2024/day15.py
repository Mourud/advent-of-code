from copy import deepcopy
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

def move_robot(rob, dir, map_area):
    moves = {'>': (1,0), '<' : (-1,0), '^': (0,1), 'v' : (0,-1)}
    move_obj(ROBOT, rob, moves[dir], map_area)
    
    return map_area

def move_obj(OBJ, pos, dir, map_area):
    return
    map_copy = deepcopy(map_area)
    x, y = pos[0] + dir[0] , pos[1] + dir[1]
    # match map_copy[m_y][m_x]:
        # case EMPTY:
        #     return map_copy
        # case BOX:
        #     map_copy[m_y][m_x] = OBJ
        #     move_obj()
        # case _:
        #     return
    


def part2(data):
    pass


main()
