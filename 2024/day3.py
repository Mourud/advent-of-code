from ast import pattern
from input_fetcher import fetch_input
import re

def main():
    input: str | None = fetch_input(__file__)
    print(part1(input))
    print(part2(input))

patrn = "mul\(\d{1,3},\d{1,3}\)"
def part1(input):
    operations = re.findall(patrn, input)
    total = 0
    for operation in operations:
        nums = re.findall(r"\d{1,3}", operation)
        mult = 1
        for num in nums:
            mult *= int(num)
        total += mult
    return total

def part2(input):
    donts = input.split("don't()")
    total = part1(donts[0])
    for dont in donts[1:]:
        dos = re.split("do()", dont)
        for do in dos[1:]:
            total += part1(do)
main()