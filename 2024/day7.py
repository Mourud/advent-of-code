from aoc_input_fetcher import fetch_input

def main():
    data = fetch_input(__file__)
    data = parse_data(data)
    print(part1(data))
    print(part2(data))

def parse_data(data):
    equations = []
    for line in data.splitlines():
        eq = line.split(':')
        res = int(eq[0])
        nums = [int(x) for x in eq[1].split()]
        equations.append((nums, res))
    return equations

def part1(data):
    total = 0
    for eq in data:
        if maths_is_possible(eq):
            total += eq[1]
    return total

def maths_is_possible(eq):
    nums, res = eq

    def rec(nums, total):
        if len(nums) == 0:
            return total == res
        return (rec(nums[1:], total=total+nums[0])) or rec(nums[1:], total*nums[0]) 

    return rec(nums, 0)
    
def part2(data):
    total = 0
    for eq in data:
        if maths_is_possible2(eq):
            total += eq[1]
    return total

def maths_is_possible2(eq):
    nums, res = eq

    def rec(nums, total):
        if len(nums) == 0:
            return total == res
        n = nums[0]
        digits = 0
        while(n != 0):
            rem = n% 10
            n //= 10 
            digits += 1
        multiplier = 10 ** digits
      
        return rec(nums[1:], total=total+nums[0]) or rec(nums[1:], total*nums[0])  or rec(nums[1:],  (total) * multiplier + nums[0])
    return rec(nums, 0)
main()