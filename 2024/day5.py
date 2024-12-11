from input_fetcher import fetch_input


def main():
    input = fetch_input(__file__)
    print(input)
    parsed_input = parse_input(input)
    print(part1(parsed_input))
    print(part2(parsed_input))

def parse_input(input):
    rules = []
    pages = []
    combined_list = [rules, pages]
    i = 0
    for line in input.splitlines():
        if line == "":
            i += 1
        combined_list[i].append(line)
    return combined_list

def part1(input):
    
    pass

def part2(input):
    pass


main()