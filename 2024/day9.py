from aoc_input_fetcher import fetch_input


def main():
    data = fetch_input(__file__)
    print(part1(data))
    print(part2(data))



def part1(data):
    free_space = 0
    for i, num in enumerate(data[:-1]):
        if i%2 ==1:
            free_space += int(num)
    id = 0
    checksum = 0
    start = 0
    end = len(data)-2
    nums_left = int(data[end])

    while(start<end):
        start_num = int(data[start])
        if start%2 == 0:
            for _ in range(start_num):
                checksum += start/2*id
                id += 1
            start += 1
        else:
            for _ in range(start_num):
                if nums_left == 0:
                    end -= 1
                    nums_left = int(data[end])
                checksum += end/2*id
                nums_left -= 1
                id += 1
    return checksum        
    for i, num in enumerate(data[:-1]):
        if i%2 == 0:
            # Possibly optimize with a sum formula?
            for x in range(int(num)):
                checksum=i*id
                id += 1
        else:
            end = len(data) - 2
            data[end]
                

    pass

def part2(data):
    pass

main()