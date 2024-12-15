from aoc_input_fetcher import fetch_input
# from send_answer import submit_answer

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
    data_m = data
    checksum = CheckSumCalulatorO()
    end = len(data_m)-2
    ids = [0] * (len(data) - 1)
    for i in range(1, len(data)-1):
        ids[i] = ids[i-1] + int(data[i-1])

    while(end >= 0):
        fsp = 1
        point_to_add = end
        while(fsp < end):
            if int(data_m[fsp]) < int(data_m[end]):
                fsp += 2
            else:
                point_to_add = fsp
                break
        fid = ids[point_to_add] + int(data[point_to_add]) - int(data_m[point_to_add])
        checksum.calculate_checksum(int(data_m[end]), end // 2, fid)
        data_m = data_m[:point_to_add] + str((int(data_m[point_to_add]) - int(data_m[end]))) + data_m[point_to_add+1:end]
        end -= 2          
    return checksum.get_checksum()

class CheckSumCalulatorO:

    def __init__(self):
        self.checksum = 0

    def calculate_checksum(self, iterations, num, id):
        for _ in range(iterations):
            self.checksum += (num*id)
            id += 1
    def get_checksum(self):
        return self.checksum

main()