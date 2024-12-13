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
    num_map = {}
    for line in input[0]:
        nums = [int(x) for x in line.split('|')]
        num_map.setdefault(nums[1], set())
        num_map[nums[1]].add(nums[0])
    total = 0
    for line in input[1]:
        list_of_nums = [int(x) for x in line.split(',')]
        is_rules_broken = False
        for i, num in enumerate(list_of_nums):
            if num in num_map.keys():
                rules = num_map[num]
                print(num, rules, list_of_nums[i+1:])
                for rule_num in list_of_nums[i+1:]:
                    if rule_num in rules:
                        is_rules_broken = True
                        break
                
        if not is_rules_broken:
            total += list_of_nums[int(len(list_of_nums)/2)]
    return total


def part2(input):
    pass


main()