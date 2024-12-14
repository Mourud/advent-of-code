from aoc_input_fetcher import fetch_input


def main():
    data = fetch_input(__file__)
    # data = '12345\n'
    # data = '2333133121414131402\n'
    print(part1(data))
    print(part2(data))


class CheckSumCalulator:

    def __init__(self):
        self.id = 0
        self.checksum = 0

    def calculate_checksum(self, iterations, num):
        for _ in range(iterations):
            self.checksum += (num*self.id)
            self.id += 1
    def get_checksum(self):
        return self.checksum



def part1(data):
    data_m = data
    checksum = CheckSumCalulator()
    start = 0
    end = len(data_m)-2
    while(start<end):
        start_num = int(data_m[start])
        if start%2 == 0:
            checksum.calculate_checksum(start_num, start//2)
        else:
            nums_left = int(data_m[end])
            for _ in range(start_num):
                if nums_left == 0:
                    if end - 2 < start:
                        break
                    end -= 2
                    nums_left = int(data_m[end])

                checksum.calculate_checksum(1, end//2)
                nums_left -= 1
            data_m = data_m[:end] + str(nums_left)
        start += 1

    while(start<len(data_m)):
          start_num = int(data_m[start])
          if start%2 == 0:
            checksum.calculate_checksum(start_num, start//2)
            start += 2
          
    return checksum.get_checksum()

def part2(data):
    pass

main()