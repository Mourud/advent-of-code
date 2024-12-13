from aoc_input_fetcher import fetch_input


def main():
    input = fetch_input(__file__)
    input_matrix = parse_input(input)
    print(part1(input_matrix))
    print(part2(input_matrix))

def parse_input(input):
    mat = []
    for i, line in enumerate(input.splitlines()):
        mat.append([])
        for c in line:
            mat[i].append(c)
    return mat


def part1(input):
    guard = find_guard(input)
    return guard_sim(guard, input)
    

    pass
def find_guard(input):
    for i, row in enumerate(input):
        for j, pos in enumerate(row):
            if pos in ['v', '<', '>', '^']:
                return (i,j,pos)
            
def guard_sim(guard, input):
    unique_pos = set()
    y = guard[0]
    x = guard[1]
    dir = guard[2]
    while (True):
        # xxxxxxxxxxxxxxxxxxx = input[x+0][y-2:y] + [guard[2]] + input[x][y+1:y+3]
        unique_pos.add((y,x))
        if dir == 'v':
            y += 1
            if not guard_on_map((y,x,dir), input):
                return len(unique_pos) 
            if (input[y][x] == '#'):
                y -=1
                dir = '<'      
        elif dir == '<':
            x -= 1
            if not guard_on_map((x,y,dir), input):
                return len(unique_pos) 
            if (input[y][x] == '#'):
                x += 1
                dir = '^'
        elif dir == '^':
            y -= 1
            if not guard_on_map((x,y,dir), input):
                return len(unique_pos) 
            if (input[y][x] == '#'):
                y += 1
                dir = '>'
                
        elif dir == '>':
            x += 1
            if not guard_on_map((x,y,dir), input):
                return len(unique_pos) 
            if (input[y][x] == '#'):
                x -= 1
                dir = 'v'
            


def guard_on_map(guard, area):
    x = guard[0]
    y = guard[1]

    if x > len(area) - 1 or x < 0:
        return False
    if y > len(area[x]) - 1 or y < 0:
        return False
    return True

def guard_sim2(guard, input):
    unique_pos = set()
    y = guard[0]
    x = guard[1]
    dir = guard[2]
    time_since_unique = 0
    
    while (True):
        
        if time_since_unique > len(unique_pos):
            return 1
        xxxxxxxxxxxxxxxxxxx = input[y][x-2:x] + [dir] + input[y][x+1:x+3]
        pos = (y,x)
        if pos not in unique_pos:
            time_since_unique = 0
            unique_pos.add(pos)
        else:
            time_since_unique += 1
        if dir == 'v':
            y += 1
            if not guard_on_map((y,x,dir), input):
                return 0
            if (input[y][x] == '#'):
                y -=1
                dir = '<'      
        elif dir == '<':
            x -= 1
            if not guard_on_map((x,y,dir), input):
                return 0
            if (input[y][x] == '#'):
                x += 1
                dir = '^'
        elif dir == '^':
            y -= 1
            if not guard_on_map((x,y,dir), input):
                return 0
            if (input[y][x] == '#'):
                y += 1
                dir = '>'
        elif dir == '>':
            x += 1
            if not guard_on_map((x,y,dir), input):
                return 0
            if (input[y][x] == '#'):
                x -= 1
                dir = 'v'

                



def part2(input):
    guard = find_guard(input)
    total = 0
    for i, row in enumerate(input):
        for j, pos in enumerate(row):
            if pos not in ['v', '<', '>', '^', '#']:
                input[i][j] = '#'
                total += guard_sim2(guard, input)

        
    return total
main()