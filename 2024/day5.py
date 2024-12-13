from aoc_input_fetcher import fetch_input
from bintrees import AVLTree

def main():
    input = fetch_input(__file__)
    parsed_input = parse_input(input)
    print(part1(parsed_input))
    print(part2(parsed_input))

def parse_input(input):
    combined_list = [[], []]
    i = 0
    for line in input.splitlines():
        if line == "":
            i += 1
            continue
        combined_list[i].append(line)
    return combined_list

def part1(input):
    num_map = get_rules(input[0])
    
    total = 0
    for line in input[1]:
        list_of_nums = [int(x) for x in line.split(',')]
        is_rules_broken = False
        for i, num in enumerate(list_of_nums[:-1]):
            if num in num_map.keys():
                rules = num_map[num]
                for rule_num in list_of_nums[i+1:]:
                    if rule_num in rules:
                        is_rules_broken = True
                        break
                if is_rules_broken:
                    break
        if not is_rules_broken:
            total += list_of_nums[int(len(list_of_nums)/2)]
    return total

def get_rules(rules):
    num_map = {}
    for line in rules:
        nums = [int(x) for x in line.split('|')]
        num_map.setdefault(nums[1], set())
        num_map[nums[1]].add(nums[0])
    return num_map




def part2(input):
    rule_map = get_rules(input[0])
    total = 0
    for line in input[1]:
        list_of_nums = [int(x) for x in line.split(',')]
        fixed_line = []
        for i, num in enumerate(list_of_nums[:-1]):
            if num in rule_map.keys():
                rules = rule_map[num]
                for rule_num in list_of_nums[i+1:]:
                    if rule_num in rules:
                        fixed_line = fix(list_of_nums, rule_map)
                        break
                if len(fixed_line) > 0:
                    break
        if len(fixed_line) > 0:
            total += fixed_line[int(len(fixed_line)/2)]
    return total

def fix(lon, rule_map):
    if len(lon) == 0:
        return lon
    rules ={k:v for k,v in rule_map.items() if k in lon}
    brokes = []
    rem = []
    n = lon[0]
    for val in lon[1:]:
        if val in rules[n]:
            brokes.append(val)
        else:
            rem.append(val)
    return fix(brokes, rules) + [n] + fix(rem, rules)

   
    


main()